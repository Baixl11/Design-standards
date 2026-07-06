---
name: fastapi-backend-standard
description: Python FastAPI 后端服务开发规范 Skill。用于约束 FastAPI 项目的目录结构、API 路由、Pydantic Schema、服务层、数据库模型、统一错误处理、日志、测试、数据源一致性和 AI Coding 修改规则。
---

# FastAPI 后端开发规范 Skill

## 适用场景

适用于：

- Python FastAPI 后端服务
- AI 应用后端
- 数据处理 API
- Web/App/桌面端配套后端
- MVP 快速后端服务

## 推荐技术组合

```text
FastAPI + Python
数据校验：Pydantic
ORM：SQLAlchemy / SQLModel
迁移：Alembic
数据库：PostgreSQL / MySQL / SQLite
鉴权：JWT / OAuth2
测试：pytest + httpx
代码规范：ruff + black + mypy
```

## 推荐目录结构

```text
app/
  main.py
  api/
    v1/
      routes/
      deps.py
  modules/
    user/
      router.py
      service.py
      repository.py
      schemas.py
      models.py
      constants.py
      tests/
  core/
    config.py
    security.py
    errors.py
    logging.py
  db/
    session.py
    migrations/
  tests/
```

## 分层规范

```text
1. router 只处理路由、参数、响应，不写复杂业务逻辑。
2. service 处理业务规则。
3. repository 处理数据库访问。
4. schemas 处理请求/响应模型。
5. models 处理数据库模型。
6. constants 处理枚举、状态、错误码。
```

## API 规范

```text
1. API 必须有明确请求 schema 和响应 schema。
2. 禁止直接返回数据库 ORM 对象给前端。
3. 错误响应必须统一格式。
4. 分页、筛选、排序参数必须统一。
5. 修改字段时必须同步 schemas、models、repository、service、测试和前端接口文档。
```

## 数据模型规范

```text
1. 数据库模型和 Pydantic schema 必须明确区分。
2. 每个业务模块维护自己的 models/schemas/constants。
3. 枚举字段必须统一定义。
4. 字段默认值、可空、长度、索引必须明确。
5. 数据库变更必须创建迁移脚本。
```

## 错误处理与日志规范

```text
1. 全局异常必须统一处理。
2. 业务错误必须有错误码。
3. 日志必须包含 trace_id/request_id。
4. 敏感信息不得进入日志。
5. 文件上传、鉴权、权限失败必须记录必要审计信息。
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


## FastAPI 项目修改前检查

涉及以下内容时，必须先触发 `change-impact-analysis`：

```text
1. 修改 API 路由
2. 修改请求/响应 schema
3. 修改数据库模型
4. 修改枚举/状态
5. 修改鉴权/权限
6. 修改 service 业务规则
7. 修改 repository 查询逻辑
8. 修改错误码
9. 修改测试用例
10. 修改前端依赖接口
```
