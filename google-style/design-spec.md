# Google 风设计规范

> 本文是面向独立产品的可迁移规范，不复制目标品牌的 Logo、商标、专有图标、插画或文案。所有精确起始值均以 `adapted` 标注，不代表目标品牌的内部 token。

## 1. 文档状态

| 字段 | 内容 |
|---|---|
| 状态 | `draft` |
| 目标对象 | 受 Google 品牌视觉价值启发、但具有独立表达的产品语言（明确不含 Material Design） |
| 平台与版本 | Google 当前公开品牌规范与 Google Design 历史/字体材料；采集于 2026-07-14 |
| 目标项目 | 用于 AI Coding 的跨平台风格实施包 |
| 采集日期 | 2026-07-14 |
| 主题、语言与地区 | 自有浅色起始主题；完整深色主题为项目映射；全球多语言 |
| 负责人 | Codex（证据整理）/ 项目团队（落地验证） |

状态为 `draft` 的原因：本轮以公开文档和设计研究为证据，没有指定目标应用、运行时页面、组件库或可测设计文件，因此不能把推荐值标成 `measured` 或把实现质量标成已验证。

## 2. 范围与限制

### 已覆盖

- 公开材料中的风格定位、原则和使用边界（E-001、E-002、E-003、E-004、E-005）。
- 面向独立项目的颜色、排版、间距、形状、层级、动效与语义 token 起始方案。
- 代表性组件：按钮 / Action、输入框 / Field、卡片 / Surface、导航 / Selection、状态标记 / Motion Motif。
- Web WCAG 2.2 AA、用户偏好、键盘/触控/辅助技术和国际化的适配要求。

### 未覆盖

- 目标产品、用户任务、技术栈、组件库、真实页面、运行时样式和设计文件。
- 品牌或平台未公开的内部 token、完整组件状态、动效实现与版本差异。
- 真实深浅主题、高对比模式、断点、设备安全区、性能与视觉回归结果。

### 使用限制

- 只学习可迁移规律，不复制 Logo、商标、专有字体字形、图标、插画、产品图或品牌文案。
- 来源为公开文档和研究，不是目标应用的 DOM、代码、设计节点或像素测量。
- 精确起始值全部标为 adapted；落地后必须按具体前景/背景、状态和平台复测。
- Google 品牌规范禁止第三方模仿其视觉身份；本包不是品牌授权。
- Google Sans 开源许可与品牌模仿限制语境需分开判断，默认采取保守独立字体方案。

## 3. 证据索引

