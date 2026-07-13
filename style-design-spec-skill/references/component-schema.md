# 组件 Schema

只记录已观察到或目标产品明确需要的组件。不要为满足固定数量而补造组件、变体或状态。

索引：[记录格式](#记录格式) · [顶层字段](#顶层字段) · [Anatomy](#anatomy) · [Variants](#variants) · [States](#states) · [Input Modality](#input-modality) · [A11y](#a11y) · [Token 绑定](#token-绑定) · [Evidence](#evidence) · [发布检查](#发布检查)

## 记录格式

按以下结构输出。字段类型用于约束格式，不是可交付值；不要把 `string` 或 `[]` 原样写入结果。

```yaml
component_id: string
name: string
purpose: string
platforms: [string]
anatomy:
  - part_id: string
    role: string
    required: boolean
    conditions: [string]
    status: measured | sampled | observed | inferred | adapted
    confidence: high | medium | low
    confidenceReason: string
    scope: {}
    evidenceIds: [E-001]
    method: string
    captured_at: ISO-8601 string
    rationale: required when status is adapted
variants:
  - axis: string
    values: [string]
    default: string
    constraints: [string]
    status: measured | sampled | observed | inferred | adapted
    confidence: high | medium | low
    confidenceReason: string
    scope: {}
    evidenceIds: [E-001]
    method: string
    captured_at: ISO-8601 string
    rationale: required when status is adapted
states:
  - name: string
    trigger: string
    behavior: string
    input_modalities: [pointer, touch, keyboard, assistive_technology]
    token_bindings: {}
    a11y_effects: [string]
    status: measured | sampled | observed | inferred | adapted
    confidence: high | medium | low
    confidenceReason: string
    scope: {}
    evidenceIds: [E-001]
    method: string
    captured_at: ISO-8601 string
    rationale: required when status is adapted
input_modalities: {}
a11y: {}
tokens: {}
evidence:
  coverage: {}
  gaps: [string]
```

## 顶层字段

为每个组件建立一个独立记录，并使用稳定 `component_id`：

| 字段 | 要求 |
| --- | --- |
| `component_id` | 使用稳定、唯一、语义化 ID。 |
| `name` | 使用产品中的组件名称；未知时使用中性功能名。 |
| `purpose` | 用一句话说明职责，不描述装饰。 |
| `platforms` | 列出 Web、Windows、macOS、iOS、Android 等适用平台。 |
| `anatomy` | 定义部位、职责、可选性和证据。 |
| `variants` | 定义变体轴与合法取值，不要枚举不存在的组合。 |
| `states` | 定义触发条件、行为、视觉变化和状态转换。 |
| `input_modalities` | 分别定义指针、触控、键盘和辅助技术行为。 |
| `a11y` | 定义语义、名称、焦点、键盘、对比度和用户偏好。 |
| `tokens` | 将可视属性绑定到结构化 Token 路径。 |
| `evidence` | 引用逐项证据，并标明未覆盖范围。 |

## Anatomy

为每个部位记录：

- `part_id`、名称和职责。
- `required` 与出现条件。
- 内容类型、长度或数量限制。
- 与其他部位的布局关系。
- 支持该结论的 `evidenceIds`、`status`、`confidence` 和 `scope`。

不要把视觉样式写死在 Anatomy；通过 `tokens` 绑定样式。

## Variants

将变体拆成正交轴，例如层级、尺寸或强调程度。为每个轴记录：

- 合法取值与默认值。
- 适用平台和上下文。
- 禁止组合或依赖条件。
- 每个取值的 status、confidence、scope 和 evidenceIds。

将为目标产品新增的变体标为 `adapted`。不要把推断的变体标为来源事实。

## States

只定义适用状态。常见状态可包括 `default`、`hover`、`focus-visible`、`active`、`selected`、`disabled`、`loading`、`error`、`success` 和 `empty`，但不要强制补齐。

为每个状态记录：

- 进入条件、退出条件和允许的状态转换。
- 可交互性、事件结果和异步行为。
- 文案、图标、布局与 Token 的变化。
- 适用输入模态和平台。
- 无障碍语义或公告变化。
- status、confidence、scope 和 evidenceIds。

区分 `disabled` 与 `loading`，区分 `focus-visible` 与指针点击后的焦点。未知行为列入覆盖缺口，不要自行确定。

## Input Modality

分别检查并记录：

- `pointer`：悬停、点击、右键、拖拽和精细指向。
- `touch`：触控目标、长按、手势、滚动冲突和安全区。
- `keyboard`：Tab 顺序、Enter/Space、方向键、Escape 和快捷键。
- `assistive_technology`：可访问名称、角色、值、状态和动态公告。

不要要求触控设备提供 `hover`。不要仅用颜色或悬停传达必要信息。

## A11y

至少评估以下项目，并对不适用项标记 `N/A`：

- 语义角色、可访问名称、描述、值和状态。
- 键盘可操作性、逻辑焦点顺序、焦点可见性和焦点恢复。
- 文本、图标、边界和状态提示的对比度。
- 目标平台适用的触控或点击目标要求。
- 200% 缩放、reflow、文本膨胀和本地化。
- `prefers-reduced-motion`、高对比模式、深浅主题和用户字体设置。
- RTL、读屏顺序、错误识别与修复提示。

将无障碍修正标为 `adapted`，并说明依据的标准、平台规范或用户约束。

## Token 绑定

使用 `属性 -> Token 路径` 映射，例如将背景、文字、边框、间距、圆角、阴影、排版和动效分别绑定。遵循以下规则：

- 优先引用 Component Token，其次引用 Semantic Token。
- 不在组件文档中重复字面值。
- 为变体和状态使用明确路径，不依赖含糊的覆盖顺序。
- 未知 Token 保持缺失，并列入 `token_gaps`；不要生成空绑定。

## Evidence

让 Anatomy、Variant、State、A11y 和 Token 绑定分别引用自己的 `evidenceIds`。除 `adapted` 外，每项至少引用一个匹配 `^E-[0-9]{3,}$` 的 ID；`adapted` 可使用空数组，但必须填写 `rationale`。不要只在组件底部附一个通用来源。

记录 `coverage`：列出已观察的平台、主题、视口、状态和输入模态；将未观察部分列入 `gaps`。所有 status、confidence、scope、冲突与裁决规则遵循 `evidence-model.md`。

## 发布检查

1. 检查组件是否确实存在或有明确目标需求。
2. 检查部位、变体和状态是否互相一致且无非法组合。
3. 检查每种适用输入模态是否有可执行行为。
4. 检查无障碍字段是否可验收，而不是泛泛建议。
5. 检查 Token 引用是否存在、类型匹配且无悬空路径。
6. 检查每个确定结论是否有逐项证据，未知项是否留在缺口清单。
