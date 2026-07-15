# 设计风格实施包索引

> 生成日期：2026-07-14。每个目录都包含 `design-spec.md`、`design-tokens.json` 和 `design-review-checklist.md`。

## 如何理解这些规范

这些条目并不处于同一层级，组合使用前应先确定主设计系统，再叠加视觉或行为层：

| 类型 | 条目 | 使用方式 |
|---|---|---|
| 品牌/平台语言 | 小米、鸿蒙、Google 风 | 作为产品气质、平台习惯与内容表达参考；不得复制专有品牌资产。 |
| 完整设计系统 | Material Design | 可作为组件、颜色、排版、形状和动效的主系统。 |
| 视觉流派 | 扁平化、拟物化、极简主义、暗黑模式、玻璃拟态、粘土拟态 | 作为表面、密度、材质或主题策略；不能替代完整交互系统。 |
| 行为层 | 微交互设计 | 叠加在任意主系统之上，定义触发、反馈、状态、恢复与减弱动效。 |

## 文件清单

| 目录 | 中文名称 | 类型 | 状态 | 定位摘要 |
|---|---|---|---|---|
| [`xiaomi/`](./xiaomi/design-spec.md) | 小米风格 | 品牌/平台语言 | `draft` | HyperOS 3：中性信息骨架、多尺寸组件、连续即时活动与跨设备任务；不复制小米资产。 |
| [`harmonyos/`](./harmonyos/design-spec.md) | 鸿蒙风格 | 品牌/平台语言 | `draft` | HarmonyOS 7：空间化界面、沉浸光感、轻量悬浮窗口与多设备自适应；旧蓝白/轻拟物仅作历史基础。 |
| [`google-style/`](./google-style/design-spec.md) | Google 风 | 品牌/平台语言 | `draft` | Google 品牌价值启发：简单、友好、几何、状态驱动；必须使用独立色盘、字体、图标和组件，且不等同 Material。 |
| [`flat-design/`](./flat-design/design-spec.md) | 扁平化设计 | 视觉流派 | `draft` | 二维、清晰、低装饰；用 Flat 2.0 的边界和轻层级补回交互线索。 |
| [`skeuomorphism/`](./skeuomorphism/design-spec.md) | 拟物化设计 | 视觉流派 | `draft` | 用一致的现实对象和受力线索帮助理解；数字效率与可访问性优先于物理忠实。 |
| [`material-design/`](./material-design/design-spec.md) | 材质设计 | 完整设计系统 | `draft` | M3/M3 Expressive：语义色、15 级排版、形状、色调海拔、组件与自适应；稳定 API 和 alpha 预览严格分开。 |
| [`minimalism/`](./minimalism/design-spec.md) | 极简主义 | 视觉流派 | `draft` | 以任务为准做减法；有限色盘、强排版和负空间不能牺牲导航、标签与反馈。 |
| [`microinteractions/`](./microinteractions/design-spec.md) | 微交互设计 | 行为层 | `draft` | 跨风格行为层；用触发—规则—反馈—恢复描述按钮、校验、进度和状态变化。 |
| [`dark-mode/`](./dark-mode/design-spec.md) | 暗黑模式 | 视觉流派/主题模式 | `draft` | 跨平台主题模式：语义色重映射、暗色表面层级、系统协商与媒体/控件完整覆盖；禁止简单反相。 |
| [`glassmorphism/`](./glassmorphism/design-spec.md) | 玻璃拟态 | 视觉流派 | `draft` | 单层、瞬态、语义化毛玻璃；必须在最差背景测对比，并为 reduced transparency/无支持/低性能提供实色回退。 |
| [`claymorphism/`](./claymorphism/design-spec.md) | 粘土拟态 | 视觉流派 | `draft` | 实色、饱满、大圆角和统一光源的软体表面；阴影只补充体积，控件边界、焦点和状态必须独立可靠。 |

## 组合建议

- 移动端生态应用：以 HarmonyOS 或 Material 为主系统，再选择极简、暗黑或微交互作为附加层。
- 跨平台工具：以 Material 或自有组件系统为骨架，吸收 Google 风的信息清晰度、小米/鸿蒙的跨设备规则。
- 展示型体验：可叠加玻璃拟态或粘土拟态，但核心表单、表格、长文本和高风险操作保留高对比实色表面。
- 拟物化与粘土拟态：用于强化对象、品牌或低频体验，不应让材质替代标签、状态和可访问语义。
- 暗黑模式不是独立品牌；它应通过 semantic token 映射与任一主风格配对。
- 微交互不是视觉主题；它负责反馈与状态转换，不能用动效掩盖失败、延迟或缺失的错误恢复。

## 状态说明

当前全部标记为 `draft`：公开文档证据和适配规则已整理，但尚未绑定具体项目、组件库、目标版本和运行时页面。选定风格并进入项目后，应补充真实页面证据、运行态测量、对比度报告、键盘/读屏测试和视觉回归，再升级为 `partial` 或 `verified`。
