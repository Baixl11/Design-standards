# {{TARGET_NAME}} 设计规范

> 生成时替换所有 `{{...}}` 字段，删除不适用章节和空表格。不要保留未经证据支持的默认值。

## 1. 文档状态

| 字段 | 内容 |
|---|---|
| 状态 | `draft` / `partial` / `verified` |
| 目标对象 | {{TARGET_NAME}} |
| 平台与版本 | {{PLATFORM_AND_VERSION}} |
| 目标项目 | {{TARGET_PROJECT}} |
| 采集日期 | {{CAPTURE_DATE}} |
| 主题、语言与地区 | {{MODES_AND_LOCALE}} |
| 负责人 | {{OWNER}} |

## 2. 范围与限制

### 已覆盖

{{COVERED_SCOPE}}

### 未覆盖

{{UNCOVERED_SCOPE}}

### 使用限制

{{LIMITATIONS}}

## 3. 证据索引

| ID | 来源 | 页面、节点或时间码 | 状态与视口 | 证据类型 | 采集方法 | 采集时间 | 限制 |
|---|---|---|---|---|---|---|---|
| E-001 | {{SOURCE}} | {{LOCATION}} | {{STATE_AND_SCOPE}} | DOM / Design node / Code / Screenshot / Video / Document | {{METHOD}} | {{CAPTURED_AT}} | {{LIMITATION}} |

## 4. 覆盖矩阵

| 页面或流程 | 组件 | 状态 | 主题 | 视口或输入模态 | 覆盖状态 | 证据 |
|---|---|---|---|---|---|---|
| {{SURFACE}} | {{COMPONENT}} | {{STATE}} | {{THEME}} | {{SCOPE}} | Covered / Partial / Missing | E-001 |

## 5. 设计定位

用可观察的界面规律描述产品语境和视觉语言。避免只写“高级、简洁、科技”等抽象词。

| 规则 | 界面表现 | 来源类型 | 置信度 | 证据 |
|---|---|---|---|---|
| {{RULE}} | {{OBSERVABLE_BEHAVIOR}} | `observed` | High / Medium / Low | E-001 |

## 6. 设计原则

| 原则 | 可执行规则 | 例外 | 证据 |
|---|---|---|---|
| {{PRINCIPLE}} | {{RULE}} | {{EXCEPTION}} | E-001 |

## 7. 基础系统

### 7.1 色彩

记录角色、状态、主题和 token 路径。将对比度结果与视觉观察分开。

| 角色 | 值或范围 | 用途 | 主题与状态 | 来源类型 | 置信度 | Token | 证据 |
|---|---|---|---|---|---|---|---|
| {{ROLE}} | {{VALUE}} | {{USAGE}} | {{MODE}} | {{STATUS}} | {{CONFIDENCE}} | {{TOKEN_PATH}} | E-001 |

### 7.2 字体与内容密度

| 角色 | 字体 | 字号 | 字重 | 行高 | 字距 | 内容规则 | 来源与证据 |
|---|---|---|---|---|---|---|---|
| {{ROLE}} | {{FAMILY}} | {{SIZE}} | {{WEIGHT}} | {{LINE_HEIGHT}} | {{LETTER_SPACING}} | {{CONTENT_RULE}} | {{STATUS}}, E-001 |

### 7.3 布局、网格与间距

| 场景 | 行为规则 | 值或范围 | 来源类型 | 置信度 | 证据 |
|---|---|---|---|---|---|
| {{CONTEXT}} | {{BEHAVIOR}} | {{VALUE}} | {{STATUS}} | {{CONFIDENCE}} | E-001 |

### 7.4 形状、边框、层级与阴影

| 角色 | 规则 | 值或范围 | Token | 来源与证据 |
|---|---|---|---|---|
| {{ROLE}} | {{RULE}} | {{VALUE}} | {{TOKEN_PATH}} | {{STATUS}}, E-001 |

### 7.5 图标、图像与品牌资产

{{ICONOGRAPHY_AND_IMAGERY}}

### 7.6 动效

| 场景 | 属性 | 时长与曲线 | 减弱动效行为 | 来源与证据 |
|---|---|---|---|---|
| {{SCENARIO}} | {{PROPERTY}} | {{MOTION}} | {{REDUCED_MOTION}} | {{STATUS}}, E-001 |

## 8. 语义 Token 架构

说明 primitive、semantic 和 component token 的关系、主题模式、命名规则与例外。以 `design-tokens.json` 为值的单一事实源。

{{TOKEN_ARCHITECTURE}}

## 9. 组件规范

只保留已观察或目标项目明确需要的组件。每个组件使用相同结构。

### {{COMPONENT_NAME}}

每条组件结论分别记录 `status`、`confidence`、`confidenceReason`、`evidenceIds`、`scope`、采集方法与时间；`adapted` 结论同时记录 `rationale`。

| 项目 | 规范 | 来源与证据 |
|---|---|---|
| 用途与边界 | {{USAGE}} | {{STATUS}}, E-001 |
| Anatomy | {{ANATOMY}} | {{STATUS}}, E-001 |
| Variants 与 sizes | {{VARIANTS}} | {{STATUS}}, E-001 |
| 适用状态 | {{STATES}} | {{STATUS}}, E-001 |
| 内容与溢出 | {{CONTENT_RULES}} | {{STATUS}}, E-001 |
| 鼠标、键盘与触控 | {{INPUT_BEHAVIOR}} | {{STATUS}}, E-001 |
| 响应式行为 | {{RESPONSIVE_BEHAVIOR}} | {{STATUS}}, E-001 |
| 无障碍 | {{ACCESSIBILITY}} | {{STATUS_AND_EVIDENCE}} |
| Tokens | {{TOKEN_PATHS}} | `design-tokens.json` |
| 实现注意事项 | {{IMPLEMENTATION_NOTES}} | `adapted`, {{RATIONALE}} |

## 10. 页面与流程

| 页面或流程 | 信息层级 | 布局与操作区 | 状态与异常路径 | 响应式行为 | 证据 |
|---|---|---|---|---|---|
| {{SURFACE}} | {{HIERARCHY}} | {{LAYOUT}} | {{STATES}} | {{RESPONSIVE}} | E-001 |

## 11. 响应式与输入模态

优先描述内容或容器达到边界时发生的行为变化。将观察到的阈值和项目建议阈值分开。

{{RESPONSIVE_AND_INPUT_RULES}}

## 12. 主题、国际化与极端内容

记录浅色、深色、高对比度、RTL、文本膨胀、系统字号、日期数字格式和长内容处理。

{{MODES_AND_LOCALIZATION}}

## 13. 无障碍观察与合规发现

| ID | 检查项 | 状态 | 证据 | 严重度 | 建议 |
|---|---|---|---|---|---|
| A11Y-001 | {{CHECK}} | Pass / Fail / Not tested / N/A | E-001 | Critical / High / Medium / Low | {{RECOMMENDATION}} |

## 14. 项目适配决策

| 决策 | 原始证据 | 适配原因 | 影响范围 | 状态 |
|---|---|---|---|---|
| {{DECISION}} | E-001 | {{RATIONALE}} | {{SCOPE}} | `adapted` |

## 15. 冲突、未知项与后续材料

| 项目 | 当前证据或冲突 | 影响 | 所需最少材料 | 当前处理 |
|---|---|---|---|---|
| {{ITEM}} | {{CONFLICT}} | {{IMPACT}} | {{MATERIAL}} | Omit / Draft / Adapted |

## 16. 实现与验收说明

{{IMPLEMENTATION_AND_REVIEW_NOTES}}
