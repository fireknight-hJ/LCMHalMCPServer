---
name: find_demo_source_info
description: 如何查找程序源码中的有效信息：通过 demo 所在的配置文件读取其 DB 目录和项目原目录，然后在目录中查找想要的内容
---

# 查找 Demo 源码与 DB 中的有效信息

## 1. 定位 Demo 配置与路径

Demo 的**主配置**在：`testcases/server/<vendor>/<demo_name>/lcmhal_config.yml`

该文件里关键字段：
- **`script_path`**：当前 demo 所在目录（与 `testcases/server/<vendor>/<demo_name>` 一致）
- **`db_path`**：该 demo 对应的**数据库/工作目录**，一般形如 `.../dbs_server/DATABASE_<demo_name>`，存放构建产物、ai_log 等
- **`src_path`** / **`proj_path`**：**项目源码根目录**（STM32 工程、LwIP 等原始源码所在位置）

示例（LwIP_StreamingServer）：
```yaml
script_path: ".../testcases/server/stm32/LwIP_StreamingServer"
db_path: ".../dbs_server/DATABASE_LwIP_StreamingServer"
src_path: ".../posixGen_Demos/LwIP_StreamingServer"
proj_path: ".../posixGen_Demos/LwIP_StreamingServer"
```

## 2. 在项目源码中查找

要查「某个函数是否在源码里、如何实现」（例如 `HAL_ETH_MspInit`、`HAL_NVIC_EnableIRQ`）：

1. **确定项目源码目录**  
   从 `lcmhal_config.yml` 读取 `src_path` 或 `proj_path`（二者通常相同）。若该路径不在当前仓库，需在**实际构建该 demo 的机器/环境**上查看。

2. **在源码中搜索**  
   在 `src_path` 下对 `.c`、`.h` 做内容搜索，例如：
   ```bash
   grep -r "HAL_ETH_MspInit" <src_path>/
   grep -r "HAL_NVIC_EnableIRQ" <src_path>/
   ```

3. **说明**  
   当前 lcmhalmcp 仓库里**通常没有**项目源码，只有 `testcases/.../emulate/` 下的配置和构建产物（如 `output.elf`、`syms.yml`）。因此「在 ai_log 或当前仓库里找函数体」不可行，需用上述 `src_path` 指向的原始工程。

## 3. 在 DB 目录中查找

`db_path` 下可能有：
- **`lcmhal_ai_log/`**：Agent 会话日志（JSON），记录替换了哪些函数、替换内容等，**不包含**反汇编或源码正文。
- 符号表、构建中间文件等。

若需「某次构建/替换」的结论可从 ai_log 的 session 日志里查 `replacement_code`、`ReplacementUpdate` 等。

## 4. 结合 ELF 反汇编（无源码时）

当没有 `src_path` 可访问或想确认当前二进制内容时：

1. **用 ELF 反汇编**  
   demo 的固件一般在 `script_path/emulate/output.elf`（或 `db_path` 下对应路径）。
   ```bash
   arm-none-eabi-nm -n <path_to_output.elf>   # 看符号
   arm-none-eabi-objdump -d <path_to_output.elf>  # 反汇编
   ```

2. **注意**  
   若 `nm` 里没有某个符号（如 `HAL_ETH_MspInit`），说明当前固件中**没有**该函数（未链接或已被替换/内联），反汇编里也看不到其「函数体」。

## 5. 流程小结

| 目标 | 做法 |
|------|------|
| 查某函数在源码中的实现 | 读 `lcmhal_config.yml` 取 `src_path`，在 `src_path` 下 grep 该函数名 |
| 查某次构建做了哪些替换 | 读 `lcmhal_config.yml` 取 `db_path`，在 `db_path/lcmhal_ai_log/` 查 session 日志 |
| 查当前固件里有没有某函数 | 对 `script_path/emulate/output.elf` 运行 `nm` 查符号 |
| 看某函数在二进制里的指令 | 对 `output.elf` 用 `objdump -d`，再按地址或符号 grep |

## 6. 注意事项

- `script_path` 一定在 lcmhalmcp 仓库内；`db_path`、`src_path`、`proj_path` 可能在仓库外。
- 若本机没有挂载或无法访问 `src_path`，只能依赖 ELF 反汇编推断；此时若符号不存在，则无法看到「源码级」函数体。
