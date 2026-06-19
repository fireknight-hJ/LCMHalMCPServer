## 用飞书连接 OpenClaw 的完整流程（实战版）

> 环境：Linux 本机 + 全局 `openclaw` CLI + 飞书中国区。  
> 目标：在飞书里直接和 OpenClaw Agent 对话。

---

### 1. 前置条件

- **Node.js / npm 已安装**（例如 `node v22.13.0`）
- **可以使用全局 npm 包**（`npm install -g` 正常）
- 有一个 **企业飞书账号**，能访问飞书开放平台。

可以先确认一下 `openclaw` 是否存在：

```bash
which openclaw
openclaw --version
```

[图片：终端中运行 openclaw --version 的效果截图]

---

### 2. 安装 / 升级 OpenClaw CLI

推荐先升级到最新版本，避免插件 API 不兼容：

```bash
npm install -g openclaw
```

如果当前 shell 的工作目录已经被删除（例如你在一个被删掉的目录里执行），会看到类似：

```text
Error: ENOENT: no such file or directory, uv_cwd
```

这种情况下，先切换到一个存在的目录再执行：

```bash
cd ~
npm install -g openclaw
```

---

### 3. 安装 Feishu 插件

#### 3.1 清理旧的插件缓存（如果之前手动折腾过）

```bash
rm -rf ~/.openclaw/extensions/feishu
```

这样可以避免“duplicate plugin id”“plugin already exists”等老版本残留问题。

#### 3.2 通过 OpenClaw 官方插件机制安装 Feishu

```bash
openclaw plugins install @openclaw/feishu
```

命令过程中，你会看到类似日志：

- `Downloading @openclaw/feishu…`
- `Installing to /home/用户名/.openclaw/extensions/feishu…`
- `Installed plugin: feishu`
- `feishu_chat / feishu_wiki / feishu_drive / feishu_bitable: Registered ...`

[图片：终端中 openclaw plugins install @openclaw/feishu 的输出]

---

### 4. 在飞书开放平台创建机器人应用

#### 4.1 打开飞书开放平台

- 浏览器访问：`https://open.feishu.cn/app`
- 用企业飞书账号登录。

[图片：飞书开放平台应用列表页面]

#### 4.2 创建企业自建应用

- 点击「创建企业自建应用」
- 填写：
  - **应用名称**（和用途相关就行）
  - **应用描述**
  - 选择一个图标
- 创建完成后，进入该应用详情页。

[图片：创建企业自建应用的表单页面]

#### 4.3 获取 App ID 和 App Secret

在左侧菜单中找到 **「凭证与基础信息」**：

- 复制 **App ID**（形如 `cli_xxxxx`）
- 点击小眼睛 / 查看按钮，复制 **App Secret**

这两个值稍后要粘到 `openclaw` 配置里，请妥善保管，不要泄露。

[图片：凭证与基础信息页面，标出 App ID 和 App Secret 位置]

#### 4.4 配置权限（Scope）

在左侧菜单中找到 **「权限管理」**：

- 点击「批量导入」或类似按钮
- 将官方文档提供的 JSON `scopes` 内容粘进去（包含 `im:message.receive_v1`、`im:message:send_as_bot` 等权限）
- 保存并申请权限（企业自建通常自动通过）

[图片：权限管理页面，批量导入 scopes 界面]

#### 4.5 开启机器人能力

在左侧菜单中找到 **「应用功能 / 机器人」**：

- 启用「机器人」能力
- 设置机器人名称、头像
- 保存配置

[图片：机器人能力配置页面]

---

### 5. 配置事件订阅（长连接 WebSocket）

目标：让飞书可以把 `im.message.receive_v1` 事件推到本地 OpenClaw Gateway。

#### 5.1 启动本地 Gateway（必须先跑起来）

开一个单独终端，前台运行：

```bash
openclaw gateway
# 或如果你全程想用 dev profile:
# openclaw --dev gateway
```

这条命令需要保持运行，不要关掉。飞书保存“长连接事件订阅”时会尝试连接这个网关。

[图片：终端中 openclaw gateway 正在前台运行]

#### 5.2 在飞书中配置事件订阅

回到飞书开放平台，在你的应用详情中：

- 左侧菜单进入 **「开发配置 → 事件订阅 / 事件与回调」**
- 选择事件接收方式：**「使用长连接接收事件（WebSocket）」**
- 在订阅事件列表中添加事件：
  - `im.message.receive_v1`
- 点击「保存」

如果这一步提示：

> 未检测到应用连接信息，请确保长连接建立成功后再保存配置

通常是因为：

- `openclaw gateway` 没有在本地跑，或者
- 用错了 profile（比如配置用了默认 profile，你却跑的是 `--dev`，反之亦然）

确保网关在跑，重试保存即可。

[图片：事件订阅页面，选择长连接并添加 im.message.receive_v1 事件]

#### 5.3 发布应用版本

在左侧菜单进入 **「版本管理与发布」**：

- 创建版本 → 提交审核
- 企业自建应用通常很快通过
- 发布版本，使机器人在当前租户中可用

[图片：版本管理与发布页面，显示已发布版本状态]

---

### 6. 在 OpenClaw 中配置 Feishu 渠道

#### 6.1 使用向导配置渠道

