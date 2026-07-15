# 微交互设计设计规范

> 本文是面向独立产品的可迁移规范，不复制目标品牌的 Logo、商标、专有图标、插画或文案。所有精确起始值均以 `adapted` 标注，不代表目标品牌的内部 token。

## 1. 文档状态

| 字段 | 内容 |
|---|---|
| 状态 | `draft` |
| 目标对象 | 跨风格的 Microinteraction 行为规范 |
| 平台与版本 | 行为层；Web、桌面与移动端；2026-07 公开规范快照 |
| 目标项目 | 用于 AI Coding 的跨平台风格实施包 |
| 采集日期 | 2026-07-14 |
| 主题、语言与地区 | 继承宿主主题；跨语言、跨输入模态；动效和透明度用户偏好 |
| 负责人 | Codex（证据整理）/ 项目团队（落地验证） |

状态为 `draft` 的原因：本轮以公开文档和设计研究为证据，没有指定目标应用、运行时页面、组件库或可测设计文件，因此不能把推荐值标成 `measured` 或把实现质量标成已验证。

## 2. 范围与限制

### 已覆盖

- 公开材料中的风格定位、原则和使用边界（E-001、E-002、E-003、E-004）。
- 面向独立项目的颜色、排版、间距、形状、层级、动效与语义 token 起始方案。
- 代表性组件：按钮反馈、Toggle / 收藏、输入校验、进度 / Toast / Undo。
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
| E-001 | [NN/g — Microinteractions in User Experience](https://www.nngroup.com/articles/microinteractions/) | 微交互聚焦单一目的，可表达系统状态、防错和品牌；反馈通常靠近触发点。 | UX 研究与设计建议 | Document | 读取公开页面并记录可复查结论 | 2026-07-14T10:19:53+08:00 | 不提供通用视觉 token。 |
| E-002 | [IBM Carbon — Motion](https://carbondesignsystem.com/elements/motion/overview/) | Carbon 区分 productive/expressive motion，并给出 70/110/150/240/400ms 时长和缓动参考。 | Carbon Design System Web motion | Document | 读取公开页面并记录可复查结论 | 2026-07-14T10:19:53+08:00 | 数值属于 Carbon；本包引用后适配，不宣称通用事实。 |
| E-003 | [Apple HIG — Motion](https://developer.apple.com/design/human-interface-guidelines/motion) | 动效应有目的、简短、精确、可取消，并尊重减少动态设置。 | Apple 平台设计指南 | Document | 读取公开页面并记录可复查结论 | 2026-07-14T10:19:53+08:00 | Apple 平台规则不能直接证明 Web 或 Android 的实现。 |
| E-004 | [NN/g — Animation for Attention and Comprehension](https://www.nngroup.com/articles/animation-usability/) | 运动会强烈吸引注意；动效需按目标、频率和位置谨慎使用。 | Web 动画可用性研究 | Document | 读取公开页面并记录可复查结论 | 2026-07-14T10:19:53+08:00 | 原则性材料，不提供组件代码。 |
| E-090 | [W3C — Web Content Accessibility Guidelines (WCAG) 2.2](https://www.w3.org/TR/WCAG22/) | WCAG 2.2 规定文本/非文本对比、可见焦点、reflow、目标尺寸、颜色之外的状态线索等可验收基线。 | W3C Recommendation；Web；通用主题与输入模态 | Document | 读取公开页面并记录可复查结论 | 2026-07-14T10:19:53+08:00 | 不替代 Android、HarmonyOS、iOS 或桌面平台的额外要求。 |
| E-091 | [W3C — Media Queries Level 5](https://www.w3.org/TR/mediaqueries-5/) | Web 可查询 prefers-reduced-motion、prefers-reduced-transparency、prefers-contrast、forced-colors 与 prefers-color-scheme 等用户偏好。 | W3C Working Draft；Web 用户偏好媒体特性 | Document | 读取公开页面并记录可复查结论 | 2026-07-14T10:19:53+08:00 | 浏览器支持度与原生平台 API 需要在目标技术栈中另行确认。 |

证据类型与置信度分开：上表只说明来源；正文每条规则另行标注 `observed`、`inferred` 或 `adapted` 与置信度。

## 4. 覆盖矩阵

| 页面或流程 | 组件 | 状态 | 主题 | 视口或输入模态 | 覆盖状态 | 证据 |
|---|---|---|---|---|---|---|
| 公开设计语言/研究 | 原则与基础层 | 文档声明 | 文档涉及范围 | 公开网页 | Covered | E-001、E-002、E-003、E-004 |
| 跨平台起始包 | 按钮反馈、Toggle / 收藏、输入校验、进度 / Toast / Undo | default / focus / disabled / loading / error 等适用状态 | 默认起始主题 | Web、键盘、指针、触控参考 | Partial | E-001、E-002、E-003、E-004, E-090, E-091 |
| 真实产品流程 | 目标项目组件 | 全部运行态 | 实际深浅/高对比主题 | 真实设备与视口 | Missing | 无 |

## 5. 设计定位

微交互不是独立视觉主题，而是跨风格的行为层：一个用户动作或系统状态变化触发一组窄范围规则与反馈。每条微交互都应记录目的、触发、前置条件、状态转换、反馈、终止、失败恢复、焦点、公告和 reduced-motion。

| 规则 | 可观察/可验收表现 | 来源类型 | 置信度 | 证据 |
|---|---|---|---|---|
| 单一目的 | 每条微交互只解决一个主要问题：状态、确认、进度、防错、引导或品牌。 | `observed` | High | E-001 |
| 邻近及时 | 反馈紧邻触发点并在输入后立即出现；异步状态持续可见。 | `observed` | High | E-001 |
| 可中断可恢复 | 动画不阻塞继续操作，失败有重试、撤销或回滚路径。 | `inferred` | High | E-003, E-090 |

### 适用场景

- 任何需要明确状态、异步反馈、防错、进度、撤销和品牌细节的数字产品。
- 在既有设计系统之上补齐按钮、开关、表单、拖放、加载和结果反馈。
- 希望建立统一 motion token 和 reduced-motion 策略的团队。

### 不宜直接套用

- 把微交互当作独立视觉主题并另造一套色盘、字体和布局。
- 用撒花、弹跳或长动画掩盖延迟、错误和缺失的恢复路径。
- 高风险操作只给短时 toast，不提供确认、撤销或持久结果。

## 6. 设计原则

| 原则 | 可执行规则 | 例外 | 来源与置信度 |
|---|---|---|---|
| 目的先于动效 | 先定义触发和状态转换，再选择视觉、声音或触觉反馈。 | 纯品牌表达只用于低频非关键时刻。 | `observed`, High, E-001, E-004 |
| 高频要快 | 高频 productive motion 使用短时长，不能为每次操作增加等待。 | 低频重要反馈可适度延长但不阻塞。 | `observed`, High, E-002, E-003 |
| 状态必须持久 | 动画结束后仍能知道当前状态、结果和下一步。 | 瞬时 pressed 可在松开后恢复，但动作结果需另行反馈。 | `observed`, High, E-001 |
| 多通道等价 | 颜色、运动、声音和 haptic 只能补充文本、图标或程序化状态。 | 纯装饰动效可不提供语义，但不能承载关键信息。 | `adapted`, High, E-090, E-091 |

## 7. 基础系统

以下精确值是独立项目起始值，统一为 `adapted / medium`。采用理由：以触发、规则、反馈、状态和恢复为核心；视觉值只是自包含起始方案，最终应映射到宿主设计系统。

### 7.1 色彩

| 角色 | 起始值 | 用途 | 主题与状态 | Token | 来源与理由 |
|---|---|---|---|---|---|
| 画布 | `#F8FAFC` | 页面最底层 | 默认 | `semantic.color.background` | `adapted`, E-001, E-002, E-003, E-090, E-091；落地前按真实前景/背景复测对比度 |
| 表面 | `#FFFFFF` | 卡片、面板、输入背景 | 默认 | `semantic.color.surface` | `adapted`, E-001, E-002, E-003, E-090, E-091；落地前按真实前景/背景复测对比度 |
| 次级表面 | `#EEF2F6` | 弱分区与选中底 | 默认 | `semantic.color.surfaceAlt` | `adapted`, E-001, E-002, E-003, E-090, E-091；落地前按真实前景/背景复测对比度 |
| 主要文本 | `#17202A` | 标题与正文 | 默认 | `semantic.color.textPrimary` | `adapted`, E-001, E-002, E-003, E-090, E-091；落地前按真实前景/背景复测对比度 |
| 次级文本 | `#4B5563` | 说明与元数据 | 默认 | `semantic.color.textSecondary` | `adapted`, E-001, E-002, E-003, E-090, E-091；落地前按真实前景/背景复测对比度 |
| 必要边界 | `#64748B` | 组件识别与分组 | 默认 | `semantic.color.border` | `adapted`, E-001, E-002, E-003, E-090, E-091；落地前按真实前景/背景复测对比度 |
| 主要操作 | `#1D4ED8` | CTA、激活状态 | 默认/selected | `semantic.color.action` | `adapted`, E-001, E-002, E-003, E-090, E-091；落地前按真实前景/背景复测对比度 |
| 操作上内容 | `#FFFFFF` | 主要操作上的文字与图标 | 默认 | `semantic.color.onAction` | `adapted`, E-001, E-002, E-003, E-090, E-091；落地前按真实前景/背景复测对比度 |
| 焦点 | `#0B57D0` | 键盘焦点轮廓 | focus-visible | `semantic.color.focus` | `adapted`, E-001, E-002, E-003, E-090, E-091；落地前按真实前景/背景复测对比度 |
| 成功 | `#137333` | 成功反馈 | success | `semantic.color.success` | `adapted`, E-001, E-002, E-003, E-090, E-091；落地前按真实前景/背景复测对比度 |
| 警告 | `#9A6700` | 警告反馈 | warning | `semantic.color.warning` | `adapted`, E-001, E-002, E-003, E-090, E-091；落地前按真实前景/背景复测对比度 |
| 危险 | `#B42318` | 错误与破坏性操作 | error/danger | `semantic.color.danger` | `adapted`, E-001, E-002, E-003, E-090, E-091；落地前按真实前景/背景复测对比度 |

规则：语义色必须通过 token 映射；成功、警告、错误和选中不得只靠颜色表达；品牌来源中的专有色只用于分析，不应被独立产品直接当作自身品牌资产。

### 7.2 字体与内容密度

| 角色 | 字体 | 字号 / 行高 | 字重 | 内容规则 | 来源与证据 |
|---|---|---|---|---|---|
| 辅助 | Inter / Noto Sans SC / system-ui / sans-serif | `14px` / `20px` | 400–500 | 标签、元数据和帮助文字；不可承载唯一关键信息 | `adapted`, E-001, E-002, E-003, E-090, E-091 |
| 正文 | Inter / Noto Sans SC / system-ui / sans-serif | `16px` / `24px` | 400 | 默认正文与常规控件 | `adapted`, E-001, E-002, E-003, E-090, E-091 |
| 模块标题 | Inter / Noto Sans SC / system-ui / sans-serif | `24px` / `32px` | 600 | 卡片或页面分区标题 | `adapted`, E-001, E-002, E-003, E-090, E-091 |
| 展示标题 | Inter / Noto Sans SC / system-ui / sans-serif | `40px` / `48px` | 600–700 | 低频关键标题，窄屏需流体缩放 | `adapted`, E-001, E-002, E-003, E-090, E-091 |

微交互继承宿主设计系统的排版；本包字体仅为自包含示例，真实项目应删除重复排版源并映射宿主 token。

### 7.3 布局、网格与间距

| 场景 | 行为规则 | 起始值或范围 | 来源类型 | 置信度 | 证据 |
|---|---|---|---|---|---|
| 反馈邻近 | 状态反馈靠近触发点，同时保持全局结果可找到。 | `组件内 4–8px；消息区按宿主间距` | `adapted` | Medium | E-001, E-002, E-003, E-090, E-091 |
| 稳定尺寸 | loading、success、error 不改变容器主尺寸。 | `标签宽度或最小尺寸由最长状态确定` | `adapted` | Medium | E-001, E-002, E-003, E-090, E-091 |
| 消息堆叠 | 多个 toast 排队或合并，避免覆盖主操作。 | `安全区内，最多数量按产品策略` | `adapted` | Medium | E-001, E-002, E-003, E-090, E-091 |
| 运动距离 | 高频反馈尽量不位移；浮层只做短距离。 | `建议 0–16px，非通用事实` | `adapted` | Medium | E-001, E-002, E-003, E-090, E-091 |

不得把建议断点写成已观察断点。先以内容溢出、最小列宽、任务优先级和输入模态确定行为边界，再为工程实现记录断点。

### 7.4 形状、边框、层级与阴影

| 角色 | 规则 | 起始值 | Token | 来源与证据 |
|---|---|---|---|---|
| 控件圆角 | 继承宿主控件形状，不因动效另造形状体系。 | `8px` | `semantic.shape.control` | `adapted`, E-001, E-002, E-003, E-090, E-091 |
| 容器圆角 | 反馈容器保持稳定尺寸，状态切换不应造成布局跳动。 | `12px` | `semantic.shape.container` | `adapted`, E-001, E-002, E-003, E-090, E-091 |
| 默认边界 | focus、error 和 selected 的边界可同时区分。 | `1px` | `primitive.stroke.thin` | `adapted`, E-001, E-002, E-003, E-090, E-091 |
| 静止表面 | 常态反馈不依赖阴影。 | `none` | `primitive.effect.shadowRest` | `adapted`, E-001, E-002, E-003, E-090, E-091 |
| 抬升表面 | toast/浮层可表达真实遮挡，但不能抢夺层级。 | `0 4px 12px rgb(0 0 0 / 12%)` | `primitive.effect.shadowRaised` | `adapted`, E-001, E-002, E-003, E-090, E-091 |

### 7.5 图标、图像与品牌资产

- 微交互不建立独立图标库；使用宿主设计系统的状态图标。
- 成功动画和插画不能替代真实结果、文本说明或后续操作。
- 声音与 haptic 需遵循平台权限、静音和用户偏好，并始终有视觉/文本等价反馈。

### 7.6 动效

| 场景 | 属性 | 起始时长与曲线 | 减弱动效行为 | 来源与证据 |
|---|---|---|---|---|
| 即时按压 | 颜色/形状/≤1px 位移 | `70ms / productive easing` | 取消位移，保留即时状态 | `adapted`, E-002, E-003, E-091 |
| 常规状态 | 透明度、图标或小范围展开 | `150ms / cubic-bezier(0.2,0,0.38,0.9)` | 即时切换或短淡化 | `adapted`, E-002, E-003, E-091 |
| 系统反馈 | toast/面板进入与退出 | `240ms / enter/exit easing` | 取消位移，保留显隐 | `adapted`, E-002, E-004, E-091 |
| 低频强调 | 有限表达型动效 | `≤400ms；不用于日常按钮` | 改为静态结果与可选淡化 | `adapted`, E-002, E-003, E-091 |

## 8. Token 架构

`design-tokens.json` 是本实施包的结构化单一事实源：

1. `primitive.*` 保存颜色、间距、圆角、排版、时长和效果原值。
2. `semantic.*` 按背景、表面、文本、操作、反馈、焦点和形状角色引用 primitive。
3. `component.*` 为按钮、输入框和卡片绑定 semantic 角色。
4. 主题切换只替换 semantic 映射；未知主题值不写入空 token。
5. 所有叶节点都有 `status`、`evidenceIds`、`confidence`、`scope` 和 `rationale`。

当前 JSON 是跨平台起始源；CSS、Tailwind、Compose、SwiftUI 等映射应在技术栈和版本确定后由该源单向生成。

## 9. 组件规范

### 按钮反馈

组件级 provenance：`status=adapted`；`confidence=medium`；`confidenceReason=来源支持风格或交互原则，结构和精确实现值是跨平台起始适配，尚无目标产品运行时证据。`；`evidenceIds=E-001,E-002,E-003,E-004,E-090,E-091`；`scope=Web 与移动端参考；浅色起始主题；键盘、指针、触控和辅助技术`；`method=公开规范归纳后进行独立项目适配`；`captured_at=2026-07-14T10:19:53+08:00`；`rationale=建立明确的触发—规则—反馈—结果链路。`。

| 项目 | 规范 | 来源与证据 |
|---|---|---|
| 用途与边界 | 把触发、处理中和结果反馈绑定到同一动作。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-090, E-091 |
| Anatomy | 按钮标签、可选图标、进度；结果消息位于触发点附近或稳定反馈区。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-090, E-091 |
| Variants 与 sizes | 同步动作 / 异步动作 / 危险动作；不同风险有不同恢复策略。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-090, E-091 |
| 适用状态 | default → pressed → loading → success/error；取消与重试按任务需要。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-090, E-091 |
| 内容与溢出 | 处理中保留动作上下文；结果说明完成了什么或如何修复。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-090, E-091 |
| 鼠标、键盘与触控 | 按下即时反馈；异步期间防重复提交；键盘/触控行为一致。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-090, E-091 |
| 响应式行为 | 反馈不被软键盘、安全区或底部导航遮挡。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-090, E-091 |
| 无障碍 | loading/结果可被辅助技术感知；不擅自移动焦点；错误具有恢复路径。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-090, E-091 |
| Tokens | primitive.motion.*；semantic.motion.state；semantic.color.success/danger/focus。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-090, E-091 |
| 实现注意事项 | 动画不能延迟真实操作，也不能用成功动画掩盖失败。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-090, E-091 |

### Toggle / 收藏

组件级 provenance：`status=adapted`；`confidence=medium`；`confidenceReason=来源支持风格或交互原则，结构和精确实现值是跨平台起始适配，尚无目标产品运行时证据。`；`evidenceIds=E-001,E-002,E-003,E-004,E-090,E-091`；`scope=Web 与移动端参考；浅色起始主题；键盘、指针、触控和辅助技术`；`method=公开规范归纳后进行独立项目适配`；`captured_at=2026-07-14T10:19:53+08:00`；`rationale=让可逆状态的结果即时、持久并可恢复。`。

| 项目 | 规范 | 来源与证据 |
|---|---|---|
| 用途与边界 | 即时表达二元状态或可逆偏好。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-090, E-091 |
| Anatomy | 可见标签或名称、状态图形、可选保存反馈。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-090, E-091 |
| Variants 与 sizes | 本地即时 / 远程保存；收藏、订阅等语义分别命名。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-090, E-091 |
| 适用状态 | off/on、pressed、focus-visible、saving、error、disabled。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-090, E-091 |
| 内容与溢出 | 可访问名称随动作语义更新，当前状态单独暴露。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-090, E-091 |
| 鼠标、键盘与触控 | Space/点击切换；远程失败回滚并说明；再次激活可撤销。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-090, E-091 |
| 响应式行为 | 状态反馈贴近控件，不因窄屏变成只有颜色的图标。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-090, E-091 |
| 无障碍 | checked/pressed 状态程序化可读；颜色、缩放、haptic 不作唯一线索。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-090, E-091 |
| Tokens | primitive.motion.fast/standard；semantic.color.action/focus/danger。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-090, E-091 |
| 实现注意事项 | 高频切换使用短 productive motion，不加入庆祝式延迟。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-090, E-091 |

### 输入校验

组件级 provenance：`status=adapted`；`confidence=medium`；`confidenceReason=来源支持风格或交互原则，结构和精确实现值是跨平台起始适配，尚无目标产品运行时证据。`；`evidenceIds=E-001,E-002,E-003,E-004,E-090,E-091`；`scope=Web 与移动端参考；浅色起始主题；键盘、指针、触控和辅助技术`；`method=公开规范归纳后进行独立项目适配`；`captured_at=2026-07-14T10:19:53+08:00`；`rationale=将防错、解释和修复作为同一微交互。`。

| 项目 | 规范 | 来源与证据 |
|---|---|---|
| 用途与边界 | 在合适时机解释字段状态并帮助修复。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-090, E-091 |
| Anatomy | 字段、规则提示、错误文本、状态图标；成功提示只在确有价值时显示。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-090, E-091 |
| Variants 与 sizes | 提交后 / blur 后 / 输入时增量校验；按错误成本选择。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-090, E-091 |
| 适用状态 | pristine、editing、validating、valid、invalid、server-error。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-090, E-091 |
| 内容与溢出 | 错误说明问题和修复方式，不显示内部代码。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-090, E-091 |
| 鼠标、键盘与触控 | 不在每个字符上无意义打断；提交失败将焦点或摘要引导到错误并可继续编辑。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-090, E-091 |
| 响应式行为 | 错误多行时容器自然增长，不覆盖后续控件。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-090, E-091 |
| 无障碍 | 标签、描述与错误关联；状态消息可感知；不只改变边框颜色。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-090, E-091 |
| Tokens | semantic.color.danger/success/focus；semantic.motion.state。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-090, E-091 |
| 实现注意事项 | 动画只帮助定位变化，不使错误闪烁或抖动。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-090, E-091 |

### 进度 / Toast / Undo

组件级 provenance：`status=adapted`；`confidence=medium`；`confidenceReason=来源支持风格或交互原则，结构和精确实现值是跨平台起始适配，尚无目标产品运行时证据。`；`evidenceIds=E-001,E-002,E-003,E-004,E-090,E-091`；`scope=Web 与移动端参考；浅色起始主题；键盘、指针、触控和辅助技术`；`method=公开规范归纳后进行独立项目适配`；`captured_at=2026-07-14T10:19:53+08:00`；`rationale=让系统状态及时、邻近、可访问且可恢复。`。

| 项目 | 规范 | 来源与证据 |
|---|---|---|
| 用途与边界 | 沟通等待、完成、失败和短时可逆操作。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-090, E-091 |
| Anatomy | 消息、状态图标、进度、可选操作；关闭按钮按重要性出现。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-090, E-091 |
| Variants 与 sizes | determinate / indeterminate；inline / toast / persistent banner；含 undo 或 retry。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-090, E-091 |
| 适用状态 | starting、in-progress、completed、failed、paused/cancelled（适用时）。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-090, E-091 |
| 内容与溢出 | 已知比例显示数值；未知等待不伪造进度；关键恢复不只放短时 toast。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-090, E-091 |
| 鼠标、键盘与触控 | toast 在 hover/focus 时暂停；操作可键盘触达；等待可取消时提供取消。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-090, E-091 |
| 响应式行为 | 避开安全区和固定导航；多个消息排队或合并，禁止遮挡主操作。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-090, E-091 |
| 无障碍 | 使用合适 status/alert 语义；避免重复播报；焦点不被低风险消息抢走。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-090, E-091 |
| Tokens | primitive.motion.standard/slow；semantic.color.success/warning/danger。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-090, E-091 |
| 实现注意事项 | 低风险 undo 显示时长由内容与平台确定；关键恢复提供持久入口。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-090, E-091 |

## 10. 页面与流程

| 页面或流程 | 信息层级 | 布局与操作区 | 状态与异常路径 | 响应式行为 | 证据 |
|---|---|---|---|---|---|
| 异步提交 | 触发点 → 处理中 → 结果 → 恢复/下一步 | 状态尽量留在原位置，结果与全局反馈一致 | 重复提交、超时、取消、失败和重试明确 | 移动端不被键盘/安全区遮挡 | E-001, E-003, adapted |
| 直接操控 | 对象 → 手势/键盘 → 连续反馈 → 提交/取消 | 反馈跟手但不滞后；值与位置同步 | 无效目标、撤销和中断有路径 | 触控与键盘提供等价操作 | E-001, E-004, E-090, adapted |

## 11. 响应式与输入模态

- 以内容和任务触发行为变化：导航拥挤时改型、列宽不足时重排、操作过密时按优先级分层；阈值由目标项目记录。
- 触控界面不依赖 hover；精细指针的 hover 只加强默认可见线索。
- 交互目标起始值采用 44px；Web 合规仍须逐项核对 WCAG 2.2 的 24×24 CSS px 基线及例外。
- 200% 文本缩放与约 320 CSS px reflow 时，不丢失标签、错误、操作、当前状态与恢复路径。
- 使用逻辑方向属性；RTL 只镜像具有方向语义的布局和图标。
- 反馈靠近触发点，但在移动端必须避开软键盘、刘海、安全区和底部导航。
- 桌面 hover 仅补充，触控使用 pressed、选中、文字或适用 haptic。

## 12. 主题、国际化与极端内容

- 浅色、深色和高对比主题分别映射 semantic token；不得直接反相颜色、阴影、图片或材质。
- 响应 prefers-color-scheme、prefers-contrast、forced-colors、prefers-reduced-motion；透明材质还应处理 prefers-reduced-transparency。
- 使用真实 CJK、拉丁长词、阿拉伯语 RTL、日期、数字、货币和 30%–50% 文案膨胀测试。
- 按钮与标签允许换行或自适应宽度，不通过缩小字号或无提示省略关键动作解决溢出。
- 行为 token 可跨主题共用；颜色通过宿主 semantic mapping 切换。
- reduced-motion 下取消位移、缩放、视差和弹跳，而不是只把时长缩短。

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
| 使用独立项目色盘，不直接复制品牌或案例颜色 | E-001, E-002, E-003, E-090, E-091 | 保留风格规律，同时避免品牌混淆并满足具体内容对比度。 | 全部颜色与主题 | `adapted` |
| 采用 primitive → semantic → component 三层 token | E-001, E-002, E-003, E-090, E-091, E-090 | 支持主题、状态和平台映射，避免组件硬编码。 | design-tokens.json 与全部组件 | `adapted` |
| 动效时长参考 Carbon 后跨系统适配 | E-002, E-003, E-004 | 使用成熟节奏建立起始 token，同时明确不是通用或品牌实测值。 | motion duration 与 easing | `adapted` |
| 颜色和排版继承宿主系统 | E-001 | 微交互是行为层，不应与主设计系统争夺单一事实源。 | 最终项目 token 映射 | `adapted` |

## 15. 冲突、未知项与后续材料

| 项目 | 当前证据或冲突 | 影响 | 所需最少材料 | 当前处理 |
|---|---|---|---|---|
| 目标项目与用户任务 | 未提供真实产品和关键流程 | 无法判断密度、组件数量和页面模板 | 产品范围、关键流程、用户与平台 | Draft |
| 真实 token 与组件状态 | 没有代码、设计文件或运行页面 | 推荐值无法视为实测 | 组件库版本、主题文件、代表性页面 | Adapted |
| 对比度与输入模态 | 只有规范目标，没有渲染结果 | 不能标记无障碍通过 | 各主题状态截图、键盘/读屏/触控测试 | Not tested |
| 完整交互清单 | 未提供关键流程和系统延迟 | 无法判断每条微交互的状态与时长 | 流程图、异步耗时、失败模式和风险等级 | Draft |
| 声音/haptic API | 未指定平台和权限 | 不能生成确定反馈 | 目标平台 API、静音/触觉偏好策略 | Omit |

### 反模式

- 每次操作都撒花、弹跳或播放声音。
- 动画播放完才能继续，或反馈明显晚于输入。
- loading 与 disabled 混为一态，无取消或失败恢复。
- 错误只放短时 toast，关键恢复入口随消息消失。
- Reduce Motion 只把时长变短，仍保留大幅位移和缩放。

## 16. 实现与验收说明

- 开发只消费 `design-tokens.json`，不要在组件中另写同义颜色、尺寸或时长。
- 实现前先把目标产品的页面、组件、状态、主题和输入模态填入覆盖矩阵。
- 实现后执行 `design-review-checklist.md`；没有证据的项目保持 `Not tested`。
- Web 至少验证 320 CSS px reflow、200% 文本缩放、键盘全流程、读屏状态公告和 WCAG 2.2 AA 对比度。
- 视觉回归应覆盖默认、focus-visible、disabled、loading、empty、error、长文本、深色或高对比等适用状态。
- 若目标平台提供原生组件和主题能力，优先遵循对应平台规范；本包只定义风格层，不替代平台交互契约。
