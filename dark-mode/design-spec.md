# 暗黑模式设计规范

> 本文是面向独立产品的可迁移规范，不复制目标品牌的 Logo、商标、专有图标、插画或文案。所有精确起始值均以 `adapted` 标注，不代表目标品牌的内部 token。

## 1. 文档状态

| 字段 | 内容 |
|---|---|
| 状态 | `draft` |
| 目标对象 | 跨平台 Dark Mode 主题规范 |
| 平台与版本 | Apple/Android/Windows/Web 当前公开主题能力；采集于 2026-07-14 |
| 目标项目 | 用于 AI Coding 的跨平台风格实施包 |
| 采集日期 | 2026-07-14 |
| 主题、语言与地区 | dark 为主；必须与 light、high-contrast/forced-colors 共同定义；全球多语言 |
| 负责人 | Codex（证据整理）/ 项目团队（落地验证） |

状态为 `draft` 的原因：本轮以公开文档和设计研究为证据，没有指定目标应用、运行时页面、组件库或可测设计文件，因此不能把推荐值标成 `measured` 或把实现质量标成已验证。

## 2. 范围与限制

### 已覆盖

- 公开材料中的风格定位、原则和使用边界（E-001、E-002、E-003、E-004、E-005）。
- 面向独立项目的颜色、排版、间距、形状、层级、动效与语义 token 起始方案。
- 代表性组件：按钮 / Action、输入框 / Field、卡片 / Surface、导航 / Selection、主题选择器。
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
| E-001 | [Apple HIG — Dark Mode](https://developer.apple.com/design/human-interface-guidelines/dark-mode) | 暗色应尊重系统外观，明暗不是简单反相，语义色、base/elevated 表面、图像和图标需分别验证。 | Apple 平台官方设计指南 | Document | 读取公开页面并记录可复查结论 | 2026-07-14T10:19:53+08:00 | Apple 系统色与组件行为不能直接证明 Web/Android 数值。 |
| E-002 | [Android Developers — Implement dark theme](https://developer.android.com/develop/ui/views/theming/darktheme) | Android 10+ 支持系统暗色；应用应使用 DayNight/主题属性并避免硬编码浅色颜色和图标。 | Android 官方实现指南 | Document | 读取公开页面并记录可复查结论 | 2026-07-14T10:19:53+08:00 | Views 示例不覆盖 Compose、Web 或全部设计细节。 |
| E-003 | [W3C — CSS Color Adjustment Module Level 1](https://www.w3.org/TR/css-color-adjust-1/) | color-scheme 可让用户代理控件、滚动条和表单元素参与明暗颜色协商。 | W3C Candidate Recommendation Snapshot；Web | Document | 读取公开页面并记录可复查结论 | 2026-07-14T10:19:53+08:00 | 自定义内容仍需作者主题和兼容性验证。 |
| E-004 | [W3C — Media Queries Level 5](https://www.w3.org/TR/mediaqueries-5/) | prefers-color-scheme、forced-colors、prefers-contrast 等表达用户外观偏好。 | W3C Working Draft；Web | Document | 读取公开页面并记录可复查结论 | 2026-07-14T10:19:53+08:00 | 支持度与平台 API 需按目标浏览器核对。 |
| E-005 | [Windows — Color](https://learn.microsoft.com/en-us/windows/apps/design/signature-experiences/color) | Windows 设计使用明暗模式与中性色层级，并要求主题化颜色角色。 | Microsoft Windows 设计指南 | Document | 读取公开页面并记录可复查结论 | 2026-07-14T10:19:53+08:00 | Windows 资源值不应当作通用跨平台 token。 |
| E-090 | [W3C — Web Content Accessibility Guidelines (WCAG) 2.2](https://www.w3.org/TR/WCAG22/) | WCAG 2.2 规定文本/非文本对比、可见焦点、reflow、目标尺寸、颜色之外的状态线索等可验收基线。 | W3C Recommendation；Web；通用主题与输入模态 | Document | 读取公开页面并记录可复查结论 | 2026-07-14T10:19:53+08:00 | 不替代 Android、HarmonyOS、iOS 或桌面平台的额外要求。 |
| E-091 | [W3C — Media Queries Level 5](https://www.w3.org/TR/mediaqueries-5/) | Web 可查询 prefers-reduced-motion、prefers-reduced-transparency、prefers-contrast、forced-colors 与 prefers-color-scheme 等用户偏好。 | W3C Working Draft；Web 用户偏好媒体特性 | Document | 读取公开页面并记录可复查结论 | 2026-07-14T10:19:53+08:00 | 浏览器支持度与原生平台 API 需要在目标技术栈中另行确认。 |

证据类型与置信度分开：上表只说明来源；正文每条规则另行标注 `observed`、`inferred` 或 `adapted` 与置信度。

## 4. 覆盖矩阵

| 页面或流程 | 组件 | 状态 | 主题 | 视口或输入模态 | 覆盖状态 | 证据 |
|---|---|---|---|---|---|---|
| 公开设计语言/研究 | 原则与基础层 | 文档声明 | 文档涉及范围 | 公开网页 | Covered | E-001、E-002、E-003、E-004、E-005 |
| 跨平台起始包 | 按钮 / Action、输入框 / Field、卡片 / Surface、导航 / Selection、主题选择器 | default / focus / disabled / loading / error 等适用状态 | 默认起始主题 | Web、键盘、指针、触控参考 | Partial | E-001、E-002、E-003、E-004、E-005, E-090, E-091 |
| 真实产品流程 | 目标项目组件 | 全部运行态 | 实际深浅/高对比主题 | 真实设备与视口 | Missing | 无 |

## 5. 设计定位

暗黑模式是跨平台外观模式，不是独立品牌，也没有统一固定色板。正确实现需要系统主题协商、semantic token、暗色表面层级、媒体资产、浏览器原生控件、高对比/强制颜色和运行时切换；它不是把浅色页面简单反相。

| 规则 | 可观察/可验收表现 | 来源类型 | 置信度 | 证据 |
|---|---|---|---|---|
| 系统协商 | 默认跟随系统，显式用户选择可覆盖并可回到 system。 | `observed` | High | E-001, E-002, E-003, E-004 |
| 语义重映射 | background/surface/text/action/error/outline/focus 在 light/dark 中分别映射，不逐色反相。 | `inferred` | High | E-001, E-002, E-005 |
| 色调层级 | 暗色表面用更亮的 elevated surface、outline 或色调差异表达海拔，阴影为补充。 | `observed` | High | E-001, E-005 |
| 完整覆盖 | 页面、overlay、系统栏、表单控件、滚动条、图表、代码高亮、图片和 iframe 分别验证。 | `inferred` | High | E-002, E-003 |

### 适用场景

- 几乎所有需要低光环境、系统个性化或长时使用的产品。
- 内容、工具、媒体、开发者、车载和设备应用的可选主题。
- 已经建立 semantic token 并能完整测试组件状态和第三方内容的团队。

### 不宜直接套用

- 把暗黑模式当作纯黑品牌风格并移除浅色/系统选项。
- 仅修改 body 背景，遗漏表单、滚动条、图表、代码高亮和 overlay。
- 无法控制动态背景或媒体对比却叠放低透明文字的界面。

## 6. 设计原则

| 原则 | 可执行规则 | 例外 | 来源与置信度 |
|---|---|---|---|
| 尊重偏好 | 首次默认跟随系统；切换可在运行中发生并保持任务状态。 | 媒体创作等特殊场景可提供应用级覆盖，但不能移除 system 选项。 | `observed`, High, E-001, E-002, E-004 |
| 不是反相 | 为前景、表面、图标、状态和媒体分别设计暗色角色。 | 黑白品牌标志需使用获批版本，不用 CSS invert。 | `observed`, High, E-001 |
| 层级可辨 | 使用 surface tone、outline 和必要阴影区分 base/elevated。 | OLED 场景可在局部使用纯黑，但不能抹平全部层级。 | `observed`, High, E-001, E-005 |
| 切换不跳动 | 明暗主题保持布局、字号、间距、形状和目标尺寸一致。 | 仅图像比例或媒体素材本身需要替换时可变化。 | `inferred`, High, E-001 |

## 7. 基础系统

以下精确值是独立项目起始值，统一为 `adapted / medium`。采用理由：以系统主题协商和语义色重映射为核心，使用多级 near-black 表面建立层级；所有具体颜色均需在目标品牌与状态中复测。

### 7.1 色彩

| 角色 | 起始值 | 用途 | 主题与状态 | Token | 来源与理由 |
|---|---|---|---|---|---|
| 画布 | `#0F1115` | 页面最底层 | 默认 | `semantic.color.background` | `adapted`, E-001, E-002, E-003, E-004, E-090；落地前按真实前景/背景复测对比度 |
| 表面 | `#20242D` | 卡片、面板、输入背景 | 默认 | `semantic.color.surface` | `adapted`, E-001, E-002, E-003, E-004, E-090；落地前按真实前景/背景复测对比度 |
| 次级表面 | `#2A303B` | 弱分区与选中底 | 默认 | `semantic.color.surfaceAlt` | `adapted`, E-001, E-002, E-003, E-004, E-090；落地前按真实前景/背景复测对比度 |
| 主要文本 | `#F3F4F6` | 标题与正文 | 默认 | `semantic.color.textPrimary` | `adapted`, E-001, E-002, E-003, E-004, E-090；落地前按真实前景/背景复测对比度 |
| 次级文本 | `#B7BDC8` | 说明与元数据 | 默认 | `semantic.color.textSecondary` | `adapted`, E-001, E-002, E-003, E-004, E-090；落地前按真实前景/背景复测对比度 |
| 必要边界 | `#8A93A1` | 组件识别与分组 | 默认 | `semantic.color.border` | `adapted`, E-001, E-002, E-003, E-004, E-090；落地前按真实前景/背景复测对比度 |
| 主要操作 | `#8AB4F8` | CTA、激活状态 | 默认/selected | `semantic.color.action` | `adapted`, E-001, E-002, E-003, E-004, E-090；落地前按真实前景/背景复测对比度 |
| 操作上内容 | `#0A2540` | 主要操作上的文字与图标 | 默认 | `semantic.color.onAction` | `adapted`, E-001, E-002, E-003, E-004, E-090；落地前按真实前景/背景复测对比度 |
| 焦点 | `#A8C7FA` | 键盘焦点轮廓 | focus-visible | `semantic.color.focus` | `adapted`, E-001, E-002, E-003, E-004, E-090；落地前按真实前景/背景复测对比度 |
| 成功 | `#81C995` | 成功反馈 | success | `semantic.color.success` | `adapted`, E-001, E-002, E-003, E-004, E-090；落地前按真实前景/背景复测对比度 |
| 警告 | `#FDD663` | 警告反馈 | warning | `semantic.color.warning` | `adapted`, E-001, E-002, E-003, E-004, E-090；落地前按真实前景/背景复测对比度 |
| 危险 | `#F28B82` | 错误与破坏性操作 | error/danger | `semantic.color.danger` | `adapted`, E-001, E-002, E-003, E-004, E-090；落地前按真实前景/背景复测对比度 |

规则：语义色必须通过 token 映射；成功、警告、错误和选中不得只靠颜色表达；品牌来源中的专有色只用于分析，不应被独立产品直接当作自身品牌资产。

### 7.2 字体与内容密度

| 角色 | 字体 | 字号 / 行高 | 字重 | 内容规则 | 来源与证据 |
|---|---|---|---|---|---|
| 辅助 | Inter / Noto Sans SC / system-ui / sans-serif | `14px` / `20px` | 400–500 | 标签、元数据和帮助文字；不可承载唯一关键信息 | `adapted`, E-001, E-002, E-003, E-004, E-090 |
| 正文 | Inter / Noto Sans SC / system-ui / sans-serif | `16px` / `24px` | 400 | 默认正文与常规控件 | `adapted`, E-001, E-002, E-003, E-004, E-090 |
| 模块标题 | Inter / Noto Sans SC / system-ui / sans-serif | `24px` / `32px` | 600 | 卡片或页面分区标题 | `adapted`, E-001, E-002, E-003, E-004, E-090 |
| 展示标题 | Inter / Noto Sans SC / system-ui / sans-serif | `40px` / `48px` | 600–700 | 低频关键标题，窄屏需流体缩放 | `adapted`, E-001, E-002, E-003, E-004, E-090 |

暗色主题沿用主设计系统排版；不通过缩小字号或低透明度解决层级。必要时在小字号提高字重，但仍以实际合成对比和清晰度为准。

### 7.3 布局、网格与间距

| 场景 | 行为规则 | 起始值或范围 | 来源类型 | 置信度 | 证据 |
|---|---|---|---|---|---|
| 主题一致性 | 明暗切换不改变几何、间距、字号和布局。 | `与 light 共用 layout/shape tokens` | `adapted` | Medium | E-001, E-002, E-003, E-004, E-090 |
| 表面层级 | base、surface、surface-high 至少有可辨色调差。 | `#0F1115 / #20242D / #2A303B 起始示例` | `adapted` | Medium | E-001, E-002, E-003, E-004, E-090 |
| 内容宽度 | 与主设计系统一致，暗色不无限加大字距或行距。 | `继承主体系` | `adapted` | Medium | E-001, E-002, E-003, E-004, E-090 |
| 主题加载 | 尽早声明 color-scheme 和主题属性，减少白屏闪烁。 | `在首屏 CSS/原生主题初始化前完成` | `adapted` | Medium | E-001, E-002, E-003, E-004, E-090 |

不得把建议断点写成已观察断点。先以内容溢出、最小列宽、任务优先级和输入模态确定行为边界，再为工程实现记录断点。

### 7.4 形状、边框、层级与阴影

| 角色 | 规则 | 起始值 | Token | 来源与证据 |
|---|---|---|---|---|
| 控件圆角 | 形状继承主体系；暗黑模式不另造几何。 | `8px` | `semantic.shape.control` | `adapted`, E-001, E-002, E-003, E-004, E-090 |
| 容器圆角 | surface tone 分层，容器半径与 light 保持一致。 | `12px` | `semantic.shape.container` | `adapted`, E-001, E-002, E-003, E-004, E-090 |
| 默认边界 | 必要边界在实际相邻暗色表面上达到可识别对比。 | `1px` | `primitive.stroke.thin` | `adapted`, E-001, E-002, E-003, E-004, E-090 |
| 静止表面 | 阴影在暗背景上只能补充层级。 | `0 1px 2px rgb(0 0 0 / 32%)` | `primitive.effect.shadowRest` | `adapted`, E-001, E-002, E-003, E-004, E-090 |
| 抬升表面 | 抬升以更亮 surface 与 outline 为主，阴影为辅。 | `0 12px 32px rgb(0 0 0 / 48%)` | `primitive.effect.shadowRaised` | `adapted`, E-001, E-002, E-003, E-004, E-090 |

### 7.5 图标、图像与品牌资产

- 图片、插画、图标、地图、图表和代码高亮分别提供暗色版本或安全衬底。
- 品牌标志不能自动反相；使用品牌授权的 light/dark 资产。
- 用户内容不应被全局滤镜改色；对亮白图片可使用边界、衬底或查看器策略。

### 7.6 动效

| 场景 | 属性 | 起始时长与曲线 | 减弱动效行为 | 来源与证据 |
|---|---|---|---|---|
| 主题切换 | 颜色/表面短淡变 | `120–200ms` | 直接切换或极短淡变 | `adapted`, E-001, E-004 |
| 控件状态 | 沿用主体系 motion | `100–160ms` | 保留即时状态 | `adapted`, E-002, E-091 |
| 媒体替换 | 交叉淡化（适用时） | `≤200ms` | 直接替换并避免白闪 | `adapted`, E-001, E-091 |

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
| 实现注意事项 | 几何、密度和布局继承产品主体系；暗黑模式只重映射语义颜色、图像和层级；主色在暗背景上重新调整明度/饱和度，不能直接复用 light hex | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |

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
| 实现注意事项 | 几何、密度和布局继承产品主体系；暗黑模式只重映射语义颜色、图像和层级；不得用表面效果削弱文本与边界。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |

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
| 实现注意事项 | 几何、密度和布局继承产品主体系；暗黑模式只重映射语义颜色、图像和层级；用 surface tone 与必要 outline 区分层级，黑色阴影只作补充 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |

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
| 实现注意事项 | 几何、密度和布局继承产品主体系；暗黑模式只重映射语义颜色、图像和层级；selected、focus、hover、disabled 分别验证，不能只靠亮度微差 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |

### 主题选择器

组件级 provenance：`status=adapted`；`confidence=medium`；`confidenceReason=来源支持风格或交互原则，结构和精确实现值是跨平台起始适配，尚无目标产品运行时证据。`；`evidenceIds=E-001,E-002,E-003,E-004,E-005,E-090,E-091`；`scope=Web 与移动端参考；浅色起始主题；键盘、指针、触控和辅助技术`；`method=公开规范归纳后进行独立项目适配`；`captured_at=2026-07-14T10:19:53+08:00`；`rationale=把系统主题协商和用户控制转为可验收设置组件。`。

| 项目 | 规范 | 来源与证据 |
|---|---|---|
| 用途与边界 | 允许跟随系统、浅色或深色，并让用户随时回到系统偏好。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| Anatomy | 标签、当前值、三种选择；说明或预览按产品需要。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| Variants 与 sizes | segmented control / radio group / select；选择一种符合平台模式。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| 适用状态 | system、light、dark、focus-visible、disabled；saving/error（跨设备同步时）。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| 内容与溢出 | 使用“跟随系统 / 浅色 / 深色”等可理解标签，不用仅图标。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| 鼠标、键盘与触控 | 选择立即生效或明确保存；键盘/读屏可操作；系统变化时更新 system 模式。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| 响应式行为 | 窄屏可改为 radio/list，不截断标签。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| 无障碍 | 单选组名称和 checked 状态可读；切换不移动焦点或造成眩光闪烁。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| Tokens | semantic.color.*；semantic.motion.state。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |
| 实现注意事项 | 用户显式选择可覆盖系统，但必须提供返回‘跟随系统’。 | `adapted`, Medium, E-001, E-002, E-003, E-004, E-005, E-090, E-091 |

## 10. 页面与流程

| 页面或流程 | 信息层级 | 布局与操作区 | 状态与异常路径 | 响应式行为 | 证据 |
|---|---|---|---|---|---|
| 应用页面 | 全局导航 → 页面内容 → overlay/反馈 | 所有层和系统区域使用语义暗色角色 | loading/empty/error/offline 与组件全状态 | 信息结构与 light 相同；窄屏和软键盘复测 | E-001, E-002, E-003, adapted |
| 数据/媒体页 | 主内容 → 控制 → 元数据/图表 | 内容优先；surface tone 与 outline 建层级 | 图表无数据、图片白底、视频控制和错误 | 图表/媒体自适应，控制不被安全区遮挡 | E-001, E-005, E-090, adapted |

## 11. 响应式与输入模态

- 以内容和任务触发行为变化：导航拥挤时改型、列宽不足时重排、操作过密时按优先级分层；阈值由目标项目记录。
- 触控界面不依赖 hover；精细指针的 hover 只加强默认可见线索。
- 交互目标起始值采用 44px；Web 合规仍须逐项核对 WCAG 2.2 的 24×24 CSS px 基线及例外。
- 200% 文本缩放与约 320 CSS px reflow 时，不丢失标签、错误、操作、当前状态与恢复路径。
- 使用逻辑方向属性；RTL 只镜像具有方向语义的布局和图标。
- 暗黑模式不改变信息结构；窄屏、高缩放、软键盘和安全区必须分别复测。
- 系统主题可能在应用运行中切换，保留滚动、输入、选择和媒体进度。

## 12. 主题、国际化与极端内容

- 浅色、深色和高对比主题分别映射 semantic token；不得直接反相颜色、阴影、图片或材质。
- 响应 prefers-color-scheme、prefers-contrast、forced-colors、prefers-reduced-motion；透明材质还应处理 prefers-reduced-transparency。
- 使用真实 CJK、拉丁长词、阿拉伯语 RTL、日期、数字、货币和 30%–50% 文案膨胀测试。
- 按钮与标签允许换行或自适应宽度，不通过缩小字号或无提示省略关键动作解决溢出。
- Web 使用 color-scheme 与 prefers-color-scheme，同时支持用户属性覆盖；强制颜色模式使用系统色。
- 分别测试 Increase Contrast、Reduce Transparency、forced-colors、200% 文本和 400% zoom。

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
| 使用独立项目色盘，不直接复制品牌或案例颜色 | E-001, E-002, E-003, E-004, E-090 | 保留风格规律，同时避免品牌混淆并满足具体内容对比度。 | 全部颜色与主题 | `adapted` |
| 采用 primitive → semantic → component 三层 token | E-001, E-002, E-003, E-004, E-090, E-090 | 支持主题、状态和平台映射，避免组件硬编码。 | design-tokens.json 与全部组件 | `adapted` |
| 使用 near-black 多级表面而非全页面纯黑 | E-001, E-005, E-090 | 保持层级和可读性，并避免只依赖阴影。 | 背景、表面和 overlay | `adapted` |
| 主题切换保留 system/light/dark 三态 | E-001, E-002, E-004 | 尊重系统与用户显式偏好并允许恢复。 | 主题设置与初始化 | `adapted` |

## 15. 冲突、未知项与后续材料

| 项目 | 当前证据或冲突 | 影响 | 所需最少材料 | 当前处理 |
|---|---|---|---|---|
| 目标项目与用户任务 | 未提供真实产品和关键流程 | 无法判断密度、组件数量和页面模板 | 产品范围、关键流程、用户与平台 | Draft |
| 真实 token 与组件状态 | 没有代码、设计文件或运行页面 | 推荐值无法视为实测 | 组件库版本、主题文件、代表性页面 | Adapted |
| 对比度与输入模态 | 只有规范目标，没有渲染结果 | 不能标记无障碍通过 | 各主题状态截图、键盘/读屏/触控测试 | Not tested |
| 品牌暗色角色 | 未提供 light 品牌色和真实背景组合 | 无法确认 accent 与状态色对比 | 品牌主题、组件状态截图和对比度报告 | Adapted |
| 目标平台主题 API | 未指定 Web/Android/iOS/Windows | 系统控件和存储策略未知 | 技术栈、最低版本和浏览器矩阵 | Draft |

### 反模式

- 用 filter: invert(1) 全页反相。
- 全部表面纯黑且层级只靠黑色阴影。
- 直接复用 light accent，导致荧光刺眼或对比不足。
- 只改页面背景，遗漏表单控件、滚动条、iframe、图表和代码高亮。
- 强制 dark-only 且不给系统/用户偏好留余地。

## 16. 实现与验收说明

- 开发只消费 `design-tokens.json`，不要在组件中另写同义颜色、尺寸或时长。
- 实现前先把目标产品的页面、组件、状态、主题和输入模态填入覆盖矩阵。
- 实现后执行 `design-review-checklist.md`；没有证据的项目保持 `Not tested`。
- Web 至少验证 320 CSS px reflow、200% 文本缩放、键盘全流程、读屏状态公告和 WCAG 2.2 AA 对比度。
- 视觉回归应覆盖默认、focus-visible、disabled、loading、empty、error、长文本、深色或高对比等适用状态。
- 若目标平台提供原生组件和主题能力，优先遵循对应平台规范；本包只定义风格层，不替代平台交互契约。
