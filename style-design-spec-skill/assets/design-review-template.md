# Design Review Checklist

## 审查信息

| 字段 | 内容 |
|---|---|
| 审查对象 | {{TARGET}} |
| 规范版本 | {{SPEC_VERSION}} |
| 实现版本 | {{IMPLEMENTATION_VERSION}} |
| 审查视口、主题与平台 | {{TEST_MATRIX}} |
| 审查人和日期 | {{REVIEWER_AND_DATE}} |

状态使用 `Pass`、`Fail`、`Not tested` 或 `N/A`。不要把未验证项标成通过。

## 1. 提取质量

| ID | 检查项 | 状态 | 证据 | 严重度 | Owner | 备注 |
|---|---|---|---|---|---|---|
| EX-001 | 每个精确值都有证据 ID 或明确标为 `adapted` | Not tested |  | High |  |  |
| EX-002 | 来源类型与置信度分别记录 | Not tested |  | Medium |  |  |
| EX-003 | 未观察组件、状态和主题没有被补写为事实 | Not tested |  | High |  |  |
| EX-004 | 冲突来源、范围差异与未验证项均已保留 | Not tested |  | Medium |  |  |
| EX-005 | 文档覆盖矩阵与实际采集范围一致 | Not tested |  | Medium |  |  |

## 2. Token 一致性

| ID | 检查项 | 状态 | 证据 | 严重度 | Owner | 备注 |
|---|---|---|---|---|---|---|
| TK-001 | 实现使用 `design-tokens.json` 中的语义或组件 token | Not tested |  | High |  |  |
| TK-002 | primitive、semantic 和 component alias 关系有效 | Not tested |  | High |  |  |
| TK-003 | 没有重复、空值、未知引用或未记录的语义值 | Not tested |  | High |  |  |
| TK-004 | 主题与状态切换不会改变非预期 token | Not tested |  | Medium |  |  |

## 3. 布局、内容与响应式

| ID | 检查项 | 状态 | 证据 | 严重度 | Owner | 备注 |
|---|---|---|---|---|---|---|
| LY-001 | 页面层级、容器、网格和密度符合规范 | Not tested |  | High |  |  |
| LY-002 | 在规范中的行为边界前后均已验证 | Not tested |  | High |  |  |
| LY-003 | 长文本、CJK、30% 文案膨胀和空数据不会重叠或溢出 | Not tested |  | High |  |  |
| LY-004 | 横竖屏、缩放、安全区和系统字号适用项已验证 | Not tested |  | Medium |  |  |

## 4. 组件与交互状态

| ID | 检查项 | 状态 | 证据 | 严重度 | Owner | 备注 |
|---|---|---|---|---|---|---|
| CP-001 | 组件 anatomy、variants 和 sizes 与规范一致 | Not tested |  | High |  |  |
| CP-002 | 仅实现平台和组件适用的状态 | Not tested |  | Medium |  |  |
| CP-003 | 状态变化不造成非预期布局位移 | Not tested |  | High |  |  |
| CP-004 | loading、empty、error、offline 和权限不足等适用异常路径完整 | Not tested |  | High |  |  |
| CP-005 | 鼠标、键盘和触控行为分别符合规范 | Not tested |  | High |  |  |

## 5. 无障碍与国际化

| ID | 检查项 | 状态 | 证据 | 严重度 | Owner | 备注 |
|---|---|---|---|---|---|---|
| AX-001 | 文本与非文本对比度满足目标标准 | Not tested |  | High |  |  |
| AX-002 | 键盘顺序、可见焦点和焦点恢复正确 | Not tested |  | Critical |  |  |
| AX-003 | 控件有正确语义、accessible name 和错误反馈 | Not tested |  | Critical |  |  |
| AX-004 | 320px reflow、200% 缩放和系统字号适用项可用 | Not tested |  | High |  |  |
| AX-005 | `prefers-reduced-motion` 或平台减弱动效设置有效 | Not tested |  | Medium |  |  |
| AX-006 | RTL、地区格式和翻译文本适用项正确 | Not tested |  | Medium |  |  |

## 6. 视觉验证

| ID | 检查项 | 状态 | 证据 | 严重度 | Owner | 备注 |
|---|---|---|---|---|---|---|
| VS-001 | 关键页面已在覆盖矩阵中的视口与主题截图验证 | Not tested |  | High |  |  |
| VS-002 | 目标引用与实现差异已分类为缺陷、适配或已接受差异 | Not tested |  | Medium |  |  |
| VS-003 | 动态内容和状态切换没有遮挡、闪烁或异常截断 | Not tested |  | High |  |  |

## 问题登记

| Issue ID | 位置 | 问题 | 严重度 | 证据 | 建议修复 | Owner | 状态 |
|---|---|---|---|---|---|---|---|
| DR-001 | {{LOCATION}} | {{ISSUE}} | {{SEVERITY}} | {{EVIDENCE}} | {{REMEDIATION}} | {{OWNER}} | Open |

## 审查结论

- 阻塞项：{{BLOCKERS}}
- 未验证项：{{NOT_TESTED}}
- 已接受差异：{{ACCEPTED_DEVIATIONS}}
- 结论：Pass / Pass with conditions / Fail
