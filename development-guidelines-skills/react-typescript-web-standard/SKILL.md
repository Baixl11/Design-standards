---
name: react-typescript-web-standard
description: React + TypeScript Web 应用开发规范 Skill。用于生成和约束 React Web 项目的目录结构、组件拆分、Hooks、状态管理、接口封装、类型定义、统一数据源、页面开发和 AI Coding 修改规则。
---

# React + TypeScript Web 开发规范 Skill

## 适用场景

适用于：

- React Web 应用
- 企业管理后台
- SaaS 工具
- 数据看板
- AI Coding Web 工具
- Vite + React + TypeScript 项目
- React + Ant Design / shadcn/ui / MUI 项目

## 推荐技术组合

```text
React + TypeScript + Vite
UI：Ant Design / shadcn/ui / MUI
状态管理：Zustand / Redux Toolkit / Jotai
请求层：axios / fetch wrapper / TanStack Query
表单：React Hook Form / Ant Design Form
测试：Vitest + Testing Library + Playwright
代码规范：ESLint + Prettier
```

## 推荐目录结构

```text
src/
  app/
    router.tsx
    providers.tsx
    layout.tsx
  pages/
    dashboard/
    users/
  features/
    user/
      components/
      hooks/
      services/
      stores/
      types.ts
      constants.ts
      mock.ts
      index.ts
  shared/
    components/
    hooks/
    services/
    utils/
    types/
    constants/
  assets/
  styles/
```

## React 组件规范

```text
1. 页面级组件放 pages。
2. 业务组件放 features/{module}/components。
3. 通用组件放 shared/components。
4. 组件必须单一职责，禁止一个组件同时处理数据请求、复杂业务判断和大量 UI 展示。
5. 业务组件优先通过 props 接收数据，不直接访问全局状态，除非是容器组件。
6. 表格列、状态标签、筛选器等可复用逻辑必须抽成组件或配置。
```

## Hooks 规范

```text
1. 请求类 hooks 命名为 useXxxQuery / useXxxMutation。
2. 业务逻辑 hooks 放 features/{module}/hooks。
3. 通用 hooks 放 shared/hooks。
4. 禁止在多个页面重复写相同的数据转换逻辑。
5. Hook 中涉及字段、枚举、状态转换时，必须引用统一 types/constants。
```

## 状态管理规范

```text
1. 服务端数据优先使用 TanStack Query 或统一请求 hooks。
2. 客户端 UI 状态可用 Zustand/Jotai。
3. 同一业务对象的全局状态只能有一个 store。
4. store 文件必须放在对应 feature 下。
5. 禁止页面各自维护同一份业务状态。
```

## 类型与常量规范

```text
features/user/types.ts        定义 User、UserQuery、UserDetail 等类型
features/user/constants.ts    定义 USER_STATUS、USER_ROLE 等枚举和映射
features/user/services/       定义接口请求
features/user/mock.ts         定义 mock 数据
```

字段、枚举、状态文案必须统一来源，禁止在页面中直接硬编码。

## 接口封装规范

```text
1. 页面不得直接写 axios/fetch 请求。
2. 所有 API 必须放 features/{module}/services 或 shared/services。
3. API 返回结构必须有统一类型。
4. 请求参数和返回数据必须有 TypeScript 类型定义。
5. 接口字段变化时必须同步 types、mock、页面展示、筛选、统计和测试。
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


## React 项目修改前检查

涉及以下内容时，必须先触发 `change-impact-analysis`：

```text
1. 修改 props 字段
2. 修改表格列
3. 修改筛选条件
4. 修改详情页展示字段
5. 修改状态枚举
6. 修改 hooks 返回值
7. 修改 store 结构
8. 修改 service 接口
9. 修改 mock 数据
10. 修改权限逻辑
```
