# Design-standards
用于 AI Coding 的设计规范与开发规范 Skill 集合，帮助 AI 在开发过程中遵循指定主题风格、页面设计规则、技术栈工程规范与变更联动检查流程，减少页面反复调试成本，提升生成界面的视觉一致性、交互合理性与代码维护一致性。

## 已收录内容

### style-design-spec-skill

`style-design-spec-skill` 是一个用于“目标软件 / 网站 / App / PC 客户端 / 设计风格”的设计规范采集与生成 Skill。

它的作用不是简单生成一份泛化的美化建议，而是引导 AI 基于真实页面、截图、交互状态、可观察布局和组件样式，整理出可直接服务于 AI Coding 与前端实现的设计规范。

适用场景：

- 用户希望整理、提取、分析或生成某个软件、网站、应用或设计风格的设计规范。
- 用户希望把参考产品的视觉风格沉淀成可复用的设计规则。
- 用户需要为后续页面开发生成明确的颜色、字体、间距、圆角、组件、交互与响应式规范。
- 用户希望开发完成后有一份可执行的设计审核清单，用于检查页面尺寸、按钮大小、文字重叠、横向溢出、选中态 / hover 边框突兀等问题。

核心输出物：

- `design-spec.md`：完整设计规范，描述风格定位、视觉规则、组件规范、页面模板、交互规范和前端实现建议。
- `design-tokens.md`：面向代码实现的设计变量，沉淀颜色、字体、间距、圆角、阴影、边框、断点等 token。
- `design-review-checklist.md`：开发后的设计一致性检查清单，帮助验证实现结果是否符合规范。

核心原则：

- 优先基于真实采集结果，不把主观猜测写成确定事实。
- 明确区分“真实采集结论”“观察估算值”和“适配建议”。
- 生成规范后，要继续用于页面设计、代码实现和设计审核闭环。

### development-guidelines-skills

`development-guidelines-skills` 是一个用于 AI Coding 项目开发的开发规范 Skill 套件。

它主要解决两个问题：一是新项目启动时缺少统一工程规范，导致目录结构、数据源、组件、接口、状态管理、类型定义各自为政；二是后续需求变更或问题修复时，AI 只改当前页面，没有同步修改相关页面、组件、数据源、类型、mock、接口和测试。

适用场景：

- 新项目启动前，需要根据项目目标判断应用类型、技术栈、语言、架构和应启用的规范组合。
- React、Vue、Next.js、Electron、Flutter、FastAPI、Spring Boot 等项目需要生成统一开发规范。
- 用户提出字段调整、接口调整、状态变更、页面展示修改、问题修复或功能优化时，需要先做影响范围分析。
- 修改完成后，需要检查底层数据源、页面展示、组件引用、接口字段、类型定义、mock 数据、测试用例和导出逻辑是否同步更新。

当前包含的 Skill：

- `ai-dev-tech-stack-orchestrator`：根据项目目标判断应用类型、技术栈、语言、架构，并编排应启用的规范 Skill。
- `react-typescript-web-standard`：React + TypeScript Web 应用开发规范。
- `vue-typescript-web-standard`：Vue + TypeScript Web 应用开发规范。
- `nextjs-fullstack-standard`：Next.js + TypeScript 全栈应用开发规范。
- `electron-desktop-standard`：Electron 桌面 PC 软件开发规范。
- `flutter-mobile-standard`：Flutter 移动端应用开发规范。
- `fastapi-backend-standard`：Python FastAPI 后端服务开发规范。
- `springboot-backend-standard`：Java Spring Boot 后端服务开发规范。
- `change-impact-analysis`：需求变更与问题修改前的影响面分析。
- `data-consistency-regression-test`：修改完成后的数据一致性与回归测试检查。

推荐使用流程：

1. 新项目启动时，先使用 `ai-dev-tech-stack-orchestrator` 判断技术栈和规范组合。
2. 技术栈确定后，启用对应的技术栈开发规范 Skill，生成目录结构、数据源、组件、接口、状态管理和测试规范。
3. 正式开发过程中，任何需求变更、字段修改、接口调整、状态变更或页面问题修复，都先触发 `change-impact-analysis`。
4. 修改完成后，触发 `data-consistency-regression-test`，检查相关页面、底层数据、类型、mock、接口和测试是否同步。

核心原则：

- 先定工程规范，再写业务代码。
- 先分析影响范围，再执行变更。
- 修改不能只停留在单个页面，必须同步数据源、类型、接口、组件、mock 和测试。
- 每次开发完成后都要做一致性检查和回归验证。
