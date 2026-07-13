# Token 模型

将结构化 JSON 作为 Token 单一事实源。按目标工具支持的 DTCG 版本序列化，并在根级扩展中记录版本；再由该文件生成 CSS、Tailwind 或原生平台映射。

## 分层

只建立有证据或明确适配依据的叶节点：

| 层级 | 作用 | 示例路径形式 |
| --- | --- | --- |
| Primitive | 保存原始色彩、尺寸、字体、时长等基础值，不表达用途。 | `color.primitive.neutral.900` |
| Semantic | 表达界面角色，并优先通过别名引用 Primitive。 | `color.semantic.text.primary` |
| Component | 表达组件部位、变体和状态，并优先引用 Semantic。 | `component.button.primary.background.default` |

不要为了填满层级而制造 Token。只有一个已知层级时，先输出该层级并记录缺口。

## DTCG 结构

- 使用 `$type`、`$value`、`$description` 和 `$extensions`。
- 使用 DTCG 别名语法引用其他 Token；不要复制可复用的字面值。
- 使用 DTCG 定义的颜色、尺寸、时长、描边、阴影、字体等复合类型。
- 为每个叶节点添加 `style-design-spec` 扩展。
- 在根级扩展中记录 `formatVersion`、`generatedAt`、`targets` 和 `documentStatus`。
- 若消费工具不支持某种 DTCG 类型，保留规范源并在生成器中显式转换；不要降级规范源的数据语义。

根级 `style-design-spec` 扩展必须包含：

| 字段 | 约束 |
|---|---|
| `formatVersion` | 非空格式版本字符串。 |
| `generatedAt` | 带时区的 ISO-8601 date-time。 |
| `targets` | 至少一个非空目标平台或消费端。 |
| `documentStatus` | `draft`、`partial` 或 `verified`。 |

每个叶节点的扩展至少包含：

```json
{
  "$extensions": {
    "style-design-spec": {
      "status": "measured",
      "evidenceIds": ["E-007", "E-008"],
      "confidence": "high",
      "confidenceReason": "同一版本的多个实例由直接工具取得一致值",
      "scope": {
        "theme": "light",
        "state": "default"
      }
    }
  }
}
```

示例只说明扩展字段，不构成默认值。`status` 和 `confidence` 的含义遵循 `evidence-model.md`。除 `adapted` 外，`evidenceIds` 至少包含一个匹配 `^E-[0-9]{3,}$` 的 ID。

## 命名与别名

- 使用小写英文、稳定层级和一致的单复数；避免在路径中编码暂时页面名。
- 让 Primitive 名称描述值域，让 Semantic 名称描述用途，让 Component 名称描述组件契约。
- 将状态放在组件路径末端，例如 `default`、`hover`、`focus-visible` 或 `disabled`。
- 只为真实存在或目标平台需要的状态建项；不要强制为触控界面生成 `hover`。
- 防止循环别名和悬空别名。生成前解析全部引用。
- 需要主题或模式时，使用目标工具明确支持的模式结构或带版本的扩展；不要假装 DTCG 核心已定义目标工具的模式语义。

## 适配项

将平台、安全、无障碍或品牌约束导致的修改标为 `adapted`，并遵守：

- 必须填写 `rationale`，说明必须调整的约束。
- 可将 `evidenceIds` 设为空数组；存在参考证据时仍应引用。
- 必须在 `scope` 中说明平台、主题、输入模态或用户设置。

不要用适配后的值覆盖参考对象的采集值；需要比较时保留两个独立 Token 集或在报告中建立映射。

## 未知项与冲突项

- 未知值不要创建 Token 叶节点。
- 不要输出 `null`、空字符串、`TBD`、无单位尺寸、无效颜色或仅含注释的变量。
- 不要为未知值生成 CSS 自定义属性、Tailwind 配置或原生常量。
- 将未知项写入 `design-spec.md` 的 `unresolved` 清单，记录所需证据和受影响用途；若用户只要求 tokens，则在交付摘要中报告。不要把非 token 清单混入 `design-tokens.json`。
- 将未解决冲突写入 `design-spec.md` 的 `conflicts` 清单，并引用全部证据；若用户只要求 tokens，则在交付摘要中报告。裁决前不要生成代码。
- 仅生成具有合法 `$value` 或可解析别名的叶节点。

## 生成检查

1. 校验 JSON 语法和目标 DTCG 版本。
2. 校验类型、单位、颜色空间、别名路径和循环引用。
3. 校验每个叶节点的 `status`、`evidenceIds`、`confidence`、`confidenceReason` 和 `scope`；校验 `adapted` 的 `rationale`。
4. 校验 Semantic 优先引用 Primitive，Component 优先引用 Semantic。
5. 校验生成代码只包含已确认且目标平台可表达的 Token。
6. 比较生成物与结构化源；发现手工漂移时重新生成，不要双向修改。
