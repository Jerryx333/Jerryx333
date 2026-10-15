<h2 align="center">Jerry · 让一群 AI 像团队一样干活</h2>

<p align="center">
我做 AI 编程助手的<b>多模型调度层</b>：强模型当技术负责人，只定方案、做验收；读代码、跑命令、写初稿这些体力活，派给更便宜甚至免费的模型。<br>
这套东西不是 demo：我每天用它交付需求，已经跑了约 300 个真实需求。
</p>

<p align="center">
<a href="https://github.com/Jerryx333/aiw"><img src="https://img.shields.io/badge/aiw-多模型分工-111?style=for-the-badge" alt="aiw"></a>
<a href="https://github.com/Jerryx333/agent-use"><img src="https://img.shields.io/badge/agent--use-统一调度-111?style=for-the-badge" alt="agent-use"></a>
<a href="https://marketplace.visualstudio.com/items?itemName=AT-9420.console-helper"><img src="https://img.shields.io/visual-studio-marketplace/i/AT-9420.console-helper?style=for-the-badge&label=console-helper%20installs" alt="console-helper installs"></a>
</p>

---

### 🧠 [aiw](https://github.com/Jerryx333/aiw)：给 Claude Code / Codex 配一支外包团队

主会话额度总不够、上下文一长就失忆？aiw 把主模型从"什么都自己干"变成"派单 + 验收"：

- **按角色派单**：改代码、只读评审、起草摘要三类活，各自按你排好的候选顺序找第一个可用的模型；某家限流或挂了，自动换下一家。
- **多家会诊**：同一个问题同时问几家模型，主会话先写下自己的判断，再逐条决定接受、驳回还是暂缓，不按多数票。
- **自动验收**：派出去的改动由 aiw 在本机跑完测试才交回，产出一律当待审稿。
- **花得更少**：作者日常约 300 个需求里，改 3 个以上文件的需求，派单后主会话的花费中位数约为自己改的 **1/4**；盲评对照里，两边的代码质量看不出差别。

### 🔌 [agent-use](https://github.com/Jerryx333/agent-use)：任何终端里的模型，一个接口全接管

- 所有模型都用同一种 JSON 请求调用，换模型只改配置，不改脚本。
- 按顺序自动换下一家，你主动中断时整条停下，不会乱试。
- 每次调用的原文、回答、尝试记录和校验哈希都留档；结果默认 `accepted: false`，核对过才算数。
- 配套：[agent-use-adapters](https://github.com/Jerryx333/agent-use-adapters)（Codex / Claude Code / OpenCode 现成适配器）、[aiw-board](https://github.com/Jerryx333/aiw-board)（派单看板 + Claude Code 状态栏）。

### 🤖 我自己的 AI 工作台

一台 24 小时开机的 Mac 上跑着我的私人 AI 助理：Discord 私聊下指令，它能读邮件、操控真实的 iPhone、跑定时任务；危险操作先发审批按钮，崩溃重启后从断点续跑。上面这些开源工具，大多是从它身上长出来的。

### 🔥 最近在忙

<!-- RECENT:START -->
- [aiw](https://github.com/Jerryx333/aiw) · 2026-10-15：让主模型只做规划和把关，体力活交给别的模型：派单、顶替、会诊、改进缓冲区
- [aiw-board](https://github.com/Jerryx333/aiw-board) · 2026-10-15：看清 aiw 派出去的活：谁在跑、跑了多久、成没成、哪个座位被熔断；终端看板，外加 Claude Code 状态栏和 Codex 底栏
- [agent-use](https://github.com/Jerryx333/agent-use) · 2026-10-14：Local, vendor-neutral dispatcher for text-generation agents: ordered fallback, per-route models, review-first results.
- [agent-use-adapters](https://github.com/Jerryx333/agent-use-adapters) · 2026-10-13：Ready-to-use Codex, Claude Code, and OpenCode adapters for agent-use
- [vscode-console-helper](https://github.com/Jerryx333/vscode-console-helper) · 2026-10-12：20k+ 开发者正在使用的，一键输出 console.log 的 vscode 插件

<sub>每天自动更新 · 2026-10-15</sub>
<!-- RECENT:END -->

---

### 🌍 开源贡献

除了自己的项目，也给 AI agent 工具链和前端生态的上游提代码，最近合并的有：

- **[egoist/mygo](https://github.com/egoist/mygo)** ★1.9k：macOS 上 CJK 字体没有斜体时的倾斜渲染
- **[leeguooooo/iphone-use](https://github.com/leeguooooo/iphone-use)**：7 个 PR，系统弹窗防误触、Xcode 26 签名、Codex 客户端截图
- **[leeguooooo/chrome-use](https://github.com/leeguooooo/chrome-use)**：6 个 PR，扩展超时恢复、守护进程保活、`doctor` 健康诊断
- **[sorrycc/Tiller](https://github.com/sorrycc/Tiller)**：5 个 PR，Codex 自定义 provider、OAuth 弹窗、macOS 崩溃修复
- **[leeguooooo/image-use](https://github.com/leeguooooo/image-use)**、[sorrycc/Mayoi](https://github.com/sorrycc/Mayoi)、[openapi-ts-request](https://github.com/openapi-ui/openapi-ts-request)、[AntmJS/vantui](https://github.com/AntmJS/vantui)……

### 🛠 早年作品

前端出身（Vue / React / 小程序），留下最多人用的是 **[console-helper](https://github.com/Jerryx333/vscode-console-helper)**：一键输出 `console.log` 的 VS Code 插件，**2.6 万+ 安装**、满分评价。

---

<p align="center">
<b>常用</b>：Python · TypeScript · Node.js · Rust · Claude Code · Codex · MCP<br>
📮 atxiesz@gmail.com
</p>

<p align="center"><sub>I build the orchestration layer for AI coding agents: a strong model plans and reviews, cheaper models do the legwork. See <a href="https://github.com/Jerryx333/aiw">aiw</a> and <a href="https://github.com/Jerryx333/agent-use">agent-use</a>.</sub></p>
