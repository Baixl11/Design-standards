---
name: nextjs-fullstack-standard
description: Next.js + TypeScript 全栈应用开发规范 Skill。用于约束 App Router、页面/组件分层、Server/Client Components、API Routes、数据请求、类型定义、统一数据源、SEO 和 AI Coding 修改规则。
---

# Next.js 全栈开发规范 Skill

## 适用场景

适用于：

- 官网 / 内容站 / 文档站
- SaaS Web 应用
- 全栈 Web 项目
- 需要 SEO 的产品页面
- Next.js App Router 项目

## 推荐技术组合

```text
Next.js + TypeScript
UI：shadcn/ui / Tailwind CSS / MUI
数据请求：Server Actions / Route Handlers / TanStack Query
数据库：Prisma + PostgreSQL / MySQL
鉴权：NextAuth/Auth.js 或自定义鉴权
测试：Vitest + Testing Library + Playwright
代码规范：ESLint + Prettier
```

## 推荐目录结构

```text
src/
  app/
    (marketing)/
    (dashboard)/
    api/
    layout.tsx
    page.tsx
  features/
    user/
      components/
      actions/
      services/
      queries/
      types.ts
      constants.ts
      schema.ts
      mock.ts
  shared/
    components/
    lib/
    utils/
    types/
    constants/
  server/
    db/
    auth/
    services/
```

## Server / Client Component 规范

```text
1. 默认使用 Server Component。
2. 只有需要交互、状态、浏览器 API 时才使用 Client Component。
3. Client Component 必须显式声明 'use client'。
4. 数据请求优先放在 Server Component、Server Action 或 query 层。
5. 禁止在多个页面重复定义相同数据获取逻辑。
```

## 数据请求规范

```text
1. 服务端数据获取统一放 features/{module}/queries 或 server/services。
2. 写操作统一使用 Server Actions 或 Route Handlers。
3. API 返回结构必须统一。
4. 数据库 schema、DTO、前端类型必须保持一致。
5. 修改字段时必须同步 Prisma schema、类型、表单、页面展示、mock 和测试。
```

## SEO 与路由规范

```text
1. 内容页必须配置 metadata。
2. 动态路由必须明确 params 类型。
3. 页面级 layout 不得混入复杂业务逻辑。
4. 权限路由必须统一在 middleware 或 layout 中处理。
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


## Next.js 项目修改前检查

涉及以下内容时，必须先触发 `change-impact-analysis`：

```text
1. 修改数据库字段
2. 修改 Prisma schema
3. 修改 Server Action 参数
4. 修改 Route Handler 返回值
5. 修改页面 metadata
6. 修改动态路由参数
7. 修改鉴权/权限逻辑
8. 修改表单字段
9. 修改列表/详情展示
10. 修改 mock 与测试数据
```
