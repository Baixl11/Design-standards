# 极简主义设计规范

> 本文是面向独立产品的可迁移规范，不复制目标品牌的 Logo、商标、专有图标、插画或文案。所有精确起始值均以 `adapted` 标注，不代表目标品牌的内部 token。

## 1. 文档状态

| 字段 | 内容 |
|---|---|
| 状态 | `draft` |
| 目标对象 | 任务导向的极简界面 |
| 平台与版本 | 抽象风格；Web 与移动端；2026-07 公开研究快照 |
| 目标项目 | 用于 AI Coding 的跨平台风格实施包 |
| 采集日期 | 2026-07-14 |
| 主题、语言与地区 | 浅色起始方案；深色/高对比为待映射主题；简体中文与多语言参考 |
| 负责人 | Codex（证据整理）/ 项目团队（落地验证） |

状态为 `draft` 的原因：本轮以公开文档和设计研究为证据，没有指定目标应用、运行时页面、组件库或可测设计文件，因此不能把推荐值标成 `measured` 或把实现质量标成已验证。

## 2. 范围与限制

### 已覆盖

- 公开材料中的风格定位、原则和使用边界（E-001、E-002）。
- 面向独立项目的颜色、排版、间距、形状、层级、动效与语义 token 起始方案。
- 代表性组件：按钮 / Action、输入框 / Field、卡片 / Surface、导航 / Selection。
- Web WCAG 2.2 AA、用户偏好、键盘/触控/辅助技术和国际化的适配要求。

### 未覆盖

- 目标产品、用户任务、技术栈、组件库、真实页面、运行时样式和设计文件。
- 品牌或平台未公开的内部 token、完整组件状态、动效实现与版本差异。
- 真实深浅主题、高对比模式、断点、设备安全区、性能与视觉回归结果。

### 使用限制

- 只学习可迁移规律，不复制 Logo、商标、专有字体字形、图标、插画、产品图或品牌文案。
- 来源为公开文档和研究，不是目标应用的 DOM、代码、设计节点或像素测量。
- 精确起始值全部标为 adapted；落地后必须按具体前景/背景、状态和平台复测。

## 3. 证据索引

