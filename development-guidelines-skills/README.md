# 开发相关 Skill 套件

本套 Skill 用于解决 AI Coding 过程中常见的两个核心问题：

1. 项目开发之初没有规范，导致目录、数据源、组件、接口、状态管理各自为政。
2. 后续需求变更或问题修复时，AI 只修改当前页面，没有联动修改相关页面、组件、数据源、类型、mock、接口和测试。

## Skill 分类

| 分类 | Skill | 用途 |
|---|---|---|
| 1 | `ai-dev-tech-stack-orchestrator` | 根据项目目标判断应用类型、技术栈、语言、架构，并编排应启用的规范 Skill。 |
| 2 | 技术栈开发规范 Skill | 针对 React、Vue、Next.js、Electron、Flutter、FastAPI、Spring Boot 等技术栈生成具体开发规范。 |
| 3 | `change-impact-analysis` | 每次需求变更/问题修改前，先分析影响范围，避免单点修改。 |
| 4 | `data-consistency-regression-test` | 修改完成后检查数据源、页面、组件、接口、类型、mock、测试是否同步更新。 |

## 推荐使用流程

```text
用户提出项目目标
  ↓
ai-dev-tech-stack-orchestrator
判断项目类型、技术栈、架构、规范组合
  ↓
对应技术栈开发规范 Skill
生成项目目录、数据源、组件、接口、状态管理规范
  ↓
正式开发
  ↓
用户提出修改/问题/需求变更
  ↓
change-impact-analysis
先查影响范围，再统一修改
  ↓
data-consistency-regression-test
检查底层数据、相关页面、影响项是否同步
```

## 当前包含的技术栈开发规范 Skill

- `react-typescript-web-standard`
- `vue-typescript-web-standard`
- `nextjs-fullstack-standard`
- `electron-desktop-standard`
- `flutter-mobile-standard`
- `fastapi-backend-standard`
- `springboot-backend-standard`

后续可以继续扩展：

- `react-native-mobile-standard`
- `android-kotlin-standard`
- `ios-swift-standard`
- `tauri-desktop-standard`
- `dotnet-wpf-standard`
- `python-desktop-tool-standard`
- `ai-agent-project-standard`

## 使用建议

- 新项目启动时，先使用 `ai-dev-tech-stack-orchestrator`。
- 技术栈确定后，再启用对应技术栈开发规范 Skill。
- 任何需求变更、字段修改、接口调整、状态变更、页面问题修复，都必须触发 `change-impact-analysis`。
- 每次修改完成后，必须触发 `data-consistency-regression-test`。
