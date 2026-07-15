# 玻璃拟态设计规范

> 本文是面向独立产品的可迁移规范，不复制目标品牌的 Logo、商标、专有图标、插画或文案。所有精确起始值均以 `adapted` 标注，不代表目标品牌的内部 token。

## 1. 文档状态

| 字段 | 内容 |
|---|---|
| 状态 | `draft` |
| 目标对象 | 具有可访问降级与性能边界的 Glassmorphism |
| 平台与版本 | 抽象风格；参考 Apple Materials、Microsoft Acrylic/Fluent 与 CSS Filter Effects；采集于 2026-07-14 |
| 目标项目 | 用于 AI Coding 的跨平台风格实施包 |
| 采集日期 | 2026-07-14 |
| 主题、语言与地区 | light/dark/opaque-fallback/high-contrast；Web 优先，原生平台按材料 API 映射；全球多语言 |
| 负责人 | Codex（证据整理）/ 项目团队（落地验证） |

状态为 `draft` 的原因：本轮以公开文档和设计研究为证据，没有指定目标应用、运行时页面、组件库或可测设计文件，因此不能把推荐值标成 `measured` 或把实现质量标成已验证。

## 2. 范围与限制

### 已覆盖

- 公开材料中的风格定位、原则和使用边界（E-001、E-002、E-003、E-004、E-005）。
- 面向独立项目的颜色、排版、间距、形状、层级、动效与语义 token 起始方案。
- 代表性组件：玻璃导航 / Floating Toolbar、Popover / Menu、媒体控制层、短内容玻璃卡片。
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
| E-001 | [Apple HIG — Materials](https://developer.apple.com/design/human-interface-guidelines/materials) | Apple 要求按语义使用材料，并适配 Reduce Transparency 与 Increase Contrast；平台材料不是固定通用颜色。 | Apple 平台官方材料指南 | Document | 读取公开页面并记录可复查结论 | 2026-07-14T10:19:53+08:00 | Liquid Glass/Material 规则不可直接当作通用 Web token。 |
| E-002 | [Microsoft — Acrylic material](https://learn.microsoft.com/en-us/windows/apps/design/style/acrylic) | Acrylic 由半透明、blur、tint、noise 构成，适合瞬态表面，并在高对比、关闭透明、低性能等条件下退化为实色。 | Windows 官方材料指南 | Document | 读取公开页面并记录可复查结论 | 2026-07-14T10:19:53+08:00 | Windows 参数和性能行为不能证明其他平台。 |
| E-003 | [Fluent 2 — Material](https://fluent2.microsoft.design/material) | Fluent 将 Acrylic 用于 popover/menu 等 transient light-dismiss surfaces，并区分 Solid、Mica、Acrylic、Smoke。 | Fluent 2 设计系统 | Document | 读取公开页面并记录可复查结论 | 2026-07-14T10:19:53+08:00 | 不同材料不可合并成单一玻璃拟态标准。 |
| E-004 | [CSS Filter Effects Level 2](https://drafts.csswg.org/filter-effects-2/) | backdrop-filter 对元素背后像素生效；嵌套和 backdrop root 会带来绘制、裁切与性能复杂度。 | CSS Working Group Editor's Draft | Document | 读取公开页面并记录可复查结论 | 2026-07-14T10:19:53+08:00 | 草案状态且不构成视觉设计规范；浏览器支持需另验。 |
| E-005 | [W3C — Media Queries Level 5](https://www.w3.org/TR/mediaqueries-5/) | prefers-reduced-transparency、prefers-contrast、forced-colors 和 prefers-reduced-motion 可表达相关用户偏好。 | W3C Working Draft；Web | Document | 读取公开页面并记录可复查结论 | 2026-07-14T10:19:53+08:00 | prefers-reduced-transparency 支持度不能假设完整。 |
| E-090 | [W3C — Web Content Accessibility Guidelines (WCAG) 2.2](https://www.w3.org/TR/WCAG22/) | WCAG 2.2 规定文本/非文本对比、可见焦点、reflow、目标尺寸、颜色之外的状态线索等可验收基线。 | W3C Recommendation；Web；通用主题与输入模态 | Document | 读取公开页面并记录可复查结论 | 2026-07-14T10:19:53+08:00 | 不替代 Android、HarmonyOS、iOS 或桌面平台的额外要求。 |
| E-091 | [W3C — Media Queries Level 5](https://www.w3.org/TR/mediaqueries-5/) | Web 可查询 prefers-reduced-motion、prefers-reduced-transparency、prefers-contrast、forced-colors 与 prefers-color-scheme 等用户偏好。 | W3C Working Draft；Web 用户偏好媒体特性 | Document | 读取公开页面并记录可复查结论 | 2026-07-14T10:19:53+08:00 | 浏览器支持度与原生平台 API 需要在目标技术栈中另行确认。 |

证据类型与置信度分开：上表只说明来源；正文每条规则另行标注 `observed`、`inferred` 或 `adapted` 与置信度。

## 4. 覆盖矩阵

| 页面或流程 | 组件 | 状态 | 主题 | 视口或输入模态 | 覆盖状态 | 证据 |
|---|---|---|---|---|---|---|
| 公开设计语言/研究 | 原则与基础层 | 文档声明 | 文档涉及范围 | 公开网页 | Covered | E-001、E-002、E-003、E-004、E-005 |
| 跨平台起始包 | 玻璃导航 / Floating Toolbar、Popover / Menu、媒体控制层、短内容玻璃卡片 | default / focus / disabled / loading / error 等适用状态 | 默认起始主题 | Web、键盘、指针、触控参考 | Partial | E-001、E-002、E-003、E-004、E-005, E-090, E-091 |
| 真实产品流程 | 目标项目组件 | 全部运行态 | 实际深浅/高对比主题 | 真实设备与视口 | Missing | 无 |

## 5. 设计定位

玻璃拟态没有统一官方标准、固定 token 或组件库。Apple Materials/Liquid Glass 与 Microsoft Acrylic 是各自平台材料系统，CSS backdrop-filter 只是实现原语。可迁移规范是：按语义选择材料、优先单层瞬态表面、最差背景测对比、限制性能成本，并为减少透明度、高对比、无支持和低性能提供不透明回退。

| 规则 | 可观察/可验收表现 | 来源类型 | 置信度 | 证据 |
|---|---|---|---|---|
| 材料有语义 | 玻璃用于导航、菜单、浮动工具、媒体控制和短摘要等保留背景上下文的层。 | `observed` | High | E-001, E-002, E-003 |
| 单层优先 | 避免嵌套 backdrop-filter 与永久全屏多层玻璃。 | `observed` | High | E-002, E-003, E-004 |
| 降级是契约 | 减少透明度、高对比、无支持、低性能或复杂背景时切换不透明表面。 | `observed` | High | E-001, E-002, E-005 |
| 合成后验收 | 文本、边界、图标和焦点在最亮、最暗、最复杂真实背景上测量。 | `inferred` | High | E-001, E-090 |

### 适用场景

- 顶部/底部导航、浮动工具条、菜单、popover、非模态 drawer 和媒体控制。
- 在图片、视频或动态内容上方短时保留背景上下文的操作层。
- 能控制叠层数量、GPU 预算并完整设计不透明降级的产品。

### 不宜直接套用

- 长表单、数据表格、法律文本、密集设置和需要稳定阅读的正文。
- 多层嵌套 card、永久全屏背景和每个区域都 backdrop-filter。
- 只在单一 Chrome/高端设备上验证且没有 opaque fallback 的方案。

## 6. 设计原则

| 原则 | 可执行规则 | 例外 | 来源与置信度 |
|---|---|---|---|
| 内容优先于透射 | 透明只保留上下文，不得让背景干扰文字、控件和错误。 | 背景不可控时提高 tint/dimming 或直接 opaque。 | `observed`, High, E-001, E-002 |
| 材料不嵌套 | 一个视觉区域最多一个 backdrop-filter 材料层。 | 平台原生控件若内部实现不可控，按官方性能指南验收。 | `observed`, High, E-002, E-004 |
| 瞬态优先 | 用于菜单、popover、浮动工具和媒体控制，不作为长表单/表格的永久底。 | 品牌展示的有限大面积效果需单独性能和可读性测试。 | `observed`, High, E-002, E-003 |
| 实色回退同等设计 | fallback 保持信息层级、边界、焦点和品牌语义，而不是临时灰块。 | 强制颜色模式使用系统色和实线边界。 | `observed`, High, E-001, E-002, E-005 |

## 7. 基础系统

以下精确值是独立项目起始值，统一为 `adapted / medium`。采用理由：参考平台材料的语义、瞬态用途和降级要求，建立单层、可测对比、可无障碍回退的跨平台玻璃配方；数值不是任何官方标准。

### 7.1 色彩

| 角色 | 起始值 | 用途 | 主题与状态 | Token | 来源与理由 |
|---|---|---|---|---|---|
| 画布 | `#EAF2FF` | 页面最底层 | 默认 | `semantic.color.background` | `adapted`, E-001, E-002, E-003, E-004, E-090, E-091；落地前按真实前景/背景复测对比度 |
| 表面 | `rgb(255 255 255 / 0.62)` | 卡片、面板、输入背景 | 默认 | `semantic.color.surface` | `adapted`, E-001, E-002, E-003, E-004, E-090, E-091；落地前按真实前景/背景复测对比度 |
| 次级表面 | `rgb(255 255 255 / 0.78)` | 弱分区与选中底 | 默认 | `semantic.color.surfaceAlt` | `adapted`, E-001, E-002, E-003, E-004, E-090, E-091；落地前按真实前景/背景复测对比度 |
| 主要文本 | `#172033` | 标题与正文 | 默认 | `semantic.color.textPrimary` | `adapted`, E-001, E-002, E-003, E-004, E-090, E-091；落地前按真实前景/背景复测对比度 |
| 次级文本 | `#46536A` | 说明与元数据 | 默认 | `semantic.color.textSecondary` | `adapted`, E-001, E-002, E-003, E-004, E-090, E-091；落地前按真实前景/背景复测对比度 |
| 必要边界 | `#66738A` | 组件识别与分组 | 默认 | `semantic.color.border` | `adapted`, E-001, E-002, E-003, E-004, E-090, E-091；落地前按真实前景/背景复测对比度 |
| 主要操作 | `#2457C5` | CTA、激活状态 | 默认/selected | `semantic.color.action` | `adapted`, E-001, E-002, E-003, E-004, E-090, E-091；落地前按真实前景/背景复测对比度 |
| 操作上内容 | `#FFFFFF` | 主要操作上的文字与图标 | 默认 | `semantic.color.onAction` | `adapted`, E-001, E-002, E-003, E-004, E-090, E-091；落地前按真实前景/背景复测对比度 |
| 焦点 | `#0B57D0` | 键盘焦点轮廓 | focus-visible | `semantic.color.focus` | `adapted`, E-001, E-002, E-003, E-004, E-090, E-091；落地前按真实前景/背景复测对比度 |
| 成功 | `#137333` | 成功反馈 | success | `semantic.color.success` | `adapted`, E-001, E-002, E-003, E-004, E-090, E-091；落地前按真实前景/背景复测对比度 |
| 警告 | `#8A5A00` | 警告反馈 | warning | `semantic.color.warning` | `adapted`, E-001, E-002, E-003, E-004, E-090, E-091；落地前按真实前景/背景复测对比度 |
| 危险 | `#B42318` | 错误与破坏性操作 | error/danger | `semantic.color.danger` | `adapted`, E-001, E-002, E-003, E-004, E-090, E-091；落地前按真实前景/背景复测对比度 |

规则：语义色必须通过 token 映射；成功、警告、错误和选中不得只靠颜色表达；品牌来源中的专有色只用于分析，不应被独立产品直接当作自身品牌资产。

### 7.2 字体与内容密度

| 角色 | 字体 | 字号 / 行高 | 字重 | 内容规则 | 来源与证据 |
|---|---|---|---|---|---|
| 辅助 | Inter / Noto Sans SC / system-ui / sans-serif | `14px` / `20px` | 400–500 | 标签、元数据和帮助文字；不可承载唯一关键信息 | `adapted`, E-001, E-002, E-003, E-004, E-090, E-091 |
| 正文 | Inter / Noto Sans SC / system-ui / sans-serif | `16px` / `24px` | 400 | 默认正文与常规控件 | `adapted`, E-001, E-002, E-003, E-004, E-090, E-091 |
| 模块标题 | Inter / Noto Sans SC / system-ui / sans-serif | `24px` / `32px` | 600 | 卡片或页面分区标题 | `adapted`, E-001, E-002, E-003, E-004, E-090, E-091 |
| 展示标题 | Inter / Noto Sans SC / system-ui / sans-serif | `40px` / `48px` | 600–700 | 低频关键标题，窄屏需流体缩放 | `adapted`, E-001, E-002, E-003, E-004, E-090, E-091 |

沿用产品主字体；玻璃不是排版系统。正文至少从 16/24 的可读级别起步，长文、表格和复杂表单使用较实或不透明内层表面。

### 7.3 布局、网格与间距

| 场景 | 行为规则 | 起始值或范围 | 来源类型 | 置信度 | 证据 |
|---|---|---|---|---|---|
| 材料强度 | regular/strong/opaque-fallback 由语义 token 控制。 | `blur 16–24px；tint alpha 0.55–0.75（adapted）` | `adapted` | Medium | E-001, E-002, E-003, E-004, E-090, E-091 |
| 卡片内距 | 短内容有充足边缘，避免与复杂背景混在一起。 | `16 / 24px` | `adapted` | Medium | E-001, E-002, E-003, E-004, E-090, E-091 |
| 叠层 | 一个视觉区域一个 backdrop-filter；浮层之间用不透明/solid 分隔。 | `max 1 backdrop-filter layer` | `adapted` | Medium | E-001, E-002, E-003, E-004, E-090, E-091 |
| 材料区域 | 大屏限制玻璃范围，小屏减少覆盖与卡片数量。 | `按内容和性能预算决定` | `adapted` | Medium | E-001, E-002, E-003, E-004, E-090, E-091 |

不得把建议断点写成已观察断点。先以内容溢出、最小列宽、任务优先级和输入模态确定行为边界，再为工程实现记录断点。

### 7.4 形状、边框、层级与阴影

| 角色 | 规则 | 起始值 | Token | 来源与证据 |
|---|---|---|---|---|
| 控件圆角 | 浮动控件可较圆，但焦点与点击边界保持实色可见。 | `16px` | `semantic.shape.control` | `adapted`, E-001, E-002, E-003, E-004, E-090, E-091 |
| 容器圆角 | 玻璃容器使用少量统一大圆角，不叠多层不同半径。 | `24px` | `semantic.shape.container` | `adapted`, E-001, E-002, E-003, E-004, E-090, E-091 |
| 默认边界 | 1px 起始边界必须按实际合成结果验收；低透明白边不能承担唯一识别。 | `1px` | `primitive.stroke.thin` | `adapted`, E-001, E-002, E-003, E-004, E-090, E-091 |
| 静止表面 | 单层玻璃用柔和阴影与 tint 表达层级。 | `0 8px 32px rgb(15 23 42 / 16%)` | `primitive.effect.shadowRest` | `adapted`, E-001, E-002, E-003, E-004, E-090, E-091 |
| 抬升表面 | 浮层不通过继续增加 blur/嵌套来抬升。 | `0 12px 36px rgb(15 23 42 / 24%)` | `primitive.effect.shadowRaised` | `adapted`, E-001, E-002, E-003, E-004, E-090, E-091 |

### 7.5 图标、图像与品牌资产

- 背景媒体必须有最亮、最暗、最复杂测试样本；不可控背景使用 dimming 或 opaque。
- noise、反光和渐变只作为轻微材料细节，不能持续动画或遮挡内容。
- 不得把 Apple Liquid Glass、visionOS glass、Windows Acrylic 或 Mica 混称为同一规范。

### 7.6 动效

| 场景 | 属性 | 起始时长与曲线 | 减弱动效行为 | 来源与证据 |
|---|---|---|---|---|
| hover/focus | tint/边界变化，不改 blur | `120–180ms` | 即时边界/颜色 | `adapted`, E-002, E-005 |
| 打开/关闭 | 透明度与短位移 | `180–240ms` | 取消位移，保留显隐与焦点 | `adapted`, E-002, E-005 |
| 材料变化 | 禁止持续动画 blur/noise | `状态变化时离散切换` | 直接切换 opaque fallback | `adapted`, E-004, E-005 |

## 8. Token 架构

`design-tokens.json` 是本实施包的结构化单一事实源：

1. `primitive.*` 保存颜色、间距、圆角、排版、时长和效果原值。
2. `semantic.*` 按背景、表面、文本、操作、反馈、焦点和形状角色引用 primitive。
3. `component.*` 为按钮、输入框和卡片绑定 semantic 角色。
4. 主题切换只替换 semantic 映射；未知主题值不写入空 token。
5. 所有叶节点都有 `status`、`evidenceIds`、`confidence`、`scope` 和 `rationale`。

当前 JSON 是跨平台起始源；CSS、Tailwind、Compose、SwiftUI 等映射应在技术栈和版本确定后由该源单向生成。

## 9. 组件规范

### 玻璃导航 / Floating Toolbar

组件级 provenance：`status=adapted`；`confidence=medium`；`confidenceReason=来源支持风格或交互原则，结构和精确实现值是跨平台起始适配，尚无目标产品运行时证据。`；`evidenceIds=E-001,E-002,E-003,E-004,E-005,E-090,E-091`；`scope=Web 与移动端参考；浅色起始主题；键盘、指针、触控和辅助技术`；`method=公开规范归纳后进行独立项目适配`；`captured_at=2026-07-14T10:19:53+08:00`；`rationale=借鉴 Acrylic/平台材料的瞬态用途和降级策略，形成可访问玻璃导航。`。

| 项目 | 规范 | 来源与证据 |
|---|---|---|
| 用途与边界 | 在内容上方提供稳定导航或高频工具，同时保留背景上下文。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| Anatomy | 单层玻璃容器、导航/工具项、选中指示、可选分隔；内容与背景之间有可降级 tint。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| Variants 与 sizes | top/bottom/floating；regular/strong/opaque-fallback 三种材料强度。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| 适用状态 | default、hover（指针）、focus-visible、pressed、selected、disabled、fallback。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| 内容与溢出 | 标签和图标保持简短；必要状态不依赖透明边界或背景颜色。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| 鼠标、键盘与触控 | 触控/键盘行为按导航或工具条语义；背景不接收穿透点击。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| 响应式行为 | 窄屏减少项目或改为抽屉，不叠多层玻璃；大屏限制材料区域。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| 无障碍 | focus 使用独立实色环；最亮/最暗/最复杂背景逐状态测对比；reduced transparency 走实色。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| Tokens | semantic.color.surface/action/focus；semantic.shape.container；primitive.effect.shadowRaised。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| 实现注意事项 | 适合单层浮动导航，不把整页做成模糊永久背景。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |

### Popover / Menu

组件级 provenance：`status=adapted`；`confidence=medium`；`confidenceReason=来源支持风格或交互原则，结构和精确实现值是跨平台起始适配，尚无目标产品运行时证据。`；`evidenceIds=E-001,E-002,E-003,E-004,E-005,E-090,E-091`；`scope=Web 与移动端参考；浅色起始主题；键盘、指针、触控和辅助技术`；`method=公开规范归纳后进行独立项目适配`；`captured_at=2026-07-14T10:19:53+08:00`；`rationale=把平台材料的瞬态用途转换为跨平台菜单/浮层契约。`。

| 项目 | 规范 | 来源与证据 |
|---|---|---|
| 用途与边界 | 在触发点附近承载短时、可轻-dismiss 的选择或命令。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| Anatomy | 玻璃表面、菜单项、可选标题/分组、焦点与关闭逻辑。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| Variants 与 sizes | menu / popover / non-modal drawer；复杂或长内容改为不透明 dialog/page。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| 适用状态 | closed、opening、active、hover/focus、selected、disabled、closing、fallback。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| 内容与溢出 | 项目名称短而可扫描；不能在动态复杂背景上使用低透明文字。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| 鼠标、键盘与触控 | Escape/外部点击关闭；焦点进入、循环或按组件模式管理并恢复。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| 响应式行为 | 窄屏可转实色 bottom sheet；避免玻璃弹层再嵌套玻璃。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| 无障碍 | menu/dialog 语义正确；焦点不被背景吞没；强制颜色使用系统色和实线边界。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| Tokens | component.card.*；semantic.motion.layer；primitive.effect.shadowRaised。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| 实现注意事项 | Microsoft Acrylic 的典型用途是 transient light-dismiss surface，数值配方仍为项目适配。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |

### 媒体控制层

组件级 provenance：`status=adapted`；`confidence=medium`；`confidenceReason=来源支持风格或交互原则，结构和精确实现值是跨平台起始适配，尚无目标产品运行时证据。`；`evidenceIds=E-001,E-002,E-003,E-004,E-005,E-090,E-091`；`scope=Web 与移动端参考；浅色起始主题；键盘、指针、触控和辅助技术`；`method=公开规范归纳后进行独立项目适配`；`captured_at=2026-07-14T10:19:53+08:00`；`rationale=利用玻璃保留媒体上下文，同时设置对比与实色降级底线。`。

| 项目 | 规范 | 来源与证据 |
|---|---|---|
| 用途与边界 | 叠加在图片或视频上提供播放、进度和短时信息。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| Anatomy | 玻璃控制条、播放/时间/音量/字幕等必要操作；scrim 或实色回退。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| Variants 与 sizes | compact / expanded；light/dark tint 根据媒体最差背景选择。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| 适用状态 | hidden、visible、hover/focus、playing/paused、buffering、error、fallback。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| 内容与溢出 | 图标配可访问名称；时间和状态文本不被背景干扰。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| 鼠标、键盘与触控 | 点击媒体显示控制；键盘和辅助技术始终可获得；自动隐藏时 focus/hover 暂停。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| 响应式行为 | 小屏减少次要控制但保留字幕、播放和退出；安全区内布局。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| 无障碍 | 控制与背景最差位置测对比；自动隐藏不困住焦点；状态可读。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| Tokens | semantic.color.textPrimary/focus/danger；primitive.motion.*。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| 实现注意事项 | 背景不可控时提高 tint、增加 dimming 或直接切换 opaque，不坚持透明。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |

### 短内容玻璃卡片

组件级 provenance：`status=adapted`；`confidence=medium`；`confidenceReason=来源支持风格或交互原则，结构和精确实现值是跨平台起始适配，尚无目标产品运行时证据。`；`evidenceIds=E-001,E-002,E-003,E-004,E-005,E-090,E-091`；`scope=Web 与移动端参考；浅色起始主题；键盘、指针、触控和辅助技术`；`method=公开规范归纳后进行独立项目适配`；`captured_at=2026-07-14T10:19:53+08:00`；`rationale=限制玻璃卡片的内容和叠层，避免把审美效果扩张为全页面容器。`。

| 项目 | 规范 | 来源与证据 |
|---|---|---|
| 用途与边界 | 承载摘要、状态或少量操作；不用于长表单、表格和法律文本。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| Anatomy | 单层玻璃容器、标题、简短正文、可选一个主操作。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| Variants 与 sizes | regular / strong / opaque-fallback；interactive 与 static 分开。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| 适用状态 | default、hover/focus（interactive）、pressed、selected、error、fallback。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| 内容与溢出 | 正文长度受限；超出进入详情或改用不透明表面。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| 鼠标、键盘与触控 | 整卡与内部操作避免冲突；背景不可点击穿透。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| 响应式行为 | 一层卡片即可；小屏减少数量和阴影，禁止多层互相覆盖。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| 无障碍 | 文本对比按合成结果测；error 优先实色容器；focus 实色可见。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| Tokens | component.card.*；semantic.color.surface/textPrimary/border。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| 实现注意事项 | 只承载有限内容，信息密度或对比不可控时必须使用不透明卡片。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |

## 10. 页面与流程

| 页面或流程 | 信息层级 | 布局与操作区 | 状态与异常路径 | 响应式行为 | 证据 |
|---|---|---|---|---|---|
| 媒体详情 | 媒体 → 玻璃控制层 → 详情/操作 | 单层控制与必要 scrim，正文用实色表面 | buffering/error/captions/controls hidden | 安全区内布局；窄屏减少次要控制 | E-001, E-002, E-090, adapted |
| 工具/内容页 | 实色主内容 → 玻璃浮动导航/工具 → 瞬态菜单 | 材料只用于浮动和短时操作 | fallback/high-contrast/reduced-transparency | 小屏减少叠层，大屏限制材料区域 | E-002, E-003, E-004, adapted |

## 11. 响应式与输入模态

- 以内容和任务触发行为变化：导航拥挤时改型、列宽不足时重排、操作过密时按优先级分层；阈值由目标项目记录。
- 触控界面不依赖 hover；精细指针的 hover 只加强默认可见线索。
- 交互目标起始值采用 44px；Web 合规仍须逐项核对 WCAG 2.2 的 24×24 CSS px 基线及例外。
- 200% 文本缩放与约 320 CSS px reflow 时，不丢失标签、错误、操作、当前状态与恢复路径。
- 使用逻辑方向属性；RTL 只镜像具有方向语义的布局和图标。
- 用 @supports 检测 backdrop-filter；不支持时走不透明 fallback。
- 窄屏减少玻璃卡片互相覆盖；大屏不把整个窗口变成模糊纹理。

## 12. 主题、国际化与极端内容

- 浅色、深色和高对比主题分别映射 semantic token；不得直接反相颜色、阴影、图片或材质。
- 响应 prefers-color-scheme、prefers-contrast、forced-colors、prefers-reduced-motion；透明材质还应处理 prefers-reduced-transparency。
- 使用真实 CJK、拉丁长词、阿拉伯语 RTL、日期、数字、货币和 30%–50% 文案膨胀测试。
- 按钮与标签允许换行或自适应宽度，不通过缩小字号或无提示省略关键动作解决溢出。
- light/dark 分别设计 tint、border、shadow 和 opaque fallback；不能反相一套玻璃配方。
- prefers-reduced-transparency 尚不能假设全浏览器支持，同时提供应用内或平台级实色降级。

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
| 使用独立项目色盘，不直接复制品牌或案例颜色 | E-001, E-002, E-003, E-004, E-090, E-091 | 保留风格规律，同时避免品牌混淆并满足具体内容对比度。 | 全部颜色与主题 | `adapted` |
| 采用 primitive → semantic → component 三层 token | E-001, E-002, E-003, E-004, E-090, E-091, E-090 | 支持主题、状态和平台映射，避免组件硬编码。 | design-tokens.json 与全部组件 | `adapted` |
| 玻璃限定为单层、瞬态或短内容表面 | E-002, E-003, E-004 | 降低叠层、性能和可读性风险。 | 导航、菜单、工具、媒体控制和短卡片 | `adapted` |
| 每个材料 token 配 opaque fallback | E-001, E-002, E-005, E-090 | 支持减少透明度、高对比、无支持和低性能。 | 全部玻璃表面 | `adapted` |

## 15. 冲突、未知项与后续材料

| 项目 | 当前证据或冲突 | 影响 | 所需最少材料 | 当前处理 |
|---|---|---|---|---|
| 目标项目与用户任务 | 未提供真实产品和关键流程 | 无法判断密度、组件数量和页面模板 | 产品范围、关键流程、用户与平台 | Draft |
| 真实 token 与组件状态 | 没有代码、设计文件或运行页面 | 推荐值无法视为实测 | 组件库版本、主题文件、代表性页面 | Adapted |
| 对比度与输入模态 | 只有规范目标，没有渲染结果 | 不能标记无障碍通过 | 各主题状态截图、键盘/读屏/触控测试 | Not tested |
| 浏览器/GPU 预算 | 未指定目标设备和支持矩阵 | blur 性能与 backdrop root 行为未知 | 浏览器矩阵、GPU/内存预算和滚动性能测试 | Draft |
| 平台材料目标 | 未确认是通用 glass、Acrylic 或 Liquid Glass | 语义与 API 可能不同 | 明确目标平台和材料 API | Draft |

### 反模式

- 宣称‘20px blur / 24px radius’是玻璃拟态官方标准。
- 把 Apple Liquid Glass、visionOS glass、Windows Acrylic 和 Mica 混成同一体系。
- 多层 backdrop-filter 嵌套或大面积永久模糊。
- 在动态视频上直接放低透明文字。
- 只在 Chrome 验收且没有不透明、高对比和减少透明度回退。

## 16. 实现与验收说明

- 开发只消费 `design-tokens.json`，不要在组件中另写同义颜色、尺寸或时长。
- 实现前先把目标产品的页面、组件、状态、主题和输入模态填入覆盖矩阵。
- 实现后执行 `design-review-checklist.md`；没有证据的项目保持 `Not tested`。
- Web 至少验证 320 CSS px reflow、200% 文本缩放、键盘全流程、读屏状态公告和 WCAG 2.2 AA 对比度。
- 视觉回归应覆盖默认、focus-visible、disabled、loading、empty、error、长文本、深色或高对比等适用状态。
- 若目标平台提供原生组件和主题能力，优先遵循对应平台规范；本包只定义风格层，不替代平台交互契约。