在另一个终端执行：

```bash
openclaw channels add
# 或：
# openclaw --dev channels add
```

按引导选择：

- 选择 **Feishu / Lark (飞书)** 作为渠道
- 输入：
  - **App ID**：刚才复制的 `cli_xxx`
  - **App Secret**：刚才复制的 `xxx`
- 选择 Feishu DM 策略：
  - 一般直接用默认的 **Pairing（推荐）**
- 为这个 Feishu 账号设置一个内部的 **account name**，例如：
  - `default`
  - `feishu-main`
  - `personal`

> 这个名称仅在 OpenClaw 配置中使用，不影响飞书里的机器人名字。

[图片：openclaw channels add 交互过程截图，显示选择 Feishu 和输入 App ID/Secret 的界面]

#### 6.2 确认 Feishu 渠道已启用

执行：

```bash
openclaw channels list
```

理想输出中应包含类似：

```text
Chat channels:
- Feishu default: configured, enabled
```

[图片：openclaw channels list 输出，标出 Feishu default: configured, enabled]

---

### 7. 启动 Gateway 并测试消息收发

确保网关在前台运行（第 5 步已经起过的话，只要没关就行）：

```bash
openclaw gateway
# 或
openclaw --dev gateway
```

再开一个终端实时查看日志：

```bash
openclaw logs --follow
```

#### 7.1 首次私聊机器人：配对流程

在飞书客户端：

- 搜索你的机器人名称
- **使用私聊** 打开对话，发送一条消息，例如：“你好”

如果一切配置正常，机器人会先返回类似内容（或者你能在日志里看到）：

```text
OpenClaw: access not configured.
Your Feishu user id: ou_4d3c57d382f7a534f5841e9528cc3142
Pairing code: AV87HHQ3
Ask the bot owner to approve with:
openclaw pairing approve feishu AV87HHQ3
```

这表示：

- 当前 `dmPolicy` 为 `pairing`（默认）
- 新用户（你的 Feishu 账号）需要被「配对批准」才能开始正式对话

[图片：飞书客户端中首次给机器人发送“你好”后的回复截图]

#### 7.2 通过配对请求

在一个终端执行：

```bash
openclaw pairing approve feishu AV87HHQ3
```

将命令中的 `AV87HHQ3` 替换为日志中实际看到的 Pairing code。

也可以先查看所有待配对请求：

```bash
openclaw pairing list feishu
openclaw pairing approve feishu <CODE>
```

配对成功后，再在飞书给机器人发送消息，就会正式开始对话并收到 OpenClaw 的回复。

[图片：终端中 pairing approve 执行成功的截图]

---

### 8. 常见问题与排查思路

#### 8.1 飞书端保存事件订阅时提示“未检测到应用连接信息”

检查：

- 本地是否正在运行：
  - `openclaw gateway` 或 `openclaw --dev gateway`
- 配置渠道用的 profile 和运行 gateway 的 profile 是否一致：
  - 如果你是 `openclaw channels add`（无 `--dev`），gateway 也用 `openclaw gateway`
  - 如果你是 `openclaw --dev channels add`，就用 `openclaw --dev gateway`
- 一般本机不会有防火墙问题，但如有特殊安全策略也需确认。

#### 8.2 日志提示 `feishu failed to load` 或 `Cannot find module '@sinclair/typebox'`

- 通常是旧插件残留或手动拷贝插件导致的版本不匹配
- 清理并按第 3 步重新安装：

```bash
rm -rf ~/.openclaw/extensions/feishu
openclaw plugins install @openclaw/feishu
```

#### 8.3 日志提示 `plugin feishu: duplicate plugin id detected`

- 说明配置里有多个名为 `feishu` 的插件条目（例如手动加了一份 + 安装了一份）
- 一般不影响功能，但推荐：
  - 只保留 `openclaw plugins install @openclaw/feishu` 安装出来的那一份
  - 删除手动拷贝或自己写的重复入口

#### 8.4 已经收到了 “Pairing code”，却仍然没回应

- 确认已经执行了：

```bash
openclaw pairing approve feishu <CODE>
```

- 并确保命令中的 `<CODE>` 与日志中的完全一致（包括大小写）。

---

### 9. 小结

- **OpenClaw 侧关键 3 步**：
  - 安装并升级 CLI：`npm install -g openclaw`
  - 安装 Feishu 插件：`openclaw plugins install @openclaw/feishu`
  - 配置渠道：`openclaw channels add` → 填 `App ID / Secret` → 确认 `Feishu ... configured, enabled`

- **飞书侧关键 4 步**：
  - 创建企业自建应用 → 记下 `App ID / Secret`
  - 配好权限 + 开启机器人能力
  - 配置事件订阅：长连接 + `im.message.receive_v1`
  - 发布应用版本

- **运行时关键 3 步**：
  - 前台跑网关：`openclaw gateway`（或 `openclaw --dev gateway`）
  - 实时看日志：`openclaw logs --follow`
  - 首次用户配对：`openclaw pairing approve feishu <CODE>`

照这个流程走一遍，就可以稳定地用飞书和 OpenClaw 双向对话。后续可以在此基础上再做多 Agent 路由、群聊策略（`groupPolicy` / `requireMention`）等进阶玩法。

