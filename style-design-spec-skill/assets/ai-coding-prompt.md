# AI Coding 执行提示词

请读取并遵循以下项目文件：

- `docs/design/design-spec.md`
- `docs/design/design-tokens.json`
- `docs/design/design-review-checklist.md`

执行要求：

1. 先检查项目现有组件、tokens、框架版本和页面模式，再决定修改位置。
2. 将 `design-tokens.json` 作为设计值的单一事实源，优先使用 semantic 或 component token。
3. 不创建重复语义值。确需扩展时，先说明需求、证据、影响范围和建议 token，再更新规范与 tokens。
4. 只实现组件、平台和输入模态适用的状态，不机械添加 hover、selected 或 loading。
5. 保持设计规范中的信息层级、内容密度、响应式行为、主题和国际化规则。
6. 实现键盘、可见焦点、语义名称、错误反馈、目标对比度和减弱动效等适用要求。
7. 不复制参考品牌的专有资产或文案。
8. 完成后在覆盖矩阵指定的视口、主题和状态进行视觉检查，并更新 review checklist 的状态与证据。
9. 对无法满足的规则列出位置、原因、风险和最小修复方案，不要静默偏离。

规则优先级：用户当前明确要求 > 已确认的项目约束 > 证据化设计规范 > 项目适配建议。发生冲突时停止相关局部修改并报告，不扩大影响范围。
