# Design-standards
用于 AI Coding 的设计规范与开发规范 Skill 集合，帮助 AI 在开发过程中遵循指定主题风格、页面设计规则、技术栈工程规范与变更联动检查流程，减少页面反复调试成本，提升生成界面的视觉一致性、交互合理性与代码维护一致性。

## 已收录内容

### style-design-spec-skill

`style-design-spec-skill` 是一个用于“目标软件 / 网站 / Web 应用 / 桌面应用 / 移动应用 / 截图 / 录屏 / 代码 / 设计稿 / 明确风格参考”的设计规范提取 Skill。

它的作用不是简单生成一份泛化的美化建议，而是引导 AI 基于可验证证据提取设计规律，并把观察事实、推断结论和项目适配建议明确分开，形成可直接服务于 AI Coding、前端实现和设计验收的规范资产。

适用场景：

- 用户希望整理、提取、分析或生成某个软件、网站、应用或设计风格的设计规范。
- 用户希望把参考产品的视觉风格沉淀成可复用的设计规则。
- 用户需要从参考界面生成 `design-spec`、设计 tokens、组件规则或验收清单。
- 用户希望开发完成后有一份可执行的设计审核清单，用于检查页面尺寸、按钮大小、文字重叠、横向溢出、选中态 / hover 边框突兀等问题。

核心输出物：

- `design-spec.md`：完整设计规范，描述风格定位、视觉规则、组件规范、页面模板、交互规范和前端实现建议。
- `design-tokens.json`：面向代码实现的设计变量，沉淀颜色、字体、间距、圆角、阴影、边框、断点等 token。
- `design-review-checklist.md`：开发后的设计一致性检查清单，帮助验证实现结果是否符合规范。

当前结构：

- `SKILL.md`：Skill 主说明。
- `references/`：证据模型、Web 采集、设计文件采集、Native 采集、token 模型、组件模型和质量门禁等参考资料。
- `assets/`：设计规范模板、设计 token schema、审核模板和 AI Coding 提示词。
- `agents/`：面向 OpenAI/Codex 的 agent 元数据。
- `scripts/`：输出校验脚本与测试。

核心原则：

- 优先基于可验证证据，不把通用 UI 惯例包装成目标产品的真实规范。
- 明确区分 `measured`、`sampled`、`observed`、`inferred` 和 `adapted`。
- 不复制目标品牌的 Logo、商标、插画、文案或其他专有资产，只提取可迁移规律。
- 生成规范后，要继续用于页面设计、代码实现和设计审核闭环。

### development-guidelines-skills

`development-guidelines-skills` 是一个用于 AI Coding 项目开发的工程治理 Skill 套件。该目录是源码与分发仓库，不是单个 Skill；安装时会按 catalog 将各 Skill 目录平铺到 Codex Skills 目录。

它主要解决两个问题：一是新项目启动时缺少可执行约束，导致技术栈、目录、数据所有权、接口和测试策略各自为政；二是后续需求变更或问题修复时，AI 只改当前文件，遗漏契约、数据、调用方、迁移、测试、发布和回滚。

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

当前结构：

- `skill-catalog.json`：登记套件内 Skill、版本、触发关系和阶段性交接关系。
- `install_to_target.sh` / `install_to_target.ps1`：安装到 Codex Skills 目录的脚本。
- `scripts/`：套件校验、安装、输出评测和单元测试脚本。
- `evals/`：前向测试契约。
- 各 Skill 子目录下的 `references/`、`assets/`、`agents/`：分技术栈或工作流的补充规则、模板和 agent 元数据。

核心原则：

- 先定工程规范，再写业务代码。
- 先分析影响范围，再执行变更。
- 修改不能只停留在单个页面，必须同步数据源、类型、接口、组件、mock 和测试。
- 每次开发完成后都要做一致性检查和回归验证。