| ID | 来源 | 支持的单一结论 | 上下文 | 证据类型 | 采集方法 | 采集时间 | 限制 |
|---|---|---|---|---|---|---|---|
| E-001 | [Google — Brand Guidance](https://about.google/brand-resource-center/guidance/) | Google 禁止第三方模仿其标志或视觉身份，包括独特色彩组合、图形、产品图标和关联图像。 | 官方品牌资源中心；第三方使用 | Document | 读取公开页面并记录可复查结论 | 2026-07-14T10:19:53+08:00 | 法律和品牌要求可能随使用场景更新，发布前需再次核对。 |
| E-002 | [Google — How to show Google's brand](https://partnermarketinghub.withgoogle.com/brands/google/branding-guidelines/how-to-show-googles-brand/) | 第三方必须清楚呈现自身品牌，并被要求不要使用 Google 品牌色或模仿 Google 品牌字体。 | 官方合作伙伴品牌规范 | Document | 读取公开页面并记录可复查结论 | 2026-07-14T10:19:53+08:00 | 具体合作协议或授权可能另有条款。 |
| E-003 | [Google Design — Evolving the Google Identity](https://design.google/library/evolving-google-identity) | Google 品牌身份以简单、友好、易接近为目标，并使用可伸缩标志元素与状态型动态圆点。 | Google Design 品牌历史文章 | Document | 读取公开页面并记录可复查结论 | 2026-07-14T10:19:53+08:00 | 历史基础不能证明当前全部产品 UI 或组件 token。 |
| E-004 | [Google Design — Making Google Sans Flex](https://design.google/library/google-sans-flex-font) | 大字号品牌字体与小字号文本字体承担不同可读性任务；Google Sans Flex 提供多可变轴并于 2025 年开源。 | Google Design 字体文章 | Document | 读取公开页面并记录可复查结论 | 2026-07-14T10:19:53+08:00 | 开源许可不自动授权第三方模仿 Google 品牌身份。 |
| E-005 | [Google — Gradient G logo announcement](https://blog.google/company-news/inside-google/company-announcements/gradient-g-logo-design/) | 当前 Google G 更新为更明亮、带混合渐变的四色公司级标志。 | Google 官方公告 | Document | 读取公开页面并记录可复查结论 | 2026-07-14T10:19:53+08:00 | 仅支持品牌事实；本规范明确不复制该组合。 |
| E-090 | [W3C — Web Content Accessibility Guidelines (WCAG) 2.2](https://www.w3.org/TR/WCAG22/) | WCAG 2.2 规定文本/非文本对比、可见焦点、reflow、目标尺寸、颜色之外的状态线索等可验收基线。 | W3C Recommendation；Web；通用主题与输入模态 | Document | 读取公开页面并记录可复查结论 | 2026-07-14T10:19:53+08:00 | 不替代 Android、HarmonyOS、iOS 或桌面平台的额外要求。 |
| E-091 | [W3C — Media Queries Level 5](https://www.w3.org/TR/mediaqueries-5/) | Web 可查询 prefers-reduced-motion、prefers-reduced-transparency、prefers-contrast、forced-colors 与 prefers-color-scheme 等用户偏好。 | W3C Working Draft；Web 用户偏好媒体特性 | Document | 读取公开页面并记录可复查结论 | 2026-07-14T10:19:53+08:00 | 浏览器支持度与原生平台 API 需要在目标技术栈中另行确认。 |

证据类型与置信度分开：上表只说明来源；正文每条规则另行标注 `observed`、`inferred` 或 `adapted` 与置信度。

## 4. 覆盖矩阵

| 页面或流程 | 组件 | 状态 | 主题 | 视口或输入模态 | 覆盖状态 | 证据 |
|---|---|---|---|---|---|---|
| 公开设计语言/研究 | 原则与基础层 | 文档声明 | 文档涉及范围 | 公开网页 | Covered | E-001、E-002、E-003、E-004、E-005 |
| 跨平台起始包 | 按钮 / Action、输入框 / Field、卡片 / Surface、导航 / Selection、状态标记 / Motion Motif | default / focus / disabled / loading / error 等适用状态 | 默认起始主题 | Web、键盘、指针、触控参考 | Partial | E-001、E-002、E-003、E-004、E-005, E-090, E-091 |
| 真实产品流程 | 目标项目组件 | 全部运行态 | 实际深浅/高对比主题 | 真实设备与视口 | Missing | 无 |

## 5. 设计定位

本条目只讨论 Google 公司品牌视觉价值，不把 Material Design 的按钮、卡片、导航或色彩系统写成“Google 风”事实。可迁移的是简单、友好、易接近、几何但不冷漠、按状态变化以及大小屏可识别；不可迁移的是 Google 四色组合、标志、产品图标、品牌字体模仿和动态圆点。

| 规则 | 可观察/可验收表现 | 来源类型 | 置信度 | 证据 |
|---|---|---|---|---|
| 简单友好 | 信息层级直接、文案平实、几何形状带少量圆润和玩趣，不显得机械。 | `observed` | High | E-003 |
| 状态驱动 | 品牌/系统动效与 listening、thinking、replying、confirmation 等真实状态对应。 | `observed` | High | E-003 |
| 大字与正文分工 | 展示字体允许更几何和表达性，正文/小字号优先可读性。 | `observed` | High | E-004 |
| 独立品牌优先 | 不使用 Google 四色、标志、产品图标或品牌字体模仿；页面清楚属于自己的品牌。 | `observed` | High | E-001, E-002, E-005 |

### 适用场景

- 希望呈现清晰、友好、全球化和轻微玩趣的搜索、AI、效率或内容产品。
- 愿意自建品牌资产和完整组件系统，只借鉴价值与关系的团队。
- 需要大标题与高可读正文分工，以及状态驱动微交互的产品。

### 不宜直接套用

- 希望直接复制 Google 四色、G、产品图标、圆点、品牌字体或搜索页外观。
- 把 Material 3 的完整组件规范重复命名为 Google 风。
- 对外材料可能暗示 Google 背书、合作或官方产品的场景。

## 6. 设计原则

| 原则 | 可执行规则 | 例外 | 来源与置信度 |
|---|---|---|---|
| 简单而不空洞 | 减少不必要装饰，用排版、留白和清楚下一步建立易接近感。 | 复杂工具仍保留必要密度、帮助和状态。 | `inferred`, Medium, E-003 |
| 几何中有人情味 | 使用稳定几何网格和适度圆润/非传统细节，形成自有角色。 | 专业、高风险场景优先清晰与稳健。 | `inferred`, Medium, E-003 |
| 动效表达系统状态 | 每个几何动效对应真实状态、开始/终止和失败恢复。 | 纯品牌装饰只用于低频非关键时刻。 | `observed`, High, E-003 |
| 品牌边界不可越过 | 自建色盘、字体、图标、标志、插画和组件，不暗示 Google 认可或合作。 | 获得书面授权时按具体授权条款执行。 | `observed`, High, E-001, E-002 |

## 7. 基础系统

以下精确值是独立项目起始值，统一为 `adapted / medium`。采用理由：只迁移简单、友好、几何、状态驱动和多语言可读等价值，所有识别性品牌资产、四色、字体模仿和组件实现均改为独立表达。

### 7.1 色彩

| 角色 | 起始值 | 用途 | 主题与状态 | Token | 来源与理由 |
|---|---|---|---|---|---|
| 画布 | `#F7F9FC` | 页面最底层 | 默认 | `semantic.color.background` | `adapted`, E-001, E-002, E-003, E-090；落地前按真实前景/背景复测对比度 |
| 表面 | `#FFFFFF` | 卡片、面板、输入背景 | 默认 | `semantic.color.surface` | `adapted`, E-001, E-002, E-003, E-090；落地前按真实前景/背景复测对比度 |
| 次级表面 | `#EAF0F8` | 弱分区与选中底 | 默认 | `semantic.color.surfaceAlt` | `adapted`, E-001, E-002, E-003, E-090；落地前按真实前景/背景复测对比度 |
| 主要文本 | `#1B2430` | 标题与正文 | 默认 | `semantic.color.textPrimary` | `adapted`, E-001, E-002, E-003, E-090；落地前按真实前景/背景复测对比度 |
| 次级文本 | `#4D5968` | 说明与元数据 | 默认 | `semantic.color.textSecondary` | `adapted`, E-001, E-002, E-003, E-090；落地前按真实前景/背景复测对比度 |
| 必要边界 | `#667384` | 组件识别与分组 | 默认 | `semantic.color.border` | `adapted`, E-001, E-002, E-003, E-090；落地前按真实前景/背景复测对比度 |
| 主要操作 | `#2B59C3` | CTA、激活状态 | 默认/selected | `semantic.color.action` | `adapted`, E-001, E-002, E-003, E-090；落地前按真实前景/背景复测对比度 |
| 操作上内容 | `#FFFFFF` | 主要操作上的文字与图标 | 默认 | `semantic.color.onAction` | `adapted`, E-001, E-002, E-003, E-090；落地前按真实前景/背景复测对比度 |
| 焦点 | `#174EA6` | 键盘焦点轮廓 | focus-visible | `semantic.color.focus` | `adapted`, E-001, E-002, E-003, E-090；落地前按真实前景/背景复测对比度 |
| 成功 | `#18794E` | 成功反馈 | success | `semantic.color.success` | `adapted`, E-001, E-002, E-003, E-090；落地前按真实前景/背景复测对比度 |
| 警告 | `#8A5A00` | 警告反馈 | warning | `semantic.color.warning` | `adapted`, E-001, E-002, E-003, E-090；落地前按真实前景/背景复测对比度 |
| 危险 | `#B42318` | 错误与破坏性操作 | error/danger | `semantic.color.danger` | `adapted`, E-001, E-002, E-003, E-090；落地前按真实前景/背景复测对比度 |

规则：语义色必须通过 token 映射；成功、警告、错误和选中不得只靠颜色表达；品牌来源中的专有色只用于分析，不应被独立产品直接当作自身品牌资产。

### 7.2 字体与内容密度

| 角色 | 字体 | 字号 / 行高 | 字重 | 内容规则 | 来源与证据 |
|---|---|---|---|---|---|
| 辅助 | Manrope / Noto Sans SC / system-ui / sans-serif | `14px` / `20px` | 400–500 | 标签、元数据和帮助文字；不可承载唯一关键信息 | `adapted`, E-001, E-002, E-003, E-090 |
| 正文 | Manrope / Noto Sans SC / system-ui / sans-serif | `16px` / `24px` | 400 | 默认正文与常规控件 | `adapted`, E-001, E-002, E-003, E-090 |
| 模块标题 | Manrope / Noto Sans SC / system-ui / sans-serif | `26px` / `34px` | 600 | 卡片或页面分区标题 | `adapted`, E-001, E-002, E-003, E-090 |
| 展示标题 | Manrope / Noto Sans SC / system-ui / sans-serif | `48px` / `56px` | 600–700 | 低频关键标题，窄屏需流体缩放 | `adapted`, E-001, E-002, E-003, E-090 |

默认采用独立几何无衬线字体；展示角色可更圆润，正文角色更高可读。若考虑 Google Sans Flex，必须先同时核对开源许可和 Google 品牌模仿限制，并避免与四色、G、圆点等识别元素组合。

### 7.3 布局、网格与间距

| 场景 | 行为规则 | 起始值或范围 | 来源类型 | 置信度 | 证据 |
|---|---|---|---|---|---|
| 页面留白 | 清楚分组与亲和节奏，不让内容拥挤。 | `16 / 24 / 32 / 48 / 64px` | `adapted` | Medium | E-001, E-002, E-003, E-090 |
| 文本层级 | 展示标题与正文分工；长文限制行长。 | `正文建议 ≤68ch` | `adapted` | Medium | E-001, E-002, E-003, E-090 |
| 几何网格 | 图标、插画和组件使用自建网格与比例。 | `8px 主节奏；数值为项目适配` | `adapted` | Medium | E-001, E-002, E-003, E-090 |
| 小尺寸识别 | 标志/图标/状态在小空间简化而非缩小全部细节。 | `按 16/20/24/32px 样例逐级验收` | `adapted` | Medium | E-001, E-002, E-003, E-090 |

不得把建议断点写成已观察断点。先以内容溢出、最小列宽、任务优先级和输入模态确定行为边界，再为工程实现记录断点。

### 7.4 形状、边框、层级与阴影

| 角色 | 规则 | 起始值 | Token | 来源与证据 |
|---|---|---|---|---|
| 控件圆角 | 形状友好清楚但不复制 Google/Material 组件轮廓。 | `10px` | `semantic.shape.control` | `adapted`, E-001, E-002, E-003, E-090 |
| 容器圆角 | 用适度圆角和留白建立自有几何体系。 | `16px` | `semantic.shape.container` | `adapted`, E-001, E-002, E-003, E-090 |
| 默认边界 | 可交互边界和 focus 明确，不依赖 Material state layer。 | `1px` | `primitive.stroke.thin` | `adapted`, E-001, E-002, E-003, E-090 |
| 静止表面 | 常态层级克制。 | `0 1px 2px rgb(24 39 58 / 8%)` | `primitive.effect.shadowRest` | `adapted`, E-001, E-002, E-003, E-090 |
| 抬升表面 | 仅弹层或真实遮挡关系使用。 | `0 8px 24px rgb(24 39 58 / 14%)` | `primitive.effect.shadowRaised` | `adapted`, E-001, E-002, E-003, E-090 |

### 7.5 图标、图像与品牌资产

- 禁止使用或模仿 Google Logo、四色顺序/比例、G、产品图标、动态圆点和关联图像。
- 自建几何插画可有明亮、友好和轻微不规则感，但需形成自己的颜色、角色和形状语法。
- 对外页面和应用商店素材必须清楚属于自身品牌，不暗示 Google 认可或合作。

### 7.6 动效

| 场景 | 属性 | 起始时长与曲线 | 减弱动效行为 | 来源与证据 |
|---|---|---|---|---|
| 控件反馈 | 颜色/形状/短透明度 | `100–180ms / 项目 easing` | 即时状态或短淡化 | `adapted`, E-003, E-091 |
| 状态标记 | 自有几何形状沿一致路径变化 | `180–260ms；持续状态按循环规则` | 改为静态形状、文字与有限淡化 | `adapted`, E-003, E-091 |
| 页面/内容进入 | 少量淡化与短位移 | `≤260ms` | 取消位移，保留显隐和焦点 | `adapted`, E-003, E-091 |

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

组件级 provenance：`status=adapted`；`confidence=medium`；`confidenceReason=来源支持风格或交互原则，结构和精确实现值是跨平台起始适配，尚无目标产品运行时证据。`；`evidenceIds=E-001,E-002,E-003,E-004,E-005,E-090,E-091`；`scope=Web 与移动端参考；浅色起始主题；键盘、指针、触控和辅助技术`；`method=公开规范归纳后进行独立项目适配`；`captured_at=2026-07-14T10:19:53+08:00`；`rationale=为形成可实现、可键盘操作且状态完整的跨平台按钮契约。`。

| 项目 | 规范 | 来源与证据 |
|---|---|---|
| 用途与边界 | 触发即时命令或提交；不把导航链接伪装成按钮。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| Anatomy | 容器、可见标签；图标和进度指示为条件部位。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| Variants 与 sizes | primary / secondary / tertiary / danger；尺寸只在目标密度确定后映射，最小高度引用 token。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| 适用状态 | default、hover（仅精细指针）、focus-visible、active、disabled、loading；loading 与 disabled 分开。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| 内容与溢出 | 优先使用动词短语；loading 时保留宽度和上下文，禁止只显示无标签图标。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| 鼠标、键盘与触控 | Enter/Space 激活；指针与触控按下即反馈；异步时阻止重复提交但保留取消或恢复路径。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| 响应式行为 | 窄容器可全宽，但不能截断关键动词；多个操作按优先级重排。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| 无障碍 | 具备可访问名称；焦点可见且不被遮挡；危险动作有确认或撤销；状态变化可感知。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| Tokens | component.button.primary.*；semantic.color.action/onAction/focus；primitive.size.targetMin。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| 实现注意事项 | 保持简单、友好、可接近和几何清晰，但组件为独立项目自建而非 Google/Material 组件；使用自有主色与标签；不得复制 Google 四色、产品图标、圆点或按钮造型 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |

### 输入框 / Field

组件级 provenance：`status=adapted`；`confidence=medium`；`confidenceReason=来源支持风格或交互原则，结构和精确实现值是跨平台起始适配，尚无目标产品运行时证据。`；`evidenceIds=E-001,E-002,E-003,E-004,E-005,E-090,E-091`；`scope=Web 与移动端参考；浅色起始主题；键盘、指针、触控和辅助技术`；`method=公开规范归纳后进行独立项目适配`；`captured_at=2026-07-14T10:19:53+08:00`；`rationale=风格不能以隐藏标签、低对比边界或仅颜色错误为代价。`。

| 项目 | 规范 | 来源与证据 |
|---|---|---|
| 用途与边界 | 采集短文本或结构化值；标签、说明、错误和输入本体职责分离。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| Anatomy | 永久标签、输入容器、值、可选前后缀、帮助/错误文本。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| Variants 与 sizes | text / password / search / number 等按真实需求启用；不为风格补造类型。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| 适用状态 | default、hover（适用时）、focus-visible、filled、disabled、read-only、error、success（确有必要时）。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| 内容与溢出 | 标签不依赖 placeholder；长错误可换行；格式要求在输入前可获得。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| 鼠标、键盘与触控 | Tab 聚焦；平台标准文本编辑；清除和显隐密码按钮有独立名称；校验时机可预测。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| 响应式行为 | 随容器伸缩但保留标签和错误；软键盘出现时字段与提交操作不被遮挡。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| 无障碍 | 程序化标签、描述和错误关联；错误不只变色；焦点环与错误边界可同时辨认。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| Tokens | component.input.*；semantic.color.textPrimary/border/focus/danger。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| 实现注意事项 | 保持简单、友好、可接近和几何清晰，但组件为独立项目自建而非 Google/Material 组件；不得用表面效果削弱文本与边界。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |

### 卡片 / Surface

组件级 provenance：`status=adapted`；`confidence=medium`；`confidenceReason=来源支持风格或交互原则，结构和精确实现值是跨平台起始适配，尚无目标产品运行时证据。`；`evidenceIds=E-001,E-002,E-003,E-004,E-005,E-090,E-091`；`scope=Web 与移动端参考；浅色起始主题；键盘、指针、触控和辅助技术`；`method=公开规范归纳后进行独立项目适配`；`captured_at=2026-07-14T10:19:53+08:00`；`rationale=将材质或平面风格限制在不破坏信息结构和可操作性的范围内。`。

| 项目 | 规范 | 来源与证据 |
|---|---|---|
| 用途与边界 | 只在信息确有分组、比较或整体操作关系时建立容器。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| Anatomy | 容器、标题、主体；媒体、元数据、操作区为可选部位。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| Variants 与 sizes | static / interactive / selected；interactive 必须在默认状态即可发现。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| 适用状态 | static 无交互状态；interactive 覆盖 default、hover（适用时）、focus-visible、active、selected、disabled（适用时）。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| 内容与溢出 | 卡片标题保持可扫描；整卡点击时内部不得嵌套冲突交互；长内容按内容优先级处理。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| 鼠标、键盘与触控 | 整卡可点击时提供单一语义目标；内部多操作时改为容器加显式按钮。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| 响应式行为 | 从多列到单列按最小可读宽度重排；不可等比缩小文字或触控目标。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| 无障碍 | 语义结构与视觉结构一致；选中不只靠颜色/阴影；必要边界对比可测。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| Tokens | component.card.*；semantic.color.surface/textPrimary/border；semantic.shape.container。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| 实现注意事项 | 保持简单、友好、可接近和几何清晰，但组件为独立项目自建而非 Google/Material 组件；用留白、排版和有限几何层级组织内容，不把 Material 组件写成 Google 品牌事实 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |

### 导航 / Selection

组件级 provenance：`status=adapted`；`confidence=medium`；`confidenceReason=来源支持风格或交互原则，结构和精确实现值是跨平台起始适配，尚无目标产品运行时证据。`；`evidenceIds=E-001,E-002,E-003,E-004,E-005,E-090,E-091`；`scope=Web 与移动端参考；浅色起始主题；键盘、指针、触控和辅助技术`；`method=公开规范归纳后进行独立项目适配`；`captured_at=2026-07-14T10:19:53+08:00`；`rationale=保证风格化导航仍有稳定位置、可发现状态和完整键盘模型。`。

| 项目 | 规范 | 来源与证据 |
|---|---|---|
| 用途与边界 | 表达当前位置、同级切换或层级返回；不混用导航与提交行为。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| Anatomy | 容器、项目、标签、选中指示；图标和徽标为条件部位。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| Variants 与 sizes | 顶部、侧边、底部或标签页按平台与信息架构选择，不能只因风格同时存在。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| 适用状态 | default、hover（适用时）、focus-visible、active、selected、disabled（适用时）。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| 内容与溢出 | 标签短而独立可理解；方向性图标按语义和 RTL 处理；当前项始终可见。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| 鼠标、键盘与触控 | Tab 到控件；组件模式适用时用方向键切换；触控目标满足项目最小值。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| 响应式行为 | 空间不足时按优先级折叠或改型，不隐藏当前状态与返回路径。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| 无障碍 | 正确使用 nav/tablist 等语义；当前页或选中态程序化可读；焦点顺序符合视觉顺序。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| Tokens | semantic.color.textPrimary/action/focus/surfaceAlt；primitive.size.targetMin。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| 实现注意事项 | 保持简单、友好、可接近和几何清晰，但组件为独立项目自建而非 Google/Material 组件；搜索和主要入口清楚直接；当前项与反馈稳定，但视觉资产和色彩完全独立 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |

### 状态标记 / Motion Motif

组件级 provenance：`status=adapted`；`confidence=medium`；`confidenceReason=来源支持风格或交互原则，结构和精确实现值是跨平台起始适配，尚无目标产品运行时证据。`；`evidenceIds=E-001,E-002,E-003,E-004,E-005,E-090,E-091`；`scope=Web 与移动端参考；浅色起始主题；键盘、指针、触控和辅助技术`；`method=公开规范归纳后进行独立项目适配`；`captured_at=2026-07-14T10:19:53+08:00`；`rationale=把公开的状态型品牌动效原则转化为独立、可访问的项目语言。`。

| 项目 | 规范 | 来源与证据 |
|---|---|---|
| 用途与边界 | 用自有几何图形表达 listening、thinking、replying、confirmation 等系统状态。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| Anatomy | 一到多个自有形状、可选文字状态和进度；不得采用 Google 四点组合。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| Variants 与 sizes | idle / listening / processing / responding / success / error；只实现真实系统状态。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| 适用状态 | entering、active、paused/cancelled、completed、failed。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| 内容与溢出 | 始终提供可读状态文本或程序化名称；不以抽象动效独占表达。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| 鼠标、键盘与触控 | 状态展示不抢焦点；可取消时提供显式按钮；键盘与读屏可操作。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| 响应式行为 | 小尺寸简化形状和运动但保留状态文本；大屏不无意义放大。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| 无障碍 | 动态播报节流；reduced-motion 下改为静态形状、文字和短淡化；颜色不是唯一线索。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| Tokens | primitive.motion.*；semantic.color.action/success/danger；semantic.motion.state。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| 实现注意事项 | 借鉴状态驱动与一致几何路径，不复制 Google Dots、四色顺序或动画轨迹。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |

## 10. 页面与流程

| 页面或流程 | 信息层级 | 布局与操作区 | 状态与异常路径 | 响应式行为 | 证据 |
|---|---|---|---|---|---|
| 搜索/问答入口 | 明确问题或任务 → 主输入 → 结果/下一步 | 宽松留白、清晰文本层级、自有主色 | 空、加载、失败、无结果和历史 | 输入和结果按内容宽度重排，主任务持续可见 | E-003, E-004, adapted |
| 产品/功能页 | 价值 → 证据/示例 → 主操作 | 几何插画与排版友好但完全独立 | 媒体失败、长文、本地化和用户设置 | 大标题与留白流体缩放；不固定品牌比例 | E-003, adapted |
| AI 状态流程 | 输入 → listening/processing/responding → 结果/纠正 | 自有状态标记与文本同步 | 取消、超时、错误、部分结果和重试 | 小屏简化动效但不隐藏状态和控制 | E-003, E-090, E-091, adapted |

## 11. 响应式与输入模态

- 以内容和任务触发行为变化：导航拥挤时改型、列宽不足时重排、操作过密时按优先级分层；阈值由目标项目记录。
- 触控界面不依赖 hover；精细指针的 hover 只加强默认可见线索。
- 交互目标起始值采用 44px；Web 合规仍须逐项核对 WCAG 2.2 的 24×24 CSS px 基线及例外。
- 200% 文本缩放与约 320 CSS px reflow 时，不丢失标签、错误、操作、当前状态与恢复路径。
- 使用逻辑方向属性；RTL 只镜像具有方向语义的布局和图标。
- 小空间优先可读文字和核心状态，不复刻 Google 标志/产品图标的小尺寸策略。
- 宽屏留白有上限；结果和表单使用可读最大宽度，操作不无限拉伸。

## 12. 主题、国际化与极端内容

- 浅色、深色和高对比主题分别映射 semantic token；不得直接反相颜色、阴影、图片或材质。
- 响应 prefers-color-scheme、prefers-contrast、forced-colors、prefers-reduced-motion；透明材质还应处理 prefers-reduced-transparency。
- 使用真实 CJK、拉丁长词、阿拉伯语 RTL、日期、数字、货币和 30%–50% 文案膨胀测试。
- 按钮与标签允许换行或自适应宽度，不通过缩小字号或无提示省略关键动作解决溢出。
- 官方品牌标志适用简单黑/白背景不能证明完整 Google 深色 UI token；项目自行建立主题。
- 多语言字体回退优先可读性、字面高度和布局稳定，不能为了品牌相似强制单一字体。

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
| 使用独立项目色盘，不直接复制品牌或案例颜色 | E-001, E-002, E-003, E-090 | 保留风格规律，同时避免品牌混淆并满足具体内容对比度。 | 全部颜色与主题 | `adapted` |
| 采用 primitive → semantic → component 三层 token | E-001, E-002, E-003, E-090, E-090 | 支持主题、状态和平台映射，避免组件硬编码。 | design-tokens.json 与全部组件 | `adapted` |
| Google 风与 Material Design 完全分档 | E-001, E-003 | Google 品牌价值不等于 Material 组件系统，防止来源和适用范围混淆。 | 整个规范与目录结构 | `adapted` |
| 默认不用 Google 品牌色和品牌字体 | E-001, E-002, E-004, E-005 | 开源许可与品牌模仿限制属于不同层面，采用保守独立表达。 | 色彩、字体、图标与对外材料 | `adapted` |

## 15. 冲突、未知项与后续材料

| 项目 | 当前证据或冲突 | 影响 | 所需最少材料 | 当前处理 |
|---|---|---|---|---|
| 目标项目与用户任务 | 未提供真实产品和关键流程 | 无法判断密度、组件数量和页面模板 | 产品范围、关键流程、用户与平台 | Draft |
| 真实 token 与组件状态 | 没有代码、设计文件或运行页面 | 推荐值无法视为实测 | 组件库版本、主题文件、代表性页面 | Adapted |
| 对比度与输入模态 | 只有规范目标，没有渲染结果 | 不能标记无障碍通过 | 各主题状态截图、键盘/读屏/触控测试 | Not tested |
| Google Sans 使用语境 | 开源许可与品牌规范在模仿语境下存在边界 | 误用可能造成品牌混淆 | 当前字体许可、品牌场景和必要法务确认 | Conservative omit |
| 非 Material 通用组件 | Google 没有公开一套独立于 Material 的通用组件库 | 不能称按钮/卡片数值为 Google 官方规范 | 目标项目自有设计系统 | Adapted |

### 反模式

- 复制 Google 四色顺序、渐变、G、产品图标或动态圆点。
- 使用 Google Sans、四色和几何标记组合来制造官方感。
- 把 Material 组件、ripple 或动态色冒充 Google 品牌事实。
- 页面暗示 Google 认可、合作或官方身份。
- 用友好和极简之名删除标签、状态、错误与恢复。

## 16. 实现与验收说明

- 开发只消费 `design-tokens.json`，不要在组件中另写同义颜色、尺寸或时长。
- 实现前先把目标产品的页面、组件、状态、主题和输入模态填入覆盖矩阵。
- 实现后执行 `design-review-checklist.md`；没有证据的项目保持 `Not tested`。
- Web 至少验证 320 CSS px reflow、200% 文本缩放、键盘全流程、读屏状态公告和 WCAG 2.2 AA 对比度。
- 视觉回归应覆盖默认、focus-visible、disabled、loading、empty、error、长文本、深色或高对比等适用状态。
- 若目标平台提供原生组件和主题能力，优先遵循对应平台规范；本包只定义风格层，不替代平台交互契约。
