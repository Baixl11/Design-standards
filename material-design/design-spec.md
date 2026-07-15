# 材质设计设计规范

> 本文是面向独立产品的可迁移规范，不复制目标品牌的 Logo、商标、专有图标、插画或文案。所有精确起始值均以 `adapted` 标注，不代表目标品牌的内部 token。

## 1. 文档状态

| 字段 | 内容 |
|---|---|
| 状态 | `draft` |
| 目标对象 | Material Design 3，包含 Material 3 Expressive 方向与稳定性边界 |
| 平台与版本 | 设计语言：M3/M3 Expressive；Android 稳定实现基线：Compose Material 3 1.4.0；1.5.0-alpha23 为预览 |
| 目标项目 | 用于 AI Coding 的跨平台风格实施包 |
| 采集日期 | 2026-07-14 |
| 主题、语言与地区 | light/dark/dynamic/high-contrast；Android 优先，Web/其他平台需映射；全球多语言 |
| 负责人 | Codex（证据整理）/ 项目团队（落地验证） |

状态为 `draft` 的原因：本轮以公开文档和设计研究为证据，没有指定目标应用、运行时页面、组件库或可测设计文件，因此不能把推荐值标成 `measured` 或把实现质量标成已验证。

## 2. 范围与限制

### 已覆盖

