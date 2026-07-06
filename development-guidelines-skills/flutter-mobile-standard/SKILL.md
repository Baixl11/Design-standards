---
name: flutter-mobile-standard
description: Flutter 移动端应用开发规范 Skill。用于约束 Flutter 项目的目录结构、页面路由、状态管理、数据模型、接口封装、权限申请、弱网处理、统一数据源和 AI Coding 修改规则。
---

# Flutter 移动端开发规范 Skill

## 适用场景

适用于：

- Flutter iOS/Android App
- 跨平台移动端应用
- 企业移动端工具
- 移动端数据采集/展示应用

## 推荐技术组合

```text
Flutter + Dart
状态管理：Riverpod / Bloc / Provider
路由：go_router
网络：Dio
数据模型：freezed + json_serializable
本地存储：shared_preferences / Hive / SQLite
测试：flutter_test + integration_test
```

## 推荐目录结构

```text
lib/
  app/
    app.dart
    router.dart
    theme.dart
  features/
    user/
      pages/
      widgets/
      providers/
      repositories/
      models/
      constants.dart
      mock.dart
  shared/
    widgets/
    services/
    utils/
    models/
    constants/
  core/
    network/
    storage/
    permissions/
    error/
```

## 页面与组件规范

```text
1. 页面放 features/{module}/pages。
2. 业务组件放 features/{module}/widgets。
3. 通用组件放 shared/widgets。
4. 页面只负责组合 UI，不直接写复杂数据请求和业务转换。
5. 业务逻辑放 providers/repositories/services。
```

## 状态管理规范

```text
1. 跨页面共享业务状态必须放 provider/bloc。
2. 本地 UI 状态可以放 StatefulWidget 或局部 provider。
3. 同一业务对象只能有一个状态来源。
4. 修改状态模型时必须全局检查引用页面、组件、repository、mock 和测试。
```

## 数据模型与接口规范

```text
1. 数据模型统一放 features/{module}/models。
2. 接口封装统一放 repositories 或 core/network。
3. JSON 序列化必须统一生成，禁止页面手动解析字段。
4. mock 数据必须与模型字段一致。
5. 字段变更必须同步模型、repository、provider、页面、测试。
```

## 移动端专项规范

```text
1. 权限申请必须统一封装，包括相机、相册、定位、通知、蓝牙、麦克风、文件。
2. 弱网、无网、超时、重试必须有统一处理。
3. 加载、空状态、错误状态必须有统一 UI。
4. 本地缓存需要明确过期策略。
5. App 生命周期变化需要处理数据刷新、暂停、恢复。
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


## Flutter 项目修改前检查

涉及以下内容时，必须先触发 `change-impact-analysis`：

```text
1. 修改 model 字段
2. 修改 repository 返回结构
3. 修改 provider/bloc 状态
4. 修改路由参数
5. 修改权限调用
6. 修改本地缓存结构
7. 修改列表/详情展示
8. 修改表单字段
9. 修改 mock 数据
10. 修改集成测试
```
