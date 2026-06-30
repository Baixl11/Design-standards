# 目标软件 / 网站 / 风格设计规范采集与生成 Skill

这个 Skill 用于在用户明确要求整理某个软件、网站、应用或风格的设计规范时触发。

它的核心作用是帮助 AI 从真实页面、截图、交互状态、可观察布局与组件样式中提炼设计规则，并输出可用于 AI Coding、前端实现和设计审核的规范文档。

这个 Skill 特别适合以下场景：

- 整理某个软件、网站、App、PC 客户端或行业工具的设计规范。
- 将“苹果风格”“企业后台风格”“取证工具风格”等参考风格转化为可执行的页面设计规则。
- 在正式开发前生成统一的颜色、字体、间距、圆角、阴影、组件、布局、交互和响应式规范。
- 在开发后检查页面尺寸、按钮大小、文字重叠、横向溢出、选中态 / hover 边框突兀等设计一致性问题。

标准输出物包括：

- `design-spec.md`：完整设计规范。
- `design-tokens.md`：面向代码实现的设计变量。
- `design-review-checklist.md`：开发完成后的设计一致性检查清单。

## 核心文件

- `SKILL.md`：Skill 主文件，可直接放入你的 AI Skill 目录。
- `templates/design-spec-template.md`：完整设计规范输出模板。
- `templates/design-tokens-template.md`：设计变量输出模板。
- `templates/design-review-checklist-template.md`：设计一致性检查清单模板。
- `prompts/ai-coding-execution-prompt.md`：给 Codex / Cursor / Claude Code 使用的执行提示词。
- `examples/example-user-prompts.md`：典型触发与不触发示例。

## 推荐放置位置

你可以把整个文件夹放到桌面，也可以放到你的 AI Skill 汇总目录中，例如：

```text
~/Desktop/style-design-spec-skill
```

或者：

```text
/Users/cyan/个人工作/AI-skillS 汇总/style-design-spec-skill
```

## 使用方式

在 Codex 或其他 AI Coding 工具中，引入 `SKILL.md`，当用户明确要求整理某个软件、网站、应用或风格的设计规范时，按 Skill 执行。
