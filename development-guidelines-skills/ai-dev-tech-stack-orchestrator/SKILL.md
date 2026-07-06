---
name: ai-dev-tech-stack-orchestrator
description: 根据用户项目目标、应用类型、运行端、复杂度、开发周期和维护要求，推荐合适的开发语言、技术框架、应用架构，并编排应启用的开发规范 Skill。适用于新项目启动、技术选型、项目初始化前的 AI Coding 规划。
---

# AI 开发技术选型与规范编排 Skill

## 目标

在项目开发之初，先判断项目适合采用哪种开发语言、技术框架和应用架构，并输出应启用的开发规范组合，避免项目一开始就出现目录混乱、数据源分散、组件重复开发、接口无统一封装、后续修改无法联动的问题。

本 Skill 不是直接写业务代码，而是负责：

1. 判断项目类型。
2. 推荐技术栈。
3. 推荐应用架构。
4. 选择需要启用的开发规范 Skill。
5. 生成项目初始化前的约束说明。

## 触发场景

当用户提出以下需求时触发：

- 我要开发一个 Web 应用。
- 我要做一个移动端 App。
- 我要做一个桌面 PC 软件。
- 我要做一个后台管理系统。
- 我要做一个企业级系统。
- 我要做一个 AI 工具 / AI Agent / AI Coding 项目。
- 帮我判断这个项目适合用什么技术栈。
- 这个项目用 React、Vue、Flutter、Electron、Python、Java 哪个更合适？
- 项目开始前，帮我生成开发规范。

## 输入信息收集

如果用户已经提供足够信息，直接判断；如果信息不足，优先基于已有内容做合理假设，不要过度追问。

需要识别的信息包括：

```text
1. 项目目标：要解决什么问题？
2. 应用类型：Web / App / 桌面端 / 后端服务 / AI Agent / 小程序。
3. 目标用户：个人、企业内部、客户、运维人员、普通用户。
4. 复杂度：Demo / MVP / 中大型系统 / 长期维护项目。
5. 运行端：浏览器、iOS、Android、Windows、macOS、Linux、服务端。
6. 数据特征：是否有大量表格、图表、文件、本地存储、实时通信、AI 调用。
7. 团队能力：是否偏前端、后端、全栈、Python、Java、JS/TS。
8. 开发周期：短期验证还是长期产品化。
9. 部署方式：云端部署、本地部署、内网部署、单机运行。
10. 是否需要跨端：Web + App、Web + 桌面端、移动端双平台。
```

## 技术选型判断规则

### Web 管理后台 / 企业系统

优先推荐：

```text
React + TypeScript + Vite + Ant Design / shadcn/ui
Vue + TypeScript + Vite + Element Plus / Arco Design
Next.js + TypeScript
```

适用场景：

- OA 系统
- 管理后台
- 数据看板
- 业务流程系统
- 表格、筛选、详情、权限较多的系统

推荐启用：

```text
react-typescript-web-standard 或 vue-typescript-web-standard
change-impact-analysis
data-consistency-regression-test
```

### 官网 / 内容站 / SEO 页面

优先推荐：

```text
Next.js + TypeScript
Astro
Nuxt
```

适用场景：

- 官网
- 文档站
- 产品介绍页
- 内容营销页面
- 需要 SEO 的站点

推荐启用：

```text
nextjs-fullstack-standard
change-impact-analysis
data-consistency-regression-test
```

### 移动端 App

优先推荐：

```text
Flutter
React Native
原生 Android Kotlin
原生 iOS Swift
```

选择规则：

```text
1. 需要快速跨 iOS/Android：Flutter 或 React Native。
2. 强依赖系统能力、性能和平台体验：原生 Kotlin / Swift。
3. 团队偏前端：React Native。
4. 追求较稳定跨端 UI：Flutter。
```

推荐启用：

```text
flutter-mobile-standard
change-impact-analysis
data-consistency-regression-test
```

### 桌面 PC 软件

优先推荐：

```text
Electron + React/Vue + TypeScript
Tauri + Rust + Web 前端
Qt + C++/Python
C# WPF / WinUI
```

选择规则：

```text
1. 需要快速开发跨平台桌面端：Electron。
2. 追求轻量安装包和安全隔离：Tauri。
3. 强图形、底层能力、跨平台工具：Qt。
4. Windows 企业桌面软件：C# WPF / WinUI。
```

推荐启用：

```text
electron-desktop-standard
change-impact-analysis
data-consistency-regression-test
```

### 后端服务 / API 服务

优先推荐：

```text
Python FastAPI
Java Spring Boot
Node.js NestJS
Go Gin/Fiber
```

选择规则：

```text
1. AI 应用、数据处理、原型快：FastAPI。
2. 企业级复杂后端、权限、事务、稳定性：Spring Boot。
3. 前端团队全栈开发：NestJS。
4. 高性能服务、部署轻量：Go。
```

推荐启用：

```text
fastapi-backend-standard 或 springboot-backend-standard
change-impact-analysis
data-consistency-regression-test
```

## 输出格式

每次执行时，必须输出以下内容：

```text
1. 项目类型判断
2. 推荐技术栈
3. 推荐应用架构
4. 选择原因
5. 不推荐方案及原因
6. 应启用的开发规范 Skill
7. 项目初始化时必须生成的规范文件
8. 后续需求变更时必须触发的检查 Skill
```

## 标准输出模板

```markdown
# 技术选型与规范编排结果

## 1. 项目类型判断
- 应用类型：
- 运行端：
- 复杂度：
- 维护周期：

## 2. 推荐技术栈
- 前端/客户端：
- 后端：
- 数据库：
- 状态管理：
- UI 组件库：
- 构建/部署：

## 3. 推荐架构
- 架构类型：
- 模块划分方式：
- 数据源管理方式：
- 接口管理方式：

## 4. 推荐原因

## 5. 不推荐方案

## 6. 应启用的 Skill
- 技术栈开发规范 Skill：
- 需求变更影响分析 Skill：change-impact-analysis
- 数据一致性与回归测试 Skill：data-consistency-regression-test

## 7. 项目初始化必须生成的规范文件
- docs/development-standard.md
- docs/data-source-standard.md
- docs/change-impact-standard.md
- docs/regression-test-checklist.md
- AGENTS.md
```

## 强制约束

1. 不要只推荐技术栈，必须同时给出规范组合。
2. 不要只关注开发速度，也要考虑后续维护、数据一致性、跨页面联动修改。
3. 如果项目涉及多个页面共享数据，必须启用数据源统一和变更影响分析规则。
4. 如果是 AI Coding 场景，必须生成 `AGENTS.md` 或等价的 AI 执行规则文件。
5. 技术选型完成后，必须提醒后续开发不能直接开始写页面，应先生成项目开发规范。
