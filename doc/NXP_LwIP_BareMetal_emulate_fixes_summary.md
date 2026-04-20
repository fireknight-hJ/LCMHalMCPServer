# NXP LwIP BareMetal 等 emulate 问题与修复摘要

## INVALID Fetch: addr=0x600024bc（entry 在 XIP 但 flash 被映射到 0x20000000）

**现象**：模拟器报 `[-] INVALID Fetch: addr= 0x00000000600024bc size=2, pc= 0x00000000600024bc`，exit_code 255。

**原因**：i.MX RT 上代码从 **FlexSPI/XIP** 运行，entry_point 在 **0x6xxxxxxx**；fuzzemu-helper 从 ELF 解析出的 flash 有时落在 **0x20000000**（如某 section 在 RAM），导致 output.bin 被映射到 0x20000000，而 CPU 从 0x600024bd 取指，该地址未映射代码。

**修复**：在 `fix_flash_size()` 中，若 config 里 **entry_point** 在 0x60000000..0x60400000 且当前 flash base 为 0x20000000，则把 flash 的 base 改为 **0x60000000**，使取指地址落在映射区内。此时与 flash 同址的 region 会变为 peripheral_ram（0x60000000），按原有逻辑跳过即可。

---

## 为什么“一运行”后 semu_config 末尾（mmio_funcs / model / rules）被截断？

**原因**：`fix_flash_size()` 在按行重写 semu_config 时，会跳过与 flash 同址的 memory_map region（如 NXP 上 **ram** 与 **flash** 都在 0x20000000）。原先逻辑是“直到遇到下一个形如 `  xxx:` 的 region 才停止跳过”。若 **ram 是 memory_map 里最后一个 region**，下一行已是顶层 key（如 `mmio_funcs:`，顶格无缩进），则不会被视为“下一个 region”，`skip_region` 一直不清空，导致从 `mmio_funcs:` 到文件末尾的所有行被误删。

**修复**：在 `skip_region` 分支里增加判断：若当前行是**顶格**（不以空格/制表符开头），说明已离开 memory_map，清空 `skip_region` 并保留该行及后续内容。这样 NXP_LwIP_BareMetal 等“ram 与 flash 同址且 ram 在最后”的 demo 不会再被截断。

---

## 为什么生成的 semu_config.yml 会缺少 rules / model / mmio_funcs？（base 格式问题）

**结论：不是 fuzzemu-helper 故意不写这些字段，而是它依赖的 base_config.yml 格式必须正确；格式不对时 helper 会报错或产出异常，你看到的“缺配置”多半是用了旧的/坏的 base_config 或 base 格式不符合约定。**

### 1. 生成链路

- `semu_config.yml` 由 **fuzzemu-helper** 根据 `emulate/base_config.yml` 生成：
  - 命令：`fuzzemu-helper config base_config.yml -s`
  - 逻辑在 fuzzemu 包的 `helper/dump_config.py` 的 `config()`。
- helper 的行为：
  - 把 `base_config.yml` 当作 **YAML 字典** 加载。
  - **遍历该字典的顶层 key**，每个 key 被视为一个 **ELF 路径**（如 `output.elf`），value 是该 ELF 的配置（handlers、rules、mmio_funcs 等）。
  - 对每个 key 做：用默认 config + cortexm 模板 + **该 value（base_config）** 做 `merge_dict`，再写入 `{model}_config.yml`（即 `semu_config.yml`）。
  - 对 **semu** 模型，若合并后没有 `rules`，会 **直接 raise Exception**，不会写出一份“无 rules”的 semu_config。

因此：**只要 helper 正常跑完，写出的 semu_config 里一定会有 rules**。若你看到“每次生成出来的文件没有 rules/model/mmio_funcs”，通常是下面两种情况之一。

### 2. 根因一：base_config.yml 格式不对（最常见）

helper 要求：

