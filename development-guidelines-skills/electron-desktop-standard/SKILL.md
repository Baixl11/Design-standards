---
name: electron-desktop-standard
description: Electron 桌面 PC 软件开发规范 Skill。用于约束 Electron 主进程、渲染进程、IPC 通信、本地文件、窗口管理、自动更新、安全隔离、统一数据源和 AI Coding 修改规则。
---

# Electron 桌面软件开发规范 Skill

## 适用场景

适用于：

- Electron 桌面端软件
- Windows / macOS / Linux 跨平台工具
- 本地文件处理工具
- 企业桌面客户端
- Web 技术栈封装的桌面应用

## 推荐技术组合

```text
Electron + TypeScript
渲染层：React / Vue
构建：electron-vite / electron-builder
状态管理：Zustand / Pinia / Redux Toolkit
本地数据库：SQLite / IndexedDB
自动更新：electron-updater
日志：electron-log
测试：Vitest + Playwright
```

## 推荐目录结构

```text
src/
  main/
    index.ts
    windows/
    ipc/
    services/
    file-system/
    updater/
  preload/
    index.ts
    api.ts
  renderer/
    app/
    pages/
    features/
    shared/
  shared/
    types/
    constants/
    schemas/
```

## 主进程 / 渲染进程边界

```text
1. 主进程负责窗口、系统能力、本地文件、自动更新、托盘、菜单。
2. 渲染进程负责 UI 展示和用户交互。
3. 渲染进程不得直接访问 Node.js 系统能力。
4. 所有系统能力必须通过 preload 暴露安全 API。
5. IPC 通信必须有统一通道命名和类型定义。
```

## IPC 规范

```text
1. IPC 通道统一定义在 shared/constants/ipc.ts。
2. IPC 请求参数和返回值统一定义在 shared/types。
3. 主进程 handler 放 main/ipc。
4. 渲染进程调用封装在 renderer/shared/services。
5. 修改 IPC 参数时必须同步主进程、preload、渲染层、类型和测试。
```

## 本地文件与数据库规范

```text
1. 文件读写必须通过 main/file-system 或 main/services。
2. 禁止渲染层直接拼接本地路径。
3. 本地数据模型必须统一定义。
4. 数据迁移必须有版本记录。
5. 大文件处理必须考虑异步、进度、取消、异常恢复。
```

## 安全规范

```text
1. contextIsolation 必须开启。
2. nodeIntegration 默认关闭。
3. preload 只暴露最小必要 API。
4. 禁止渲染层执行任意系统命令。
5. 文件路径、外部链接、协议调用必须校验。
```


## 通用强制原则

无论使用任何语言或框架，都必须遵守以下规则：

```text
1. 同一业务数据只能有一个权威来源。
2. 同一字段只能有一个统一类型定义。
3. 同一枚举只能有一个统一常量定义。
4. 页面只能消费数据，不能私自重新定义业务数据。
5. 接口请求必须统一封装，禁止散落在页面中。
6. 状态管理必须有明确归属，禁止多个页面各自维护同一份状态。
7. mock 数据必须与类型定义和真实接口保持一致。
8. 任何字段、接口、枚举、状态修改前，必须触发 change-impact-analysis。
9. 任何修改完成后，必须触发 data-consistency-regression-test。
```

## 项目初始化必须生成的文件

```text
docs/development-standard.md
docs/data-source-standard.md
docs/change-impact-standard.md
docs/regression-test-checklist.md
docs/module-map.md
AGENTS.md
```

## 数据源统一规范

每个核心业务对象必须登记：

```text
1. 业务对象名称
2. 类型定义位置
3. 接口请求位置
4. 状态管理位置
5. 枚举/常量位置
6. mock 数据位置
7. 使用页面
8. 使用组件
9. 关联功能：筛选、排序、统计、导出、权限、详情、表单
10. 修改注意事项
```

推荐在项目中维护：

```text
docs/data-source-map.md
```

## AI Coding 执行规则

AI 在开发过程中必须：

```text
1. 先确认当前模块归属，再写代码。
2. 先查是否已有类型、接口、组件、常量，再新增。
3. 禁止重复创建相似组件、相似数据结构、相似状态枚举。
4. 新增页面时，必须复用已有 service、store、types、constants、components。
5. 修改已有功能时，必须先做影响面分析。
6. 修改完成后，必须输出修改文件、影响范围、自测结果和待人工验收项。
```


## Electron 项目修改前检查

涉及以下内容时，必须先触发 `change-impact-analysis`：

```text
1. 修改 IPC 通道
2. 修改 preload API
3. 修改本地文件结构
4. 修改数据库字段
5. 修改窗口行为
6. 修改自动更新逻辑
7. 修改主进程服务
8. 修改渲染层数据展示
9. 修改权限/安全策略
10. 修改日志与错误处理
```
