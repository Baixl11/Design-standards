---
name: springboot-backend-standard
description: Java Spring Boot 后端服务开发规范 Skill。用于约束 Spring Boot 项目的分层架构、Controller、Service、Repository、DTO、Entity、统一错误处理、权限、事务、日志、测试、数据源一致性和 AI Coding 修改规则。
---

# Spring Boot 后端开发规范 Skill

## 适用场景

适用于：

- Java Spring Boot 后端服务
- 企业级业务系统
- 管理后台后端
- 权限、流程、事务较复杂的系统
- 微服务或模块化单体系统

## 推荐技术组合

```text
Spring Boot + Java
ORM：Spring Data JPA / MyBatis Plus
数据库：MySQL / PostgreSQL
鉴权：Spring Security + JWT
文档：OpenAPI / Swagger
测试：JUnit + Mockito + Testcontainers
构建：Maven / Gradle
```

## 推荐目录结构

```text
src/main/java/com/example/project/
  Application.java
  common/
    config/
    exception/
    response/
    security/
    logging/
  modules/
    user/
      controller/
      service/
      repository/
      dto/
      entity/
      mapper/
      enums/
      constants/
```

## 分层规范

```text
1. Controller 只处理请求参数、鉴权上下文和响应封装。
2. Service 处理业务逻辑和事务。
3. Repository/Mapper 处理数据访问。
4. DTO 处理请求和响应对象。
5. Entity 只表示数据库实体。
6. Mapper 负责 Entity 与 DTO 转换。
```

## API 与响应规范

```text
1. 所有接口必须统一响应结构。
2. 错误码必须统一定义。
3. Controller 不得直接返回 Entity。
4. 分页、排序、筛选必须统一参数格式。
5. 接口变更必须同步 OpenAPI 文档、DTO、测试和前端调用。
```

## 数据与事务规范

```text
1. 数据库字段变更必须有迁移脚本。
2. 事务边界必须放在 Service 层。
3. 枚举字段必须统一定义。
4. 禁止多个模块重复定义同一业务枚举。
5. 跨模块调用必须通过明确的 service 接口。
```

## 权限与安全规范

```text
1. 鉴权逻辑必须统一。
2. 权限标识必须集中定义。
3. 禁止在 Controller 中散落复杂权限判断。
4. 敏感数据必须脱敏。
5. 日志不得输出密码、Token、身份证号等敏感信息。
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


## Spring Boot 项目修改前检查

涉及以下内容时，必须先触发 `change-impact-analysis`：

```text
1. 修改 DTO 字段
2. 修改 Entity 字段
3. 修改数据库表结构
4. 修改枚举/状态
5. 修改 Controller 接口
6. 修改 Service 业务逻辑
7. 修改权限标识
8. 修改错误码
9. 修改 OpenAPI 文档
10. 修改测试用例
```
