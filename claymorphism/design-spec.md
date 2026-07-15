# 粘土拟态设计规范

> 本文是面向独立产品的可迁移规范，不复制目标品牌的 Logo、商标、专有图标、插画或文案。所有精确起始值均以 `adapted` 标注，不代表目标品牌的内部 token。

## 1. 文档状态

| 字段 | 内容 |
|---|---|
| 状态 | `draft` |
| 目标对象 | 可访问、低到中密度的 Claymorphism |
| 平台与版本 | 抽象行业风格；CSS 阴影/圆角/变换与 WCAG 为可验证基础；采集于 2026-07-14 |
| 目标项目 | 用于 AI Coding 的跨平台风格实施包 |
| 采集日期 | 2026-07-14 |
| 主题、语言与地区 | 浅色 pastel 起始主题；深色与高对比需独立设计；Web 与移动端参考；全球多语言 |
| 负责人 | Codex（证据整理）/ 项目团队（落地验证） |

状态为 `draft` 的原因：本轮以公开文档和设计研究为证据，没有指定目标应用、运行时页面、组件库或可测设计文件，因此不能把推荐值标成 `measured` 或把实现质量标成已验证。

## 2. 范围与限制

### 已覆盖

- 公开材料中的风格定位、原则和使用边界（E-001、E-002、E-003）。
- 面向独立项目的颜色、排版、间距、形状、层级、动效与语义 token 起始方案。
- 代表性组件：Clay Button / FAB、Clay Card / Summary、Toggle / Selection、Text Field。
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
| E-001 | [W3C — CSS Backgrounds and Borders Level 3](https://www.w3.org/TR/css-backgrounds-3/) | CSS 定义 border-radius 与多重 inset/outset box-shadow 的绘制语义。 | W3C CSS 规范；Web | Document | 读取公开页面并记录可复查结论 | 2026-07-14T10:19:53+08:00 | 只证明技术原语，不定义 Claymorphism 风格或数值。 |
| E-002 | [W3C — CSS Transforms Level 1](https://www.w3.org/TR/css-transforms-1/) | CSS transform 提供 translate、scale 等交互形变及其绘制/布局影响。 | W3C CSS 规范；Web | Document | 读取公开页面并记录可复查结论 | 2026-07-14T10:19:53+08:00 | 只证明实现能力，不证明按压时长和比例。 |
| E-003 | [W3C — Understanding Non-text Contrast](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast) | 识别控件和状态所需的边界、图形与焦点需满足非文本对比；阴影不能自动视为可靠边界。 | WCAG 2.2 Understanding 文档 | Document | 读取公开页面并记录可复查结论 | 2026-07-14T10:19:53+08:00 | 合规需基于真实渲染和相邻颜色测量。 |
| E-090 | [W3C — Web Content Accessibility Guidelines (WCAG) 2.2](https://www.w3.org/TR/WCAG22/) | WCAG 2.2 规定文本/非文本对比、可见焦点、reflow、目标尺寸、颜色之外的状态线索等可验收基线。 | W3C Recommendation；Web；通用主题与输入模态 | Document | 读取公开页面并记录可复查结论 | 2026-07-14T10:19:53+08:00 | 不替代 Android、HarmonyOS、iOS 或桌面平台的额外要求。 |
| E-091 | [W3C — Media Queries Level 5](https://www.w3.org/TR/mediaqueries-5/) | Web 可查询 prefers-reduced-motion、prefers-reduced-transparency、prefers-contrast、forced-colors 与 prefers-color-scheme 等用户偏好。 | W3C Working Draft；Web 用户偏好媒体特性 | Document | 读取公开页面并记录可复查结论 | 2026-07-14T10:19:53+08:00 | 浏览器支持度与原生平台 API 需要在目标技术栈中另行确认。 |

证据类型与置信度分开：上表只说明来源；正文每条规则另行标注 `observed`、`inferred` 或 `adapted` 与置信度。

## 4. 覆盖矩阵

| 页面或流程 | 组件 | 状态 | 主题 | 视口或输入模态 | 覆盖状态 | 证据 |
|---|---|---|---|---|---|---|
| 公开设计语言/研究 | 原则与基础层 | 文档声明 | 文档涉及范围 | 公开网页 | Covered | E-001、E-002、E-003 |
| 跨平台起始包 | Clay Button / FAB、Clay Card / Summary、Toggle / Selection、Text Field | default / focus / disabled / loading / error 等适用状态 | 默认起始主题 | Web、键盘、指针、触控参考 | Partial | E-001、E-002、E-003, E-090, E-091 |
| 真实产品流程 | 目标项目组件 | 全部运行态 | 实际深浅/高对比主题 | 真实设备与视口 | Missing | 无 |

## 5. 设计定位

粘土拟态没有 canonical 官方设计系统、固定色板、阴影公式或组件 API。它通常用实色、大圆角、饱满体积、统一光源、外阴影和内高光形成软胶/黏土感，与透明模糊的玻璃拟态不同。所有视觉配方都是项目适配；标准来源只证明 CSS 原语和可访问性底线。

| 规则 | 可观察/可验收表现 | 来源类型 | 置信度 | 证据 |
|---|---|---|---|---|
| 饱满实色 | 表面不透射背景，使用大圆角、实色和内外阴影形成体积。 | `inferred` | Medium | E-001 |
| 统一光源 | 高光、外阴影和 pressed 内阴影共享同一主光方向。 | `inferred` | Medium | E-001 |
| 有限密度 | 粘土化集中在主按钮、轻量卡片、头像、标签和空状态，表格/长文保持平面。 | `adapted` | High | E-003, E-090 |
| 状态多线索 | 选择、焦点、错误和按下使用实色、边界、图标/文字与轻形变组合。 | `adapted` | High | E-002, E-003, E-090 |

### 适用场景

- 教育、儿童、健康、创意、轻量消费、空状态和希望友好活泼的品牌体验。
- 主按钮、FAB、轻量摘要卡、头像、标签、toggle 和插画容器。
- 能限制信息密度并愿意单独设计高对比/forced-colors 降级的产品。

### 不宜直接套用

- 高密度企业后台、交易、医疗监控和大规模数据表格的主体。
- 需要长文、复杂表单或精细比较，却把所有内容做成厚重气泡。
- 只靠软阴影表达可点击、选中、焦点或错误的方案。

## 6. 设计原则

| 原则 | 可执行规则 | 例外 | 来源与置信度 |
|---|---|---|---|
| 实色而非玻璃 | surface 具有稳定填充，背景不会穿透；体积来自光影。 | 插画可有半透明高光，但内容表面保持实色。 | `inferred`, Medium, E-001 |
| 光源一致 | 同一页面的 highlight、shadow 和 pressed 方向一致。 | 不同场景可切换光源，但不能在同一层级混用。 | `inferred`, Medium, E-001 |
| 体积有节制 | 只为高价值操作和轻量容器提供明显体积，高密度内容保持平面。 | 品牌展示可更强，但仍需对比和性能验证。 | `adapted`, High, E-003, E-090 |
| 阴影不承担语义 | 必要边界、focus、selected 和 error 通过实色/描边/图标/文字表达。 | 阴影可作为额外按压和层级反馈。 | `observed`, High, E-003 |

## 7. 基础系统

以下精确值是独立项目起始值，统一为 `adapted / medium`。采用理由：用实色、统一光源和有限内外阴影形成柔软体积，只在低到中密度、高价值组件使用；所有数值均为项目配方而非官方标准。

### 7.1 色彩

| 角色 | 起始值 | 用途 | 主题与状态 | Token | 来源与理由 |
|---|---|---|---|---|---|
| 画布 | `#F5F3FF` | 页面最底层 | 默认 | `semantic.color.background` | `adapted`, E-001, E-002, E-003, E-090, E-091；落地前按真实前景/背景复测对比度 |
| 表面 | `#EDE9FE` | 卡片、面板、输入背景 | 默认 | `semantic.color.surface` | `adapted`, E-001, E-002, E-003, E-090, E-091；落地前按真实前景/背景复测对比度 |
| 次级表面 | `#DDD6FE` | 弱分区与选中底 | 默认 | `semantic.color.surfaceAlt` | `adapted`, E-001, E-002, E-003, E-090, E-091；落地前按真实前景/背景复测对比度 |
| 主要文本 | `#211B2E` | 标题与正文 | 默认 | `semantic.color.textPrimary` | `adapted`, E-001, E-002, E-003, E-090, E-091；落地前按真实前景/背景复测对比度 |
| 次级文本 | `#514A5D` | 说明与元数据 | 默认 | `semantic.color.textSecondary` | `adapted`, E-001, E-002, E-003, E-090, E-091；落地前按真实前景/背景复测对比度 |
| 必要边界 | `#6F6280` | 组件识别与分组 | 默认 | `semantic.color.border` | `adapted`, E-001, E-002, E-003, E-090, E-091；落地前按真实前景/背景复测对比度 |
| 主要操作 | `#6D28D9` | CTA、激活状态 | 默认/selected | `semantic.color.action` | `adapted`, E-001, E-002, E-003, E-090, E-091；落地前按真实前景/背景复测对比度 |
| 操作上内容 | `#FFFFFF` | 主要操作上的文字与图标 | 默认 | `semantic.color.onAction` | `adapted`, E-001, E-002, E-003, E-090, E-091；落地前按真实前景/背景复测对比度 |
| 焦点 | `#4C1D95` | 键盘焦点轮廓 | focus-visible | `semantic.color.focus` | `adapted`, E-001, E-002, E-003, E-090, E-091；落地前按真实前景/背景复测对比度 |
| 成功 | `#176B3A` | 成功反馈 | success | `semantic.color.success` | `adapted`, E-001, E-002, E-003, E-090, E-091；落地前按真实前景/背景复测对比度 |
| 警告 | `#8A5A00` | 警告反馈 | warning | `semantic.color.warning` | `adapted`, E-001, E-002, E-003, E-090, E-091；落地前按真实前景/背景复测对比度 |
| 危险 | `#A12622` | 错误与破坏性操作 | error/danger | `semantic.color.danger` | `adapted`, E-001, E-002, E-003, E-090, E-091；落地前按真实前景/背景复测对比度 |

规则：语义色必须通过 token 映射；成功、警告、错误和选中不得只靠颜色表达；品牌来源中的专有色只用于分析，不应被独立产品直接当作自身品牌资产。

### 7.2 字体与内容密度

| 角色 | 字体 | 字号 / 行高 | 字重 | 内容规则 | 来源与证据 |
|---|---|---|---|---|---|
| 辅助 | Nunito Sans / Noto Sans SC / system-ui / sans-serif | `14px` / `20px` | 400–500 | 标签、元数据和帮助文字；不可承载唯一关键信息 | `adapted`, E-001, E-002, E-003, E-090, E-091 |
| 正文 | Nunito Sans / Noto Sans SC / system-ui / sans-serif | `16px` / `24px` | 400 | 默认正文与常规控件 | `adapted`, E-001, E-002, E-003, E-090, E-091 |
| 模块标题 | Nunito Sans / Noto Sans SC / system-ui / sans-serif | `22px` / `30px` | 600 | 卡片或页面分区标题 | `adapted`, E-001, E-002, E-003, E-090, E-091 |
| 展示标题 | Nunito Sans / Noto Sans SC / system-ui / sans-serif | `36px` / `44px` | 600–700 | 低频关键标题，窄屏需流体缩放 | `adapted`, E-001, E-002, E-003, E-090, E-091 |

可用略圆润 sans-serif 强化亲和感，但正文、数字、表格和代码优先辨识度；正文不使用手写或过度圆润字体。

### 7.3 布局、网格与间距

| 场景 | 行为规则 | 起始值或范围 | 来源类型 | 置信度 | 证据 |
|---|---|---|---|---|---|
| 间距节奏 | 8px 主基线，给饱满控件足够呼吸空间。 | `8 / 12 / 16 / 24 / 32 / 48px` | `adapted` | Medium | E-001, E-002, E-003, E-090, E-091 |
| 圆角级别 | 同屏最多 2–3 个主要半径，full 只给 pill/圆形。 | `12–16 / 20–28 / full` | `adapted` | Medium | E-001, E-002, E-003, E-090, E-091 |
| 阴影层数 | 卡片使用外阴影 + 内高光/暗部；高密度区域简化。 | `最多 3 个语义影层` | `adapted` | Medium | E-001, E-002, E-003, E-090, E-091 |
| 内容密度 | 主内容保持低到中密度；复杂数据转平面内层。 | `按可读性和任务效率决定` | `adapted` | Medium | E-001, E-002, E-003, E-090, E-091 |

不得把建议断点写成已观察断点。先以内容溢出、最小列宽、任务优先级和输入模态确定行为边界，再为工程实现记录断点。

### 7.4 形状、边框、层级与阴影

| 角色 | 规则 | 起始值 | Token | 来源与证据 |
|---|---|---|---|---|
| 控件圆角 | 小控件 12–16px，按钮可 16–20px；同屏限制主要半径级别。 | `16px` | `semantic.shape.control` | `adapted`, E-001, E-002, E-003, E-090, E-091 |
| 容器圆角 | 卡片 20–28px 起始范围；不是官方 Clay 标准。 | `24px` | `semantic.shape.container` | `adapted`, E-001, E-002, E-003, E-090, E-091 |
| 默认边界 | 必要控件可加 1–2px 实线边界，可用性优先于纯软体外观。 | `1px` | `primitive.stroke.thin` | `adapted`, E-001, E-002, E-003, E-090, E-091 |
| 静止表面 | 静止表面使用一致内高光/暗部与适度外阴影。 | `0 14px 28px rgb(63 43 92 / 18%), inset 6px 6px 12px rgb(255 255 255 / 55%), inset -6px -6px 12px rgb(83 58 120 / 14%)` | `primitive.effect.shadowRest` | `adapted`, E-001, E-002, E-003, E-090, E-091 |
| 抬升表面 | 主操作可稍强体积；不要每张卡片提升到同一强度。 | `0 18px 36px rgb(63 43 92 / 22%), inset 7px 7px 14px rgb(255 255 255 / 58%), inset -7px -7px 14px rgb(83 58 120 / 16%)` | `primitive.effect.shadowRaised` | `adapted`, E-001, E-002, E-003, E-090, E-091 |

### 7.5 图标、图像与品牌资产

- 粘土插画和图标可使用自有 3D/2D 软体资产，但需授权、压缩和多尺寸输出。
- 同一场景保持光源、材质软硬和颜色温度一致。
- 装饰高光和阴影不能遮挡文字、焦点、错误或状态图标。

### 7.6 动效

| 场景 | 属性 | 起始时长与曲线 | 减弱动效行为 | 来源与证据 |
|---|---|---|---|---|
| pressed | scale 0.98 + 外阴影收紧 + 内阴影增强 | `120–160ms` | 取消 scale/translate，使用填充/边界/图标 | `adapted`, E-001, E-002, E-091 |
| release/hover | 恢复体积或上移 1–2px | `160–220ms` | 即时恢复或短颜色变化 | `adapted`, E-002, E-091 |
| 卡片进入 | 淡化与极短位移 | `≤220ms` | 取消位移，保留显隐 | `adapted`, E-002, E-091 |

## 8. Token 架构

`design-tokens.json` 是本实施包的结构化单一事实源：

1. `primitive.*` 保存颜色、间距、圆角、排版、时长和效果原值。
2. `semantic.*` 按背景、表面、文本、操作、反馈、焦点和形状角色引用 primitive。
3. `component.*` 为按钮、输入框和卡片绑定 semantic 角色。
4. 主题切换只替换 semantic 映射；未知主题值不写入空 token。
5. 所有叶节点都有 `status`、`evidenceIds`、`confidence`、`scope` 和 `rationale`。

当前 JSON 是跨平台起始源；CSS、Tailwind、Compose、SwiftUI 等映射应在技术栈和版本确定后由该源单向生成。

## 9. 组件规范

### Clay Button / FAB

组件级 provenance：`status=adapted`；`confidence=medium`；`confidenceReason=来源支持风格或交互原则，结构和精确实现值是跨平台起始适配，尚无目标产品运行时证据。`；`evidenceIds=E-001,E-002,E-003,E-090,E-091`；`scope=Web 与移动端参考；浅色起始主题；键盘、指针、触控和辅助技术`；`method=公开规范归纳后进行独立项目适配`；`captured_at=2026-07-14T10:19:53+08:00`；`rationale=把饱满体积限制在高价值操作，并补充可靠边界、焦点和状态。`。

| 项目 | 规范 | 来源与证据 |
|---|---|---|
| 用途与边界 | 用饱满体积和短促按压反馈突出主要动作。 | `adapted`, Medium, E-001, E-002, E-003, E-090, E-091 |
| Anatomy | 实色软体容器、标签/图标、外投影、内高光；focus 环独立。 | `adapted`, Medium, E-001, E-002, E-003, E-090, E-091 |
| Variants 与 sizes | primary / secondary / icon/FAB；危险操作使用独立语义而非只换粉彩。 | `adapted`, Medium, E-001, E-002, E-003, E-090, E-091 |
| 适用状态 | default、hover（指针）、focus-visible、pressed、disabled、loading、success/error。 | `adapted`, Medium, E-001, E-002, E-003, E-090, E-091 |
| 内容与溢出 | 主按钮有可见文字或熟悉图标；loading 保持尺寸。 | `adapted`, Medium, E-001, E-002, E-003, E-090, E-091 |
| 鼠标、键盘与触控 | 按下短促 scale/阴影变化；Enter/Space/触控一致；异步防重复提交。 | `adapted`, Medium, E-001, E-002, E-003, E-090, E-091 |
| 响应式行为 | 小屏减少阴影层数但保留目标尺寸；不把大软体控件挤成微型。 | `adapted`, Medium, E-001, E-002, E-003, E-090, E-091 |
| 无障碍 | 2–3px 高对比 focus；pressed/selected 不只靠凹陷阴影；文本和图标逐状态测对比。 | `adapted`, Medium, E-001, E-002, E-003, E-090, E-091 |
| Tokens | component.button.primary.*；primitive.effect.*；semantic.color.focus。 | `adapted`, Medium, E-001, E-002, E-003, E-090, E-091 |
| 实现注意事项 | scale 不改变点击区域；reduced-motion 下取消 scale/translate。 | `adapted`, Medium, E-001, E-002, E-003, E-090, E-091 |

### Clay Card / Summary

组件级 provenance：`status=adapted`；`confidence=medium`；`confidenceReason=来源支持风格或交互原则，结构和精确实现值是跨平台起始适配，尚无目标产品运行时证据。`；`evidenceIds=E-001,E-002,E-003,E-090,E-091`；`scope=Web 与移动端参考；浅色起始主题；键盘、指针、触控和辅助技术`；`method=公开规范归纳后进行独立项目适配`；`captured_at=2026-07-14T10:19:53+08:00`；`rationale=保留粘土的饱满感，同时限制内容密度和依赖阴影的风险。`。

| 项目 | 规范 | 来源与证据 |
|---|---|---|
| 用途与边界 | 以柔软、实色、饱满容器承载轻量摘要、空状态或创意内容。 | `adapted`, Medium, E-001, E-002, E-003, E-090, E-091 |
| Anatomy | 实色容器、标题、简短内容、可选图标/插画和一个主操作。 | `adapted`, Medium, E-001, E-002, E-003, E-090, E-091 |
| Variants 与 sizes | static / interactive / selected；信息密集内容改用平面表面。 | `adapted`, Medium, E-001, E-002, E-003, E-090, E-091 |
| 适用状态 | default、hover/focus（interactive）、pressed、selected、disabled、loading、error。 | `adapted`, Medium, E-001, E-002, E-003, E-090, E-091 |
| 内容与溢出 | 短而可扫描；长文、表格和多级表单不强制粘土化。 | `adapted`, Medium, E-001, E-002, E-003, E-090, E-091 |
| 鼠标、键盘与触控 | 整卡与内部操作避免嵌套；装饰图形不进入焦点顺序。 | `adapted`, Medium, E-001, E-002, E-003, E-090, E-091 |
| 响应式行为 | 小屏减少体积和装饰但保持内容；多列按最小宽度转单列。 | `adapted`, Medium, E-001, E-002, E-003, E-090, E-091 |
| 无障碍 | surface fill 是对比基准，阴影不计作文字背景；selected/error 兼用边界、图标和文字。 | `adapted`, Medium, E-001, E-002, E-003, E-090, E-091 |
| Tokens | component.card.*；semantic.color.surface/textPrimary/border。 | `adapted`, Medium, E-001, E-002, E-003, E-090, E-091 |
| 实现注意事项 | 同一屏限制主要圆角和阴影级别，避免每个元素都是不相关气泡。 | `adapted`, Medium, E-001, E-002, E-003, E-090, E-091 |

### Toggle / Selection

组件级 provenance：`status=adapted`；`confidence=medium`；`confidenceReason=来源支持风格或交互原则，结构和精确实现值是跨平台起始适配，尚无目标产品运行时证据。`；`evidenceIds=E-001,E-002,E-003,E-090,E-091`；`scope=Web 与移动端参考；浅色起始主题；键盘、指针、触控和辅助技术`；`method=公开规范归纳后进行独立项目适配`；`captured_at=2026-07-14T10:19:53+08:00`；`rationale=避免粘土阴影成为选择组件的唯一线索。`。

| 项目 | 规范 | 来源与证据 |
|---|---|---|
| 用途与边界 | 以实色位置、图标和语义状态表达选择，不只靠凹凸。 | `adapted`, Medium, E-001, E-002, E-003, E-090, E-091 |
| Anatomy | 轨道/容器、控制柄或选中图形、可见标签。 | `adapted`, Medium, E-001, E-002, E-003, E-090, E-091 |
| Variants 与 sizes | switch / checkbox / radio / selectable chip；按任务语义选择。 | `adapted`, Medium, E-001, E-002, E-003, E-090, E-091 |
| 适用状态 | off/on、unchecked/checked、hover、focus-visible、pressed、disabled、saving/error。 | `adapted`, Medium, E-001, E-002, E-003, E-090, E-091 |
| 内容与溢出 | 标签不省略；远程保存失败说明并回滚。 | `adapted`, Medium, E-001, E-002, E-003, E-090, E-091 |
| 鼠标、键盘与触控 | 点击标签和控件均激活；键盘按平台模型；状态立即反馈。 | `adapted`, Medium, E-001, E-002, E-003, E-090, E-091 |
| 响应式行为 | 标签可换行；控件不压缩到小于目标尺寸。 | `adapted`, Medium, E-001, E-002, E-003, E-090, E-091 |
| 无障碍 | checked/selected 程序化可读；accent fill + icon/check + 文本语义，非单一阴影。 | `adapted`, Medium, E-001, E-002, E-003, E-090, E-091 |
| Tokens | semantic.color.action/surfaceAlt/focus/danger；primitive.size.targetMin。 | `adapted`, Medium, E-001, E-002, E-003, E-090, E-091 |
| 实现注意事项 | 凹陷/凸起只补充状态，实色与符号承担主要可辨性。 | `adapted`, Medium, E-001, E-002, E-003, E-090, E-091 |

### Text Field

组件级 provenance：`status=adapted`；`confidence=medium`；`confidenceReason=来源支持风格或交互原则，结构和精确实现值是跨平台起始适配，尚无目标产品运行时证据。`；`evidenceIds=E-001,E-002,E-003,E-090,E-091`；`scope=Web 与移动端参考；浅色起始主题；键盘、指针、触控和辅助技术`；`method=公开规范归纳后进行独立项目适配`；`captured_at=2026-07-14T10:19:53+08:00`；`rationale=为高风险输入保留清晰边界和标签，不让拟态效果压过可用性。`。

| 项目 | 规范 | 来源与证据 |
|---|---|---|
| 用途与边界 | 在粘土页面中提供高可读、可修复的输入；不强求输入本体做厚重软体。 | `adapted`, Medium, E-001, E-002, E-003, E-090, E-091 |
| Anatomy | 永久标签、实色/轻凹输入面、值、帮助/错误和可选图标。 | `adapted`, Medium, E-001, E-002, E-003, E-090, E-091 |
| Variants 与 sizes | outlined 或轻 inset 二选一；多行按内容增长。 | `adapted`, Medium, E-001, E-002, E-003, E-090, E-091 |
| 适用状态 | default、focus-visible、filled、disabled、read-only、error、validating。 | `adapted`, Medium, E-001, E-002, E-003, E-090, E-091 |
| 内容与溢出 | placeholder 不代替标签；错误说明修复方式；长文可换行。 | `adapted`, Medium, E-001, E-002, E-003, E-090, E-091 |
| 鼠标、键盘与触控 | 标准文本编辑；清除/显隐按钮可访问；校验时机稳定。 | `adapted`, Medium, E-001, E-002, E-003, E-090, E-091 |
| 响应式行为 | 200% 文本或 400% zoom 时容器随内容增高，不固定高度截断。 | `adapted`, Medium, E-001, E-002, E-003, E-090, E-091 |
| 无障碍 | 边界与相邻表面至少 3:1；错误边界、图标和文字三重表达；focus 独立。 | `adapted`, Medium, E-001, E-002, E-003, E-090, E-091 |
| Tokens | component.input.*；semantic.color.border/focus/danger/textPrimary。 | `adapted`, Medium, E-001, E-002, E-003, E-090, E-091 |
| 实现注意事项 | 表单主体优先平面高可读，粘土感只在外层或操作区有限使用。 | `adapted`, Medium, E-001, E-002, E-003, E-090, E-091 |

## 10. 页面与流程

| 页面或流程 | 信息层级 | 布局与操作区 | 状态与异常路径 | 响应式行为 | 证据 |
|---|---|---|---|---|---|
| 轻量消费/教育页 | 主任务 → 轻量卡片 → 进度/下一步 | 主操作和关键摘要 clay 化，正文使用稳定实色面 | empty/loading/error/success 与进度 | 小屏减少体积和阴影层，保持目标尺寸 | E-001, E-003, E-090, adapted |
| 创意工具入口 | 品牌/任务 → 模板/分类 → 创建操作 | 少量粘土图标和卡片形成亲和表达 | 资源加载、失败、权限和恢复 | 多列按最小宽度重排；编辑主体保持高可读 | E-001, E-090, adapted |

## 11. 响应式与输入模态

- 以内容和任务触发行为变化：导航拥挤时改型、列宽不足时重排、操作过密时按优先级分层；阈值由目标项目记录。
- 触控界面不依赖 hover；精细指针的 hover 只加强默认可见线索。
- 交互目标起始值采用 44px；Web 合规仍须逐项核对 WCAG 2.2 的 24×24 CSS px 基线及例外。
- 200% 文本缩放与约 320 CSS px reflow 时，不丢失标签、错误、操作、当前状态与恢复路径。
- 使用逻辑方向属性；RTL 只镜像具有方向语义的布局和图标。
- 小屏减少阴影层数和装饰体积，保留主操作、标签与内容优先级。
- 圆角容器随内容增高；200% 文本和 400% zoom 不固定高度截断。

## 12. 主题、国际化与极端内容

- 浅色、深色和高对比主题分别映射 semantic token；不得直接反相颜色、阴影、图片或材质。
- 响应 prefers-color-scheme、prefers-contrast、forced-colors、prefers-reduced-motion；透明材质还应处理 prefers-reduced-transparency。
- 使用真实 CJK、拉丁长词、阿拉伯语 RTL、日期、数字、货币和 30%–50% 文案膨胀测试。
- 按钮与标签允许换行或自适应宽度，不通过缩小字号或无提示省略关键动作解决溢出。
- 深色 Clay 不能简单反相；highlight、shadow、surface 和 text 需独立生成并逐状态测量。
- forced-colors/high-contrast 下移除装饰阴影，改用系统实色、边界和焦点。

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
| 将 Clay 限制在低到中密度和高价值组件 | E-003, E-090 | 避免软体体积损害表单、表格和长文的扫描与对比。 | 组件和页面模板 | `adapted` |
| 阴影只表达体积，不承担边界、焦点或状态 | E-001, E-003, E-090 | 保证不同视觉能力和 forced-colors 下仍可操作。 | 全部交互组件 | `adapted` |

## 15. 冲突、未知项与后续材料

| 项目 | 当前证据或冲突 | 影响 | 所需最少材料 | 当前处理 |
|---|---|---|---|---|
| 目标项目与用户任务 | 未提供真实产品和关键流程 | 无法判断密度、组件数量和页面模板 | 产品范围、关键流程、用户与平台 | Draft |
| 真实 token 与组件状态 | 没有代码、设计文件或运行页面 | 推荐值无法视为实测 | 组件库版本、主题文件、代表性页面 | Adapted |
| 对比度与输入模态 | 只有规范目标，没有渲染结果 | 不能标记无障碍通过 | 各主题状态截图、键盘/读屏/触控测试 | Not tested |
| 风格软硬与目标年龄 | 没有品牌、受众和产品任务 | 无法确定体积强度和饱和度 | 品牌方向、目标年龄和用户测试 | Draft |
| 资产/性能方案 | 未确认纯 CSS 或 3D 插画 | 加载、渲染和授权未知 | 资产方案、性能预算和许可 | Draft |

### 反模式

- 宣称 pastel、24px 圆角或三层 shadow 是 Clay 官方标准。
- 全页面每个容器都做膨胀阴影。
- 把 Clay 与 Glass 混为透明模糊材质。
- 用凹凸阴影作为按钮、选中、焦点或错误的唯一线索。
- 深色模式直接把 highlight/shadow 反相，或持续果冻/3D tilt。

## 16. 实现与验收说明

- 开发只消费 `design-tokens.json`，不要在组件中另写同义颜色、尺寸或时长。
- 实现前先把目标产品的页面、组件、状态、主题和输入模态填入覆盖矩阵。
- 实现后执行 `design-review-checklist.md`；没有证据的项目保持 `Not tested`。
- Web 至少验证 320 CSS px reflow、200% 文本缩放、键盘全流程、读屏状态公告和 WCAG 2.2 AA 对比度。
- 视觉回归应覆盖默认、focus-visible、disabled、loading、empty、error、长文本、深色或高对比等适用状态。
- 若目标平台提供原生组件和主题能力，优先遵循对应平台规范；本包只定义风格层，不替代平台交互契约。
