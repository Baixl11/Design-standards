# AI Coding 执行提示词

请严格按照 design-spec.md、design-tokens.md 和 design-review-checklist.md 进行页面开发。

要求：

1. 所有页面必须使用统一色彩、字号、间距、圆角、阴影和组件规范。
2. 不允许临时创造新的视觉样式。
3. 不允许随意写死颜色、字号、间距、圆角等样式。
4. 新增组件前必须先判断是否可以复用现有组件。
5. 页面布局必须符合 design-spec.md 中的页面模板。
6. 所有交互状态必须包含 hover、active、disabled、loading、empty、error。
7. 样式应优先通过 design-tokens.md 中的 token 实现。
8. 如果使用 Tailwind CSS，应优先使用统一配置，不要在页面中散落大量临时 class。
9. 每次完成页面后，必须使用 design-review-checklist.md 进行设计一致性检查。
10. 如果页面与设计规范不一致，需要先修复再进入下一步开发。
11. 如果目标对象数据不足，不允许凭空补全设计规范，必须标注无法采集项。
