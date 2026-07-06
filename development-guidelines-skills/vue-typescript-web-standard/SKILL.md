---
name: vue-typescript-web-standard
description: Vue + TypeScript Web 应用开发规范 Skill。用于生成和约束 Vue Web 项目的目录结构、组件拆分、Composition API、Pinia 状态管理、接口封装、类型定义、统一数据源和 AI Coding 修改规则。
---

# Vue + TypeScript Web 开发规范 Skill

## 适用场景

适用于：

- Vue 3 Web 应用
- 企业管理后台
- 数据看板
- 业务系统
- Vite + Vue + TypeScript 项目
- Vue + Element Plus / Arco Design / Naive UI 项目

## 推荐技术组合

```text
Vue 3 + TypeScript + Vite
UI：Element Plus / Arco Design / Naive UI
状态管理：Pinia
请求层：axios/fetch wrapper
路由：Vue Router
表单：组件库 Form + schema 配置
测试：Vitest + Vue Test Utils + Playwright
代码规范：ESLint + Prettier
```

## 推荐目录结构

```text
src/
  app/
    router.ts
    plugins.ts
  pages/
    dashboard/
    users/
  features/
    user/
      components/
      composables/
      services/
      stores/
      types.ts
      constants.ts
      mock.ts
      index.ts
  shared/
    components/
    composables/
    services/
    utils/
    types/
    constants/
  assets/
  styles/
```

## Vue 组件规范

```text
1. 页面级组件放 pages。
2. 业务组件放 features/{module}/components。
3. 通用组件放 shared/components。
4. 单文件组件必须保持职责清晰，避免 template、script、style 过度膨胀。
5. 复杂业务逻辑必须抽到 composables 或 services。
6. 表格列、表单 schema、筛选条件需要统一配置，避免多个页面重复定义。
```

## Composition API 规范

```text
1. 业务 composable 命名为 useXxx。
2. composables 必须放在对应 feature 下，通用能力放 shared/composables。
3. 不允许多个页面重复实现同一数据转换逻辑。
4. 涉及字段和枚举的转换必须引用 constants/types。
```

## Pinia 状态管理规范

```text
1. 每个业务模块最多一个核心 Pinia store。
2. Store 放在 features/{module}/stores。
3. Store 只管理跨页面共享状态，不替代 service 层。
4. 页面临时 UI 状态可以本地维护，但业务状态必须统一。
5. 修改 store 字段时必须全局搜索引用。
```

## 接口与类型规范

```text
features/user/types.ts        定义 User、UserQuery、UserDetail 等类型
features/user/constants.ts    定义 USER_STATUS、USER_ROLE 等枚举和映射
features/user/services/       定义接口请求
features/user/mock.ts         定义 mock 数据
```

页面不得直接发请求，必须通过 service/composable 调用。


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


## Vue 项目修改前检查

涉及以下内容时，必须先触发 `change-impact-analysis`：

```text
1. 修改 props / emits
2. 修改表格列配置
3. 修改表单 schema
4. 修改筛选条件
5. 修改详情字段
6. 修改 Pinia store 字段
7. 修改 service 接口
8. 修改 mock 数据
9. 修改路由参数
10. 修改权限逻辑
```