| ID | 来源 | 支持的单一结论 | 上下文 | 证据类型 | 采集方法 | 采集时间 | 限制 |
|---|---|---|---|---|---|---|---|
| E-001 | [NN/g — The Characteristics of Minimalism in Web Design](https://www.nngroup.com/articles/characteristics-minimalism/) | 极简样本常见有限色盘、较少元素、负空间和强调排版；核心是删除不支持任务的内容。 | 112 个历史网站样本；Web | Document | 读取公开页面并记录可复查结论 | 2026-07-14T10:19:53+08:00 | 2015 年样本不能当作 2026 年市场占比或官方标准。 |
| E-002 | [NN/g — Why Zen Mode Isn't the Answer to Everything](https://www.nngroup.com/articles/zen-mode/) | 隐藏界面 chrome 可能增加交互成本、认知负荷和注意切换；少不总是更好。 | Web/应用沉浸模式研究 | Document | 读取公开页面并记录可复查结论 | 2026-07-14T10:19:53+08:00 | 聚焦于 zen mode 风险，不覆盖所有极简场景。 |
| E-090 | [W3C — Web Content Accessibility Guidelines (WCAG) 2.2](https://www.w3.org/TR/WCAG22/) | WCAG 2.2 规定文本/非文本对比、可见焦点、reflow、目标尺寸、颜色之外的状态线索等可验收基线。 | W3C Recommendation；Web；通用主题与输入模态 | Document | 读取公开页面并记录可复查结论 | 2026-07-14T10:19:53+08:00 | 不替代 Android、HarmonyOS、iOS 或桌面平台的额外要求。 |
| E-091 | [W3C — Media Queries Level 5](https://www.w3.org/TR/mediaqueries-5/) | Web 可查询 prefers-reduced-motion、prefers-reduced-transparency、prefers-contrast、forced-colors 与 prefers-color-scheme 等用户偏好。 | W3C Working Draft；Web 用户偏好媒体特性 | Document | 读取公开页面并记录可复查结论 | 2026-07-14T10:19:53+08:00 | 浏览器支持度与原生平台 API 需要在目标技术栈中另行确认。 |

证据类型与置信度分开：上表只说明来源；正文每条规则另行标注 `observed`、`inferred` 或 `adapted` 与置信度。

## 4. 覆盖矩阵

| 页面或流程 | 组件 | 状态 | 主题 | 视口或输入模态 | 覆盖状态 | 证据 |
|---|---|---|---|---|---|---|
| 公开设计语言/研究 | 原则与基础层 | 文档声明 | 文档涉及范围 | 公开网页 | Covered | E-001、E-002 |
| 跨平台起始包 | 按钮 / Action、输入框 / Field、卡片 / Surface、导航 / Selection | default / focus / disabled / loading / error 等适用状态 | 默认起始主题 | Web、键盘、指针、触控参考 | Partial | E-001、E-002, E-090, E-091 |
| 真实产品流程 | 目标项目组件 | 全部运行态 | 实际深浅/高对比主题 | 真实设备与视口 | Missing | 无 |

## 5. 设计定位

极简主义是内容、功能与布局策略：删除不支持核心任务的内容，而不只是白底、大字、少颜色。负空间、有限色盘和排版应让任务更清楚；导航、标签、状态、帮助与错误恢复不能为追求“干净”被删除。

| 规则 | 可观察/可验收表现 | 来源类型 | 置信度 | 证据 |
|---|---|---|---|---|
| 任务做减法 | 保留支持理解、导航、操作、反馈和恢复的元素，删除重复与无关内容。 | `observed` | High | E-001, E-002 |
| 排版承担层级 | 用有限字号、字重、行长和间距组织内容，不依赖装饰性容器。 | `observed` | High | E-001 |
| 负空间有职责 | 空白用于分组、聚焦和阅读节奏，不把关键任务推离可见区域。 | `inferred` | High | E-001, E-002 |

### 适用场景

- 内容、品牌、作品集、专注工具、低到中等复杂度 SaaS。
- 目标任务清楚、内容层级稳定且能通过排版直接表达的产品。
- 希望减少视觉噪声但仍愿意保留完整可用性线索的团队。

### 不宜直接套用

- 未经任务审计就删除导航、标签、帮助或状态的界面。
- 高密度监控、交易、医疗或审批场景中以空白取代必要信息。
- 只剩大字和图片，却缺少清晰下一步与错误恢复的营销页。

## 6. 设计原则

| 原则 | 可执行规则 | 例外 | 来源与置信度 |
|---|---|---|---|
| 每个元素有职责 | 元素必须支持任务、理解、导航、反馈或品牌识别。 | 合规信息和帮助即使低频也不能随意删除。 | `observed`, High, E-001 |
| 可见优于隐藏 | 高频导航、核心筛选和主操作直接可见。 | 低频次级功能可渐进披露，但入口清楚。 | `observed`, High, E-002 |
| 有限色盘 | 一个强调色优先服务主操作，语义状态色保持明确。 | 数据可视化可使用更多色，但需系统化并配非颜色线索。 | `inferred`, Medium, E-001 |
| 负空间表达关系 | 组内更近、组间更远；大空白必须强化章节或任务优先级。 | 窄屏减少绝对留白，保留相对层级。 | `inferred`, High, E-001 |

## 7. 基础系统

以下精确值是独立项目起始值，统一为 `adapted / medium`。采用理由：以核心任务、内容优先级和可发现性为边界做减法；精确值只提供克制、可读且可主题化的起始方案。

### 7.1 色彩

| 角色 | 起始值 | 用途 | 主题与状态 | Token | 来源与理由 |
|---|---|---|---|---|---|
| 画布 | `#FAFAF9` | 页面最底层 | 默认 | `semantic.color.background` | `adapted`, E-001, E-002, E-090；落地前按真实前景/背景复测对比度 |
| 表面 | `#FFFFFF` | 卡片、面板、输入背景 | 默认 | `semantic.color.surface` | `adapted`, E-001, E-002, E-090；落地前按真实前景/背景复测对比度 |
| 次级表面 | `#F1F1EF` | 弱分区与选中底 | 默认 | `semantic.color.surfaceAlt` | `adapted`, E-001, E-002, E-090；落地前按真实前景/背景复测对比度 |
| 主要文本 | `#171717` | 标题与正文 | 默认 | `semantic.color.textPrimary` | `adapted`, E-001, E-002, E-090；落地前按真实前景/背景复测对比度 |
| 次级文本 | `#525252` | 说明与元数据 | 默认 | `semantic.color.textSecondary` | `adapted`, E-001, E-002, E-090；落地前按真实前景/背景复测对比度 |
| 必要边界 | `#737373` | 组件识别与分组 | 默认 | `semantic.color.border` | `adapted`, E-001, E-002, E-090；落地前按真实前景/背景复测对比度 |
| 主要操作 | `#005FCC` | CTA、激活状态 | 默认/selected | `semantic.color.action` | `adapted`, E-001, E-002, E-090；落地前按真实前景/背景复测对比度 |
| 操作上内容 | `#FFFFFF` | 主要操作上的文字与图标 | 默认 | `semantic.color.onAction` | `adapted`, E-001, E-002, E-090；落地前按真实前景/背景复测对比度 |
| 焦点 | `#005FCC` | 键盘焦点轮廓 | focus-visible | `semantic.color.focus` | `adapted`, E-001, E-002, E-090；落地前按真实前景/背景复测对比度 |
| 成功 | `#176B3A` | 成功反馈 | success | `semantic.color.success` | `adapted`, E-001, E-002, E-090；落地前按真实前景/背景复测对比度 |
| 警告 | `#8B5E00` | 警告反馈 | warning | `semantic.color.warning` | `adapted`, E-001, E-002, E-090；落地前按真实前景/背景复测对比度 |
| 危险 | `#A12622` | 错误与破坏性操作 | error/danger | `semantic.color.danger` | `adapted`, E-001, E-002, E-090；落地前按真实前景/背景复测对比度 |

规则：语义色必须通过 token 映射；成功、警告、错误和选中不得只靠颜色表达；品牌来源中的专有色只用于分析，不应被独立产品直接当作自身品牌资产。

### 7.2 字体与内容密度

| 角色 | 字体 | 字号 / 行高 | 字重 | 内容规则 | 来源与证据 |
|---|---|---|---|---|---|
| 辅助 | Inter / Noto Sans SC / system-ui / sans-serif | `14px` / `20px` | 400–500 | 标签、元数据和帮助文字；不可承载唯一关键信息 | `adapted`, E-001, E-002, E-090 |
| 正文 | Inter / Noto Sans SC / system-ui / sans-serif | `16px` / `24px` | 400 | 默认正文与常规控件 | `adapted`, E-001, E-002, E-090 |
| 模块标题 | Inter / Noto Sans SC / system-ui / sans-serif | `24px` / `32px` | 600 | 卡片或页面分区标题 | `adapted`, E-001, E-002, E-090 |
| 展示标题 | Inter / Noto Sans SC / system-ui / sans-serif | `48px` / `56px` | 600–700 | 低频关键标题，窄屏需流体缩放 | `adapted`, E-001, E-002, E-090 |

排版承担主要层级但保持少量稳定角色；长文建议限制行长；大标题在窄屏用 clamp 或容器查询缩放。

### 7.3 布局、网格与间距

| 场景 | 行为规则 | 起始值或范围 | 来源类型 | 置信度 | 证据 |
|---|---|---|---|---|---|
| 间距节奏 | 少量稳定间距形成组内/组间关系。 | `4 / 8 / 16 / 24 / 32 / 48 / 64 / 96px` | `adapted` | Medium | E-001, E-002, E-090 |
| 长文行长 | 限制阅读宽度，不把正文铺满大屏。 | `建议 max-width: 68ch` | `adapted` | Medium | E-001, E-002, E-090 |
| 页面留白 | 大留白只用于章节和主任务聚焦，窄屏流体收缩。 | `clamp(24px, 6vw, 96px) 起始参考` | `adapted` | Medium | E-001, E-002, E-090 |
| 布局 | 优先单主栏；多列必须改善比较或效率。 | `列数按内容最小宽度决定` | `adapted` | Medium | E-001, E-002, E-090 |

不得把建议断点写成已观察断点。先以内容溢出、最小列宽、任务优先级和输入模态确定行为边界，再为工程实现记录断点。

### 7.4 形状、边框、层级与阴影

| 角色 | 规则 | 起始值 | Token | 来源与证据 |
|---|---|---|---|---|
| 控件圆角 | 少量圆角即可建立可操作性，不以胶囊堆叠制造装饰。 | `6px` | `semantic.shape.control` | `adapted`, E-001, E-002, E-090 |
| 容器圆角 | 内容不必全部装入卡片；仅对真实分组和浮层使用容器。 | `8px` | `semantic.shape.container` | `adapted`, E-001, E-002, E-090 |
| 默认边界 | 必要交互边界保持清楚；装饰分割优先用间距。 | `1px` | `primitive.stroke.thin` | `adapted`, E-001, E-002, E-090 |
| 静止表面 | 常态内容不使用阴影。 | `none` | `primitive.effect.shadowRest` | `adapted`, E-001, E-002, E-090 |
| 抬升表面 | 只给弹层和真实遮挡关系。 | `0 4px 12px rgb(0 0 0 / 10%)` | `primitive.effect.shadowRaised` | `adapted`, E-001, E-002, E-090 |

### 7.5 图标、图像与品牌资产

- 图片和插画必须承担说明、证据或品牌情绪，不用大图填补空白。
- 图标只用于熟悉动作；陌生或高风险动作使用可见文字。
- 不复制极简品牌的专有摄影、版式或字体资产。

### 7.6 动效

| 场景 | 属性 | 起始时长与曲线 | 减弱动效行为 | 来源与证据 |
|---|---|---|---|---|
| 状态反馈 | 颜色/边界/轻透明度 | `110–150ms / cubic-bezier(0.2,0,0,1)` | 即时切换并保留状态 | `adapted`, E-002, E-091 |
| 渐进披露 | 高度与透明度 | `220ms / 同曲线` | 即时展开或短淡化 | `adapted`, E-002, E-091 |
| 页面切换 | 淡化或平台原生过渡 | `≤220ms` | 禁用非必要位移 | `adapted`, E-091 |

## 8. Token 架构

`design-tokens.json` 是本实施包的结构化单一事实源：

1. `primitive.*` 保存颜色、间距、圆角、排版、时长和效果原值。
2. `semantic.*` 按背景、表面、文本、操作、反馈、焦点和形状角色引用 primitive。
3. `component.*` 为按钮、输入框和卡片绑定 semantic 角色。
4. 主题切换只替换 semantic 映射；未知主题值不写入空 token。
5. 所有叶节点都有 `status`、`evidenceIds`、`confidence`、`scope` 和 `rationale`。

当前 JSON 是跨平台起始源；CSS、Tailwind、Compose、SwiftUI 等映射应在技术栈和版本确定后由该源单向生成。

## 9. 组件规范

### 按钮 / Action

组件级 provenance：`status=adapted`；`confidence=medium`；`confidenceReason=来源支持风格或交互原则，结构和精确实现值是跨平台起始适配，尚无目标产品运行时证据。`；`evidenceIds=E-001,E-002,E-090,E-091`；`scope=Web 与移动端参考；浅色起始主题；键盘、指针、触控和辅助技术`；`method=公开规范归纳后进行独立项目适配`；`captured_at=2026-07-14T10:19:53+08:00`；`rationale=为形成可实现、可键盘操作且状态完整的跨平台按钮契约。`。

| 项目 | 规范 | 来源与证据 |
|---|---|---|
| 用途与边界 | 触发即时命令或提交；不把导航链接伪装成按钮。 | `adapted`, Medium, E-001, E-002, E-090, E-091 |
| Anatomy | 容器、可见标签；图标和进度指示为条件部位。 | `adapted`, Medium, E-001, E-002, E-090, E-091 |
| Variants 与 sizes | primary / secondary / tertiary / danger；尺寸只在目标密度确定后映射，最小高度引用 token。 | `adapted`, Medium, E-001, E-002, E-090, E-091 |
| 适用状态 | default、hover（仅精细指针）、focus-visible、active、disabled、loading；loading 与 disabled 分开。 | `adapted`, Medium, E-001, E-002, E-090, E-091 |
| 内容与溢出 | 优先使用动词短语；loading 时保留宽度和上下文，禁止只显示无标签图标。 | `adapted`, Medium, E-001, E-002, E-090, E-091 |
| 鼠标、键盘与触控 | Enter/Space 激活；指针与触控按下即反馈；异步时阻止重复提交但保留取消或恢复路径。 | `adapted`, Medium, E-001, E-002, E-090, E-091 |
| 响应式行为 | 窄容器可全宽，但不能截断关键动词；多个操作按优先级重排。 | `adapted`, Medium, E-001, E-002, E-090, E-091 |
| 无障碍 | 具备可访问名称；焦点可见且不被遮挡；危险动作有确认或撤销；状态变化可感知。 | `adapted`, Medium, E-001, E-002, E-090, E-091 |
| Tokens | component.button.primary.*；semantic.color.action/onAction/focus；primitive.size.targetMin。 | `adapted`, Medium, E-001, E-002, E-090, E-091 |
| 实现注意事项 | 优先可见、克制和少量层级，不以隐藏功能换取空白；每个视觉区域通常只设一个 primary；secondary/tertiary 仍需可发现 | `adapted`, Medium, E-001, E-002, E-090, E-091 |

### 输入框 / Field

组件级 provenance：`status=adapted`；`confidence=medium`；`confidenceReason=来源支持风格或交互原则，结构和精确实现值是跨平台起始适配，尚无目标产品运行时证据。`；`evidenceIds=E-001,E-002,E-090,E-091`；`scope=Web 与移动端参考；浅色起始主题；键盘、指针、触控和辅助技术`；`method=公开规范归纳后进行独立项目适配`；`captured_at=2026-07-14T10:19:53+08:00`；`rationale=风格不能以隐藏标签、低对比边界或仅颜色错误为代价。`。

| 项目 | 规范 | 来源与证据 |
|---|---|---|
| 用途与边界 | 采集短文本或结构化值；标签、说明、错误和输入本体职责分离。 | `adapted`, Medium, E-001, E-002, E-090, E-091 |
| Anatomy | 永久标签、输入容器、值、可选前后缀、帮助/错误文本。 | `adapted`, Medium, E-001, E-002, E-090, E-091 |
| Variants 与 sizes | text / password / search / number 等按真实需求启用；不为风格补造类型。 | `adapted`, Medium, E-001, E-002, E-090, E-091 |
| 适用状态 | default、hover（适用时）、focus-visible、filled、disabled、read-only、error、success（确有必要时）。 | `adapted`, Medium, E-001, E-002, E-090, E-091 |
| 内容与溢出 | 标签不依赖 placeholder；长错误可换行；格式要求在输入前可获得。 | `adapted`, Medium, E-001, E-002, E-090, E-091 |
| 鼠标、键盘与触控 | Tab 聚焦；平台标准文本编辑；清除和显隐密码按钮有独立名称；校验时机可预测。 | `adapted`, Medium, E-001, E-002, E-090, E-091 |
| 响应式行为 | 随容器伸缩但保留标签和错误；软键盘出现时字段与提交操作不被遮挡。 | `adapted`, Medium, E-001, E-002, E-090, E-091 |
| 无障碍 | 程序化标签、描述和错误关联；错误不只变色；焦点环与错误边界可同时辨认。 | `adapted`, Medium, E-001, E-002, E-090, E-091 |
| Tokens | component.input.*；semantic.color.textPrimary/border/focus/danger。 | `adapted`, Medium, E-001, E-002, E-090, E-091 |
| 实现注意事项 | 优先可见、克制和少量层级，不以隐藏功能换取空白；不得用表面效果削弱文本与边界。 | `adapted`, Medium, E-001, E-002, E-090, E-091 |

### 卡片 / Surface

组件级 provenance：`status=adapted`；`confidence=medium`；`confidenceReason=来源支持风格或交互原则，结构和精确实现值是跨平台起始适配，尚无目标产品运行时证据。`；`evidenceIds=E-001,E-002,E-090,E-091`；`scope=Web 与移动端参考；浅色起始主题；键盘、指针、触控和辅助技术`；`method=公开规范归纳后进行独立项目适配`；`captured_at=2026-07-14T10:19:53+08:00`；`rationale=将材质或平面风格限制在不破坏信息结构和可操作性的范围内。`。

| 项目 | 规范 | 来源与证据 |
|---|---|---|
| 用途与边界 | 只在信息确有分组、比较或整体操作关系时建立容器。 | `adapted`, Medium, E-001, E-002, E-090, E-091 |
| Anatomy | 容器、标题、主体；媒体、元数据、操作区为可选部位。 | `adapted`, Medium, E-001, E-002, E-090, E-091 |
| Variants 与 sizes | static / interactive / selected；interactive 必须在默认状态即可发现。 | `adapted`, Medium, E-001, E-002, E-090, E-091 |
| 适用状态 | static 无交互状态；interactive 覆盖 default、hover（适用时）、focus-visible、active、selected、disabled（适用时）。 | `adapted`, Medium, E-001, E-002, E-090, E-091 |
| 内容与溢出 | 卡片标题保持可扫描；整卡点击时内部不得嵌套冲突交互；长内容按内容优先级处理。 | `adapted`, Medium, E-001, E-002, E-090, E-091 |
| 鼠标、键盘与触控 | 整卡可点击时提供单一语义目标；内部多操作时改为容器加显式按钮。 | `adapted`, Medium, E-001, E-002, E-090, E-091 |
| 响应式行为 | 从多列到单列按最小可读宽度重排；不可等比缩小文字或触控目标。 | `adapted`, Medium, E-001, E-002, E-090, E-091 |
| 无障碍 | 语义结构与视觉结构一致；选中不只靠颜色/阴影；必要边界对比可测。 | `adapted`, Medium, E-001, E-002, E-090, E-091 |
| Tokens | component.card.*；semantic.color.surface/textPrimary/border；semantic.shape.container。 | `adapted`, Medium, E-001, E-002, E-090, E-091 |
| 实现注意事项 | 优先可见、克制和少量层级，不以隐藏功能换取空白；仅在分组或整体操作确有必要时使用卡片，普通内容可直接在页面排版 | `adapted`, Medium, E-001, E-002, E-090, E-091 |

### 导航 / Selection

组件级 provenance：`status=adapted`；`confidence=medium`；`confidenceReason=来源支持风格或交互原则，结构和精确实现值是跨平台起始适配，尚无目标产品运行时证据。`；`evidenceIds=E-001,E-002,E-090,E-091`；`scope=Web 与移动端参考；浅色起始主题；键盘、指针、触控和辅助技术`；`method=公开规范归纳后进行独立项目适配`；`captured_at=2026-07-14T10:19:53+08:00`；`rationale=保证风格化导航仍有稳定位置、可发现状态和完整键盘模型。`。

| 项目 | 规范 | 来源与证据 |
|---|---|---|
| 用途与边界 | 表达当前位置、同级切换或层级返回；不混用导航与提交行为。 | `adapted`, Medium, E-001, E-002, E-090, E-091 |
| Anatomy | 容器、项目、标签、选中指示；图标和徽标为条件部位。 | `adapted`, Medium, E-001, E-002, E-090, E-091 |
| Variants 与 sizes | 顶部、侧边、底部或标签页按平台与信息架构选择，不能只因风格同时存在。 | `adapted`, Medium, E-001, E-002, E-090, E-091 |
| 适用状态 | default、hover（适用时）、focus-visible、active、selected、disabled（适用时）。 | `adapted`, Medium, E-001, E-002, E-090, E-091 |
| 内容与溢出 | 标签短而独立可理解；方向性图标按语义和 RTL 处理；当前项始终可见。 | `adapted`, Medium, E-001, E-002, E-090, E-091 |
| 鼠标、键盘与触控 | Tab 到控件；组件模式适用时用方向键切换；触控目标满足项目最小值。 | `adapted`, Medium, E-001, E-002, E-090, E-091 |
| 响应式行为 | 空间不足时按优先级折叠或改型，不隐藏当前状态与返回路径。 | `adapted`, Medium, E-001, E-002, E-090, E-091 |
| 无障碍 | 正确使用 nav/tablist 等语义；当前页或选中态程序化可读；焦点顺序符合视觉顺序。 | `adapted`, Medium, E-001, E-002, E-090, E-091 |
| Tokens | semantic.color.textPrimary/action/focus/surfaceAlt；primitive.size.targetMin。 | `adapted`, Medium, E-001, E-002, E-090, E-091 |
| 实现注意事项 | 优先可见、克制和少量层级，不以隐藏功能换取空白；少量主要入口优先直接显示；折叠后仍保留当前页和返回路径 | `adapted`, Medium, E-001, E-002, E-090, E-091 |

## 10. 页面与流程

| 页面或流程 | 信息层级 | 布局与操作区 | 状态与异常路径 | 响应式行为 | 证据 |
|---|---|---|---|---|---|
| 内容/品牌页 | 价值主张 → 证据/内容 → 单一主操作 | 单主栏、强排版、有限色盘；空白表达章节 | 媒体加载失败与长内容有降级 | 大标题/边距流体缩放，内容不被隐藏 | E-001, adapted |
| 专注工作页 | 任务上下文 → 当前工作 → 必要工具/反馈 | 高频工具可见，低频项渐进披露 | 保存、冲突、错误与撤销持久可见 | 窄屏改为分步或抽屉，但保留当前状态 | E-002, adapted |

## 11. 响应式与输入模态

- 以内容和任务触发行为变化：导航拥挤时改型、列宽不足时重排、操作过密时按优先级分层；阈值由目标项目记录。
- 触控界面不依赖 hover；精细指针的 hover 只加强默认可见线索。
- 交互目标起始值采用 44px；Web 合规仍须逐项核对 WCAG 2.2 的 24×24 CSS px 基线及例外。
- 200% 文本缩放与约 320 CSS px reflow 时，不丢失标签、错误、操作、当前状态与恢复路径。
- 使用逻辑方向属性；RTL 只镜像具有方向语义的布局和图标。
- 不要把桌面大空白原样搬到手机；缩小绝对留白但保持组间比例。
- 多列转单列时按任务顺序排列，不能隐藏关键内容解决拥挤。

## 12. 主题、国际化与极端内容

- 浅色、深色和高对比主题分别映射 semantic token；不得直接反相颜色、阴影、图片或材质。
- 响应 prefers-color-scheme、prefers-contrast、forced-colors、prefers-reduced-motion；透明材质还应处理 prefers-reduced-transparency。
- 使用真实 CJK、拉丁长词、阿拉伯语 RTL、日期、数字、货币和 30%–50% 文案膨胀测试。
- 按钮与标签允许换行或自适应宽度，不通过缩小字号或无提示省略关键动作解决溢出。
- 深色极简仍需足够对比；不能用超浅灰文字和几乎不可见边界制造柔和感。

## 13. 无障碍观察与合规发现

| ID | 检查项 | 状态 | 证据 | 严重度 | 建议 |
|---|---|---|---|---|---|
| A11Y-001 | 正常文本与大文本对比度 | Not tested | E-090 | High | 逐主题、逐状态测量；正常文本至少 4.5:1，大文本至少 3:1。 |
| A11Y-002 | 必要边界、图标和状态线索的非文本对比 | Not tested | E-090 | High | 识别组件或状态所需线索与相邻颜色至少 3:1，且不只靠颜色。 |
| A11Y-003 | 键盘、焦点顺序与焦点不被遮挡 | Not tested | E-090 | Critical | 用键盘完成全部适用流程，检查 focus-visible 与弹层焦点恢复。 |
| A11Y-004 | 减弱动效、减少透明度、高对比和强制颜色 | Not tested | E-091 | Medium | 为用户偏好提供不丢失状态信息的替代呈现。 |
| A11Y-005 | reflow、文本缩放、长内容与 RTL | Not tested | E-090 | High | 在 320 CSS px、200% 文本缩放和本地化样例下验证。 |

`Not tested` 表示尚无真实页面或组件实现，不能据文档推断为通过。

## 14. 项目适配决策

| 决策 | 原始证据 | 适配原因 | 影响范围 | 状态 |
|---|---|---|---|---|
| 使用独立项目色盘，不直接复制品牌或案例颜色 | E-001, E-002, E-090 | 保留风格规律，同时避免品牌混淆并满足具体内容对比度。 | 全部颜色与主题 | `adapted` |
| 采用 primitive → semantic → component 三层 token | E-001, E-002, E-090, E-090 | 支持主题、状态和平台映射，避免组件硬编码。 | design-tokens.json 与全部组件 | `adapted` |
| 将极简定义为任务审计后的减法，而非固定视觉配方 | E-001, E-002 | 避免为追求空白删除导航、说明、反馈和恢复。 | 内容、导航、组件与页面模板 | `adapted` |

## 15. 冲突、未知项与后续材料

| 项目 | 当前证据或冲突 | 影响 | 所需最少材料 | 当前处理 |
|---|---|---|---|---|
| 目标项目与用户任务 | 未提供真实产品和关键流程 | 无法判断密度、组件数量和页面模板 | 产品范围、关键流程、用户与平台 | Draft |
| 真实 token 与组件状态 | 没有代码、设计文件或运行页面 | 推荐值无法视为实测 | 组件库版本、主题文件、代表性页面 | Adapted |
| 对比度与输入模态 | 只有规范目标，没有渲染结果 | 不能标记无障碍通过 | 各主题状态截图、键盘/读屏/触控测试 | Not tested |
| 可删除内容 | 未提供核心任务和内容优先级 | 无法证明任何功能可移除 | 任务清单、内容模型与使用频率 | Draft |

### 反模式

- 隐藏全局导航、核心搜索或筛选，只为保持页面干净。
- 移除表单标签、帮助、错误和恢复入口。
- 正文使用低对比浅灰，焦点轮廓被删除。
- 巨量空白把主任务推到首屏之外。
- 只有大标题和图片，没有清晰信息结构与下一步。

## 16. 实现与验收说明

- 开发只消费 `design-tokens.json`，不要在组件中另写同义颜色、尺寸或时长。
- 实现前先把目标产品的页面、组件、状态、主题和输入模态填入覆盖矩阵。
- 实现后执行 `design-review-checklist.md`；没有证据的项目保持 `Not tested`。
- Web 至少验证 320 CSS px reflow、200% 文本缩放、键盘全流程、读屏状态公告和 WCAG 2.2 AA 对比度。
- 视觉回归应覆盖默认、focus-visible、disabled、loading、empty、error、长文本、深色或高对比等适用状态。
- 若目标平台提供原生组件和主题能力，优先遵循对应平台规范；本包只定义风格层，不替代平台交互契约。