- 公开材料中的风格定位、原则和使用边界（E-001、E-002、E-003、E-004、E-005）。
- 面向独立项目的颜色、排版、间距、形状、层级、动效与语义 token 起始方案。
- 代表性组件：Button / FAB、Text Field、Card / Chip、Adaptive Navigation。
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
| E-001 | [Android Developers — Material Design 3 in Compose](https://developer.android.com/develop/ui/compose/designsystems/material3) | M3/M3 Expressive 包含 color scheme、typography、shapes 和动态色，并给出 M3 15 级排版与自适应组件方向。 | Android 官方设计/实现总览 | Document | 读取公开页面并记录可复查结论 | 2026-07-14T10:19:53+08:00 | 总览不能证明每个组件的 padding、状态层或所有平台行为。 |
| E-002 | [Android Developers — Compose Material 3 release notes](https://developer.android.com/jetpack/androidx/releases/compose-material3) | 截至 2026-07-01 稳定版为 1.4.0，1.5.0-alpha23 为 alpha；Expressive API 的稳定性需逐项核查。 | AndroidX 官方发布记录 | Document | 读取公开页面并记录可复查结论 | 2026-07-14T10:19:53+08:00 | 版本会变化；实施前必须按锁定依赖再次核对。 |
| E-003 | [Android Developers — MotionScheme](https://developer.android.com/reference/kotlin/androidx/compose/material3/MotionScheme) | MotionScheme 区分 standard/expressive 与 fast/default/slow、effects/spatial；当前加入 1.5.0-alpha23。 | AndroidX API reference | Document | 读取公开页面并记录可复查结论 | 2026-07-14T10:19:53+08:00 | alpha API 不应写成稳定生产契约。 |
| E-004 | [Android Developers — Grids and units](https://developer.android.com/design/ui/mobile/guides/layout-and-content/grids-and-units) | Android 设计使用 8dp 主布局网格、4dp 小元素网格，并按 Compact/Medium/Expanded 讨论窗口。 | Android 官方移动设计指南 | Document | 读取公开页面并记录可复查结论 | 2026-07-14T10:19:53+08:00 | dp/sp 和窗口类别不能原样复制到 Web/iOS。 |
| E-005 | [Android Developers — Compose accessibility API defaults](https://developer.android.com/develop/ui/compose/accessibility/api-defaults) | Material 交互组件默认遵循至少 48dp 目标及语义/组件无障碍行为。 | Jetpack Compose 官方无障碍指南 | Document | 读取公开页面并记录可复查结论 | 2026-07-14T10:19:53+08:00 | 自定义组件或其他平台必须自行实现等价行为。 |
| E-090 | [W3C — Web Content Accessibility Guidelines (WCAG) 2.2](https://www.w3.org/TR/WCAG22/) | WCAG 2.2 规定文本/非文本对比、可见焦点、reflow、目标尺寸、颜色之外的状态线索等可验收基线。 | W3C Recommendation；Web；通用主题与输入模态 | Document | 读取公开页面并记录可复查结论 | 2026-07-14T10:19:53+08:00 | 不替代 Android、HarmonyOS、iOS 或桌面平台的额外要求。 |
| E-091 | [W3C — Media Queries Level 5](https://www.w3.org/TR/mediaqueries-5/) | Web 可查询 prefers-reduced-motion、prefers-reduced-transparency、prefers-contrast、forced-colors 与 prefers-color-scheme 等用户偏好。 | W3C Working Draft；Web 用户偏好媒体特性 | Document | 读取公开页面并记录可复查结论 | 2026-07-14T10:19:53+08:00 | 浏览器支持度与原生平台 API 需要在目标技术栈中另行确认。 |

证据类型与置信度分开：上表只说明来源；正文每条规则另行标注 `observed`、`inferred` 或 `adapted` 与置信度。

## 4. 覆盖矩阵

| 页面或流程 | 组件 | 状态 | 主题 | 视口或输入模态 | 覆盖状态 | 证据 |
|---|---|---|---|---|---|---|
| 公开设计语言/研究 | 原则与基础层 | 文档声明 | 文档涉及范围 | 公开网页 | Covered | E-001、E-002、E-003、E-004、E-005 |
| 跨平台起始包 | Button / FAB、Text Field、Card / Chip、Adaptive Navigation | default / focus / disabled / loading / error 等适用状态 | 默认起始主题 | Web、键盘、指针、触控参考 | Partial | E-001、E-002、E-003、E-004、E-005, E-090, E-091 |
| 真实产品流程 | 目标项目组件 | 全部运行态 | 实际深浅/高对比主题 | 真实设备与视口 | Missing | 无 |

## 5. 设计定位

Material Design 3 是 Google 的开放设计系统，不等同于 Google 品牌视觉。M3 以语义色角色、15 级排版、形状、色调海拔、组件和自适应导航构成系统；Material 3 Expressive 扩展主题、组件、动效、排版与形状。2026-07 的设计方向可采用，但 alpha API 不能无条件作为稳定生产基线。

| 规则 | 可观察/可验收表现 | 来源类型 | 置信度 | 证据 |
|---|---|---|---|---|
| 语义角色 | 组件引用 primary/onPrimary、surface/onSurface、container/onContainer、outline、error 等用途角色，而非业务 hex。 | `observed` | High | E-001 |
| 个人化与动态色 | Android 12+ 可从用户壁纸生成动态明暗主题，不可用时回退品牌主题。 | `observed` | High | E-001 |
| 色调海拔 | 表面层级优先由 surface container 色调区分，阴影为补充。 | `observed` | High | E-001 |
| Expressive 有稳定性边界 | 设计可使用表达性原则；具体 alpha API、MaterialShapes 和 MotionScheme 逐项标预览并提供回退。 | `observed` | High | E-002, E-003 |

### 适用场景

- Android 原生、跨平台移动应用和需要成熟组件/主题系统的产品。
- 需要动态色、明暗主题、自适应导航和完整交互状态的应用。
- 愿意跟踪 Material 库版本并区分稳定与预览 API 的团队。

### 不宜直接套用

- 把 Google Logo、四色、产品插画或文案当成 Material 资产。
- 在 Web/iOS 上无差别复制 Android dp、ripple、FAB 和导航位置。
- 生产环境直接依赖未评估的 Expressive alpha API。

## 6. 设计原则

| 原则 | 可执行规则 | 例外 | 来源与置信度 |
|---|---|---|---|
| 角色成对 | on-* 前景只与对应容器角色组合，业务组件使用 semantic/component token。 | 自定义配色仍保持角色语义和对比。 | `observed`, High, E-001 |
| 表达服务层级 | 颜色、形状、尺寸、动效和 containment 强调关键动作与内容分组。 | 数据密集场景降低表达强度，优先扫描效率。 | `inferred`, High, E-001 |
| 平台自适应 | Compact/Medium/Expanded 下改变导航、sheet、列和内容宽度。 | 行为阈值按目标平台和内容验证。 | `observed`, High, E-001, E-004 |
| 稳定优先 | 生产实现使用稳定库；预览 API 有 feature flag、回退和升级测试。 | 原型可单独启用 alpha，但不得混入稳定基线。 | `observed`, High, E-002, E-003 |

## 7. 基础系统

以下精确值是独立项目起始值，统一为 `adapted / medium`。采用理由：以 M3 语义角色和成熟组件为骨架，用独立品牌色和跨平台映射落地；Expressive 的预览 API 只在明确实验范围内使用。

### 7.1 色彩

| 角色 | 起始值 | 用途 | 主题与状态 | Token | 来源与理由 |
|---|---|---|---|---|---|
| 画布 | `#FFFBFE` | 页面最底层 | 默认 | `semantic.color.background` | `adapted`, E-001, E-004, E-005, E-090；落地前按真实前景/背景复测对比度 |
| 表面 | `#FFFBFE` | 卡片、面板、输入背景 | 默认 | `semantic.color.surface` | `adapted`, E-001, E-004, E-005, E-090；落地前按真实前景/背景复测对比度 |
| 次级表面 | `#E7E0EC` | 弱分区与选中底 | 默认 | `semantic.color.surfaceAlt` | `adapted`, E-001, E-004, E-005, E-090；落地前按真实前景/背景复测对比度 |
| 主要文本 | `#1D1B20` | 标题与正文 | 默认 | `semantic.color.textPrimary` | `adapted`, E-001, E-004, E-005, E-090；落地前按真实前景/背景复测对比度 |
| 次级文本 | `#49454F` | 说明与元数据 | 默认 | `semantic.color.textSecondary` | `adapted`, E-001, E-004, E-005, E-090；落地前按真实前景/背景复测对比度 |
| 必要边界 | `#79747E` | 组件识别与分组 | 默认 | `semantic.color.border` | `adapted`, E-001, E-004, E-005, E-090；落地前按真实前景/背景复测对比度 |
| 主要操作 | `#6750A4` | CTA、激活状态 | 默认/selected | `semantic.color.action` | `adapted`, E-001, E-004, E-005, E-090；落地前按真实前景/背景复测对比度 |
| 操作上内容 | `#FFFFFF` | 主要操作上的文字与图标 | 默认 | `semantic.color.onAction` | `adapted`, E-001, E-004, E-005, E-090；落地前按真实前景/背景复测对比度 |
| 焦点 | `#4F378B` | 键盘焦点轮廓 | focus-visible | `semantic.color.focus` | `adapted`, E-001, E-004, E-005, E-090；落地前按真实前景/背景复测对比度 |
| 成功 | `#2E6B3F` | 成功反馈 | success | `semantic.color.success` | `adapted`, E-001, E-004, E-005, E-090；落地前按真实前景/背景复测对比度 |
| 警告 | `#7A5900` | 警告反馈 | warning | `semantic.color.warning` | `adapted`, E-001, E-004, E-005, E-090；落地前按真实前景/背景复测对比度 |
| 危险 | `#B3261E` | 错误与破坏性操作 | error/danger | `semantic.color.danger` | `adapted`, E-001, E-004, E-005, E-090；落地前按真实前景/背景复测对比度 |

规则：语义色必须通过 token 映射；成功、警告、错误和选中不得只靠颜色表达；品牌来源中的专有色只用于分析，不应被独立产品直接当作自身品牌资产。

### 7.2 字体与内容密度

| 角色 | 字体 | 字号 / 行高 | 字重 | 内容规则 | 来源与证据 |
|---|---|---|---|---|---|
| 辅助 | Roboto / Noto Sans SC / system-ui / sans-serif | `12px` / `16px` | 400–500 | 标签、元数据和帮助文字；不可承载唯一关键信息 | `adapted`, E-001, E-004, E-005, E-090 |
| 正文 | Roboto / Noto Sans SC / system-ui / sans-serif | `16px` / `24px` | 400 | 默认正文与常规控件 | `adapted`, E-001, E-004, E-005, E-090 |
| 模块标题 | Roboto / Noto Sans SC / system-ui / sans-serif | `22px` / `28px` | 600 | 卡片或页面分区标题 | `adapted`, E-001, E-004, E-005, E-090 |
| 展示标题 | Roboto / Noto Sans SC / system-ui / sans-serif | `45px` / `52px` | 600–700 | 低频关键标题，窄屏需流体缩放 | `adapted`, E-001, E-004, E-005, E-090 |

M3 官方 type scale 为 display/headline/title/body/label 五组，每组 large/medium/small，共 15 角色；Compose 文档给出默认 sp 值。Web 应映射为 rem，Android 使用 sp 并尊重系统字号；本 token 仅选代表角色作为起始映射。

### 7.3 布局、网格与间距

| 场景 | 行为规则 | 起始值或范围 | 来源类型 | 置信度 | 证据 |
|---|---|---|---|---|---|
| 主网格 | 布局、组件和间距落在 8dp 主网格。 | `8dp（observed，Android）` | `adapted` | Medium | E-001, E-004, E-005, E-090 |
| 小元素网格 | 图标、字形和细部可落在 4dp 网格。 | `4dp（observed，Android）` | `adapted` | Medium | E-001, E-004, E-005, E-090 |
| 紧凑边距 | 紧凑窗口可用 16dp 起步，大屏自适应。 | `16dp（observed；非全平台固定值）` | `adapted` | Medium | E-001, E-004, E-005, E-090 |
| 跨平台间距 | 消费端映射 4/8 节奏，单位按平台转换。 | `4 / 8 / 12 / 16 / 24 / 32 / 48 / 64` | `adapted` | Medium | E-001, E-004, E-005, E-090 |

不得把建议断点写成已观察断点。先以内容溢出、最小列宽、任务优先级和输入模态确定行为边界，再为工程实现记录断点。

### 7.4 形状、边框、层级与阴影

| 角色 | 规则 | 起始值 | Token | 来源与证据 |
|---|---|---|---|---|
| 控件圆角 | 控件按 M3 shape role 映射；按钮、chip 和 FAB 不共享单一半径。 | `12px` | `semantic.shape.control` | `adapted`, E-001, E-004, E-005, E-090 |
| 容器圆角 | 卡片、sheet、dialog 依据层级选择形状；Expressive morph 有普通圆角回退。 | `16px` | `semantic.shape.container` | `adapted`, E-001, E-004, E-005, E-090 |
| 默认边界 | outlined 组件与 focus 使用明确 outline 角色。 | `1px` | `primitive.stroke.thin` | `adapted`, E-001, E-004, E-005, E-090 |
| 静止表面 | 常态层级以 surface tone 为主。 | `0 1px 2px rgb(29 27 32 / 12%)` | `primitive.effect.shadowRest` | `adapted`, E-001, E-004, E-005, E-090 |
| 抬升表面 | 阴影只补充真实海拔和遮挡。 | `0 8px 24px rgb(29 27 32 / 18%)` | `primitive.effect.shadowRaised` | `adapted`, E-001, E-004, E-005, E-090 |

### 7.5 图标、图像与品牌资产

- 使用 Material Symbols/Icons 时核对许可、主题与目标平台；不把 Google 产品图标当通用 Material 图标。
- 品牌插画、摄影和图标可自定义，但保持组件语义、对比度和尺寸。
- 动态色和 expressive 形状不能降低内容/图标的可辨认性。

### 7.6 动效

| 场景 | 属性 | 起始时长与曲线 | 减弱动效行为 | 来源与证据 |
|---|---|---|---|---|
| 高频状态 | effects：颜色/透明度 | `100ms / standard fast` | 即时切换或短淡化 | `adapted`, E-003, E-091 |
| 常规结构 | effects 或小范围 spatial | `200ms / standard default` | 取消形变/大位移，保留状态 | `adapted`, E-003, E-091 |
| 主转场 | 有限 spatial/shape morph | `300ms / expressive slow；预览实现需回退` | 普通圆角与短淡化 | `adapted`, E-002, E-003, E-091 |

## 8. Token 架构

`design-tokens.json` 是本实施包的结构化单一事实源：

1. `primitive.*` 保存颜色、间距、圆角、排版、时长和效果原值。
2. `semantic.*` 按背景、表面、文本、操作、反馈、焦点和形状角色引用 primitive。
3. `component.*` 为按钮、输入框和卡片绑定 semantic 角色。
4. 主题切换只替换 semantic 映射；未知主题值不写入空 token。
5. 所有叶节点都有 `status`、`evidenceIds`、`confidence`、`scope` 和 `rationale`。

当前 JSON 是跨平台起始源；CSS、Tailwind、Compose、SwiftUI 等映射应在技术栈和版本确定后由该源单向生成。

## 9. 组件规范

### Button / FAB

组件级 provenance：`status=adapted`；`confidence=medium`；`confidenceReason=来源支持风格或交互原则，结构和精确实现值是跨平台起始适配，尚无目标产品运行时证据。`；`evidenceIds=E-001,E-002,E-003,E-004,E-005,E-090,E-091`；`scope=Web 与移动端参考；浅色起始主题；键盘、指针、触控和辅助技术`；`method=公开规范归纳后进行独立项目适配`；`captured_at=2026-07-14T10:19:53+08:00`；`rationale=依据 Material 组件层级建立跨平台起始契约，并保留平台差异。`。

| 项目 | 规范 | 来源与证据 |
|---|---|---|
| 用途与边界 | 按 Material 层级触发主要、次要或低强调动作。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| Anatomy | 容器、标签、可选 leading/trailing icon；loading 指示只在异步动作出现。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| Variants 与 sizes | filled、tonal、outlined、text、FAB/extended FAB；只保留任务需要的变体。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| 适用状态 | default、pressed、focused/focus-visible、disabled、loading；指针平台增加 hover。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| 内容与溢出 | 标签使用清楚动词；FAB 图标必须熟悉且有可访问名称；extended FAB 可加文字。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| 鼠标、键盘与触控 | Android 触控、键盘/DPAD、Web 指针分别遵循平台；异步防重复提交。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| 响应式行为 | 主操作随 Compact/Medium/Expanded 布局改变位置或变体，不无限拉宽。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| 无障碍 | Android 交互目标至少 48dp；Web 同时按 WCAG；focus 和 state programmatic 可读。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| Tokens | component.button.primary.*；semantic.color.action/onAction/focus；primitive.size.targetMin。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| 实现注意事项 | Web/iOS 不机械复制 Android ripple、dp 或 FAB 位置；按目标库实现。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |

### Text Field

组件级 provenance：`status=adapted`；`confidence=medium`；`confidenceReason=来源支持风格或交互原则，结构和精确实现值是跨平台起始适配，尚无目标产品运行时证据。`；`evidenceIds=E-001,E-002,E-003,E-004,E-005,E-090,E-091`；`scope=Web 与移动端参考；浅色起始主题；键盘、指针、触控和辅助技术`；`method=公开规范归纳后进行独立项目适配`；`captured_at=2026-07-14T10:19:53+08:00`；`rationale=保留 Material 语义角色与状态模型，不凭总览补写组件内部数值。`。

| 项目 | 规范 | 来源与证据 |
|---|---|---|
| 用途与边界 | 采集文本并使用 Material 的语义颜色、形状和状态层。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| Anatomy | label、container、input、supporting text、leading/trailing icon；prefix/suffix 按需求。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| Variants 与 sizes | filled / outlined；single-line / multiline；不同时混用无意义变体。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| 适用状态 | default、focused、filled、disabled、read-only、error、loading/validating（项目需要时）。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| 内容与溢出 | label 永久可理解；supporting/error 文本具体说明格式与修复。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| 鼠标、键盘与触控 | 平台标准文本编辑；清除和显隐按钮可键盘/读屏操作。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| 响应式行为 | 宽度受表单布局限制；大屏不无限拉长；软键盘不遮挡字段和提交。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| 无障碍 | 名称、描述、错误关联；错误不只靠色；系统字号与字体缩放可用。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| Tokens | component.input.*；semantic.color.surface/textPrimary/border/focus/danger。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| 实现注意事项 | 组件级 padding、state layer opacity 和高度需按目标 Material 库版本查证。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |

### Card / Chip

组件级 provenance：`status=adapted`；`confidence=medium`；`confidenceReason=来源支持风格或交互原则，结构和精确实现值是跨平台起始适配，尚无目标产品运行时证据。`；`evidenceIds=E-001,E-002,E-003,E-004,E-005,E-090,E-091`；`scope=Web 与移动端参考；浅色起始主题；键盘、指针、触控和辅助技术`；`method=公开规范归纳后进行独立项目适配`；`captured_at=2026-07-14T10:19:53+08:00`；`rationale=结合官方 card/chip 体系与色调海拔原则形成可验收组件。`。

| 项目 | 规范 | 来源与证据 |
|---|---|---|
| 用途与边界 | 以 Material surface、container 和 shape 角色组织内容或轻量选择。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| Anatomy | 容器、内容/标签、可选图标和操作；chip 具备选中或移除部位。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| Variants 与 sizes | Card: filled/elevated/outlined；Chip: assist/filter/input/suggestion。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| 适用状态 | default、pressed、focused、selected/checked、disabled；指针平台增加 hover。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| 内容与溢出 | 选中/过滤语义清楚；卡片内部嵌套操作避免冲突。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| 鼠标、键盘与触控 | Chip 遵循按钮/checkbox 语义；Card 整体交互与内部操作二选一。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| 响应式行为 | 卡片按最小宽度重排；Chip 可换行或横向滚动但不截断关键选项。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| 无障碍 | selected 不只变文字色；role/name/state 完整；目标尺寸和焦点可见。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| Tokens | component.card.*；semantic.color.surface/surfaceAlt/action；semantic.shape.container。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| 实现注意事项 | M3 以色调表面层级优先，阴影只作补充。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |

### Adaptive Navigation

组件级 provenance：`status=adapted`；`confidence=medium`；`confidenceReason=来源支持风格或交互原则，结构和精确实现值是跨平台起始适配，尚无目标产品运行时证据。`；`evidenceIds=E-001,E-002,E-003,E-004,E-005,E-090,E-091`；`scope=Web 与移动端参考；浅色起始主题；键盘、指针、触控和辅助技术`；`method=公开规范归纳后进行独立项目适配`；`captured_at=2026-07-14T10:19:53+08:00`；`rationale=使用 Material 自适应组件关系而不是简单缩放单一导航。`。

| 项目 | 规范 | 来源与证据 |
|---|---|---|
| 用途与边界 | 按窗口尺寸与内容结构在 navigation bar、rail 和 drawer 间选择。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| Anatomy | navigation container、destinations、icon/label、active indicator；drawer 可含 header/sections。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| Variants 与 sizes | bar / rail / drawer；Compact/Medium/Expanded 是行为类别而非视觉目标。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| 适用状态 | default、pressed、focused、selected、disabled（适用时）；pointer 增加 hover。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| 内容与溢出 | 目的地数量与标签符合信息架构；当前项和返回路径持续可见。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| 鼠标、键盘与触控 | 触控、键盘、DPAD 和辅助技术分别正确；方向键模型按组件库。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| 响应式行为 | 窗口和姿态变化时在 bar→rail→drawer 或 sheet→side sheet 间切换，并保留当前目的地。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| 无障碍 | nav/selection 语义、焦点顺序、selected 状态与标签可读。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| Tokens | semantic.color.surfaceAlt/action/focus；primitive.size.targetMin。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| 实现注意事项 | 边界和切换阈值需按目标平台文档与内容测试，不把通用像素断点写成实测。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |

## 10. 页面与流程

| 页面或流程 | 信息层级 | 布局与操作区 | 状态与异常路径 | 响应式行为 | 证据 |
|---|---|---|---|---|---|
| 移动应用主流程 | adaptive navigation → app bar → content → FAB/primary action | M3 surfaces、semantic roles 和目标窗口组件 | loading/empty/error/offline/permission | bar→rail→drawer；sheet→side sheet；内容限宽 | E-001, E-004, adapted |
| 表单流程 | 说明 → fields → supporting/error → primary/secondary actions | filled 或 outlined 一致使用；角色成对 | validation、server error、saving、success | 紧凑单列，大屏分组但保持阅读顺序 | E-001, E-005, adapted |

## 11. 响应式与输入模态

- 以内容和任务触发行为变化：导航拥挤时改型、列宽不足时重排、操作过密时按优先级分层；阈值由目标项目记录。
- 触控界面不依赖 hover；精细指针的 hover 只加强默认可见线索。
- 交互目标起始值采用 48px；Web 合规仍须逐项核对 WCAG 2.2 的 24×24 CSS px 基线及例外。
- 200% 文本缩放与约 320 CSS px reflow 时，不丢失标签、错误、操作、当前状态与恢复路径。
- 使用逻辑方向属性；RTL 只镜像具有方向语义的布局和图标。
- Android 导航可按 bar → rail → drawer 变化；Web/iOS 需转为本平台相应模式。
- 支持方向、分屏、折叠姿态、安全区、edge-to-edge 和软键盘。

## 12. 主题、国际化与极端内容

- 浅色、深色和高对比主题分别映射 semantic token；不得直接反相颜色、阴影、图片或材质。
- 响应 prefers-color-scheme、prefers-contrast、forced-colors、prefers-reduced-motion；透明材质还应处理 prefers-reduced-transparency。
- 使用真实 CJK、拉丁长词、阿拉伯语 RTL、日期、数字、货币和 30%–50% 文案膨胀测试。
- 按钮与标签允许换行或自适应宽度，不通过缩小字号或无提示省略关键动作解决溢出。
- 每个品牌至少有 light/dark 角色；Android 12+ 可叠加 dynamic color 并提供固定品牌回退。
- 高对比、系统字号和 reduced-motion 需要覆盖自定义组件，不能只依赖 Material 默认。

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
| 使用独立项目色盘，不直接复制品牌或案例颜色 | E-001, E-004, E-005, E-090 | 保留风格规律，同时避免品牌混淆并满足具体内容对比度。 | 全部颜色与主题 | `adapted` |
| 采用 primitive → semantic → component 三层 token | E-001, E-004, E-005, E-090, E-090 | 支持主题、状态和平台映射，避免组件硬编码。 | design-tokens.json 与全部组件 | `adapted` |
| 以 M3 设计语言为主，Expressive API 逐项标预览 | E-001, E-002, E-003 | 允许采用当前设计方向，同时避免把 alpha API 写成稳定生产契约。 | 组件、动效、形状与依赖版本 | `adapted` |
| Android 单位与组件行为在其他平台做语义映射 | E-004, E-005 | dp/sp、48dp、ripple 和导航属于平台语境。 | Web、iOS 与跨平台实现 | `adapted` |

## 15. 冲突、未知项与后续材料

| 项目 | 当前证据或冲突 | 影响 | 所需最少材料 | 当前处理 |
|---|---|---|---|---|
| 目标项目与用户任务 | 未提供真实产品和关键流程 | 无法判断密度、组件数量和页面模板 | 产品范围、关键流程、用户与平台 | Draft |
| 真实 token 与组件状态 | 没有代码、设计文件或运行页面 | 推荐值无法视为实测 | 组件库版本、主题文件、代表性页面 | Adapted |
| 对比度与输入模态 | 只有规范目标，没有渲染结果 | 不能标记无障碍通过 | 各主题状态截图、键盘/读屏/触控测试 | Not tested |
| 目标技术栈 | 未指定 Android/Compose、Flutter、Web 或跨平台 | 无法确定组件 API 和代码映射 | 目标平台、库版本与依赖锁 | Draft |
| Expressive 预览范围 | 未确认是否采用 alpha MotionScheme/MaterialShapes | 稳定性与升级风险未知 | 实验功能清单、feature flag 和回退 | Omit until approved |

### 反模式

- 把 M3 Expressive alpha API 写成稳定生产基线。
- 把 Google Logo、四色、插画或产品文案当成 Material 规范。
- 任意组合 container 与不对应的 on-* 前景。
- 在 Web/iOS 无差别复制 Android dp、ripple、FAB 和导航。
- 只靠阴影传达海拔或选中状态。

## 16. 实现与验收说明

- 开发只消费 `design-tokens.json`，不要在组件中另写同义颜色、尺寸或时长。
- 实现前先把目标产品的页面、组件、状态、主题和输入模态填入覆盖矩阵。
- 实现后执行 `design-review-checklist.md`；没有证据的项目保持 `Not tested`。
- Web 至少验证 320 CSS px reflow、200% 文本缩放、键盘全流程、读屏状态公告和 WCAG 2.2 AA 对比度。
- 视觉回归应覆盖默认、focus-visible、disabled、loading、empty、error、长文本、深色或高对比等适用状态。
- 若目标平台提供原生组件和主题能力，优先遵循对应平台规范；本包只定义风格层，不替代平台交互契约。