- **有且仅有一个顶层 key**，且必须是 **ELF 文件名**，例如：`output.elf`。
- 该 key 的 **value 必须是一个字典**，且其中包含 **`rules`**（以及你需要的 `mmio_funcs`、`model` 等）。

正确示例：

```yaml
output.elf:
  rules: semu_rule.txt
  enable_native: false
  emulate_mode: emulate
  loop_whitelist: [...]
  handlers: {...}
  mmio_funcs: [...]
```

若 base_config 是下面任一情况，就会出问题：

- **平铺结构**（没有 `output.elf` 这一层），例如：
  ```yaml
  rules: semu_rule.txt
  handlers: {...}
  ```
  此时 helper 会拿 `rules`、`handlers` 等字符串/字典当“ELF 路径”去 `open()`，要么报错退出，要么行为异常，**不会**正常写 semu_config。你看到的“没有 rules”的 semu_config 往往是**之前某次成功生成留下的旧文件**，并不是这次 helper 刚写的。
- **顶层 key 不是 `output.elf`**（例如拼错或写成了别的名字），导致合并用的不是我们预期的那份配置。
- **`output.elf` 下没有 `rules`**：合并后 config 里没有 `rules`，helper 在写文件前会 raise，**不会**写出新 semu_config；磁盘上的 semu_config 仍是旧的。

“跑别的 demo 没这个问题”通常是因为：别的 demo 的 `base_config.yml` 一直是由本仓库的 `generate_base_config()` 生成的（格式正确），或有问题的 demo 曾经被手改/覆盖过，或某次只生成了“部分” base，导致格式不符合上述约定。

### 3. 根因二：没有真正重新生成 base_config

本仓库里 `generate_semu_config()` 的逻辑是：

- **若已存在 `emulate/base_config.yml`，就不会再调 `generate_base_config()`**。
- 因此若这个已存在的 base 是之前手拷的、或别的脚本写的、或损坏/格式不对，就会一直被复用，fuzzemu-helper 要么报错要么用错配置，你看到的 semu_config 就可能是旧的或缺失字段。

### 4. 本仓库的修复（从根上避免用错 base）

在 `tools/emulator/conf_generator.py` 中：

- 增加了 **base_config 合法性检查** `_base_config_valid()`：
  - 要求存在且可解析为 YAML；
  - 有且仅有一个顶层 key：`output.elf`；
  - `output.elf` 的值是字典且包含 **`rules`**。
- 在 **每次** `generate_semu_config()` 里：
  - 若 `base_config.yml` 不存在，或存在但 **未通过** `_base_config_valid()`，则**强制重新调用** `generate_base_config()`，用当前代码生成一份格式正确的 base（含 `output.elf`、`rules`、`mmio_funcs` 等）。

这样就不会再拿“格式错误或缺 rules 的 base”去跑 fuzzemu-helper，生成的 semu_config 就会一直带有 rules、model、mmio_funcs。

### 5. 你自己排查时可做的检查

1. **看当前 base 格式**  
   打开 `emulate/base_config.yml`，确认：
   - 顶层只有 **一个** key：`output.elf`；
   - 下面有 `rules: semu_rule.txt`（以及需要的 `mmio_funcs`、`model` 等）。
2. **删掉错误 base 再跑一遍**  
   若格式不对，可删掉 `emulate/base_config.yml`，再跑一次完整流程（build + 生成 emulate 配置），让 `generate_base_config()` 重新写一份。
3. **手动跑一次 helper**  
   在 `emulate/` 下执行：  
   `fuzzemu-helper config base_config.yml -s`  
   若 base 格式错误或缺 rules，这里会直接报错；若成功，生成的 semu_config 里会有 rules/model/mmio_funcs。

总结：**配置“消失”是因为 base_config 格式不符合 fuzzemu-helper 的约定或被复用错了；不是 fuzzemu-helper 故意不写。** 本仓库通过“校验 base + 不合格就重新生成 base”从根上避免这个问题。
