# 视频取证工具 Design Tokens

## 1. Token 来源说明

本文件将 `design-spec.md` 中的观察结果转化为可用于前端实现的设计变量。

来源标记：

- 真实采集：来自视频取证工具视觉稿 PNG、Figma meta JSON、PRD 截图/说明或本机安装目录。
- 观察估算：来自截图观察或 meta 统计，但未逐组件精确测量。
- 适配建议：为了后续 AI Coding 和前端实现稳定性而整理的工程化建议。

注意：主工具浅色 token 与播放器暗色 token 必须分离使用。

## 2. Color Tokens

### 2.1 主工具浅色主题

| Token | Value | 用途 | 来源 |
|---|---:|---|---|
| `--color-primary` | `#2194FF` | 主操作、选中、链接、激活图标 | 真实采集 |
| `--color-primary-hover` | `#168CFF` | 主按钮 hover、强交互 hover | 真实采集与观察估算 |
| `--color-primary-active` | `#007DF1` | active、按下状态 | 真实采集 |
| `--color-primary-strong` | `#3067F2` | 报告阅读器按钮、打印按钮 | 真实采集 |
| `--color-primary-light` | `#ECF5FF` | 浅蓝选中背景 | 真实采集 |
| `--color-primary-soft` | `#E8F3FF` | hover 背景、弱强调 | 真实采集与 HTML 原型 |
| `--color-primary-border` | `#C9E4FF` | hover/selected 弱边框 | 真实采集与 HTML 原型 |
| `--color-background-page` | `#F4F6F9` | 页面背景 | 真实采集 |
| `--color-background-app` | `#F3F7FC` | 原型应用底色 | 真实采集 |
| `--color-background-card` | `#FFFFFF` | 卡片、表格、弹窗 | 真实采集 |
| `--color-background-soft` | `#FBFDFF` | 输入框弱底、浅内容区 | 观察估算 |
| `--color-background-table-head` | `#F4F6F8` | 表头、分组标题 | 真实采集 |
| `--color-background-sidebar-active` | `#ECF5FF` | 侧边栏选中项 | 真实采集 |
| `--color-background-modal-mask` | `rgba(0, 0, 0, 0.68)` | 弹窗遮罩 | 观察估算 |
| `--color-text-primary` | `#303133` | 一级文本 | 真实采集 |
| `--color-text-regular` | `#606266` | 正文 | 真实采集 |
| `--color-text-secondary` | `#909399` | 次级说明 | 真实采集 |
| `--color-text-muted` | `#A7B0C9` | 弱提示 | 真实采集 |
| `--color-text-disabled` | `#C0C4CC` | 禁用文字、placeholder | 真实采集 |
| `--color-text-inverse` | `#FFFFFF` | 深色底文字、主按钮文字 | 真实采集 |
| `--color-border-default` | `#DCDFE6` | 默认边框 | 真实采集 |
| `--color-border-light` | `#E4E7ED` | 次级边框 | 真实采集 |
| `--color-border-muted` | `#EBEEF5` | 分割线 | 真实采集 |
| `--color-border-active` | `#2194FF` | focus、selected | 真实采集 |
| `--color-success` | `#00A870` | 成功、正常、已挂载 | 真实采集 |
| `--color-success-soft` | `#E8FFF4` | 成功标签背景 | 适配建议 |
| `--color-warning` | `#FF8E00` | 警告 | 真实采集 |
| `--color-warning-soft` | `#FFF4E0` | 警告标签背景 | 适配建议 |
| `--color-danger` | `#E34D59` | 错误、失败、取消 | 真实采集 |
| `--color-danger-strong` | `#F4453C` | 强错误、红色角标、播放器红 | 真实采集 |
| `--color-danger-soft` | `#FFF0F0` | 错误标签背景 | 适配建议 |
| `--color-info` | `#2194FF` | 信息提示、进度 | 真实采集 |

### 2.2 播放器暗色扩展

| Token | Value | 用途 | 来源 |
|---|---:|---|---|
| `--player-bg` | `#000000` | 播放器深色背景 | 真实采集 |
| `--player-panel` | `rgba(24, 24, 32, 0.78)` | 播放器卡片、底部提示 | 观察估算 |
| `--player-text-primary` | `#FFFFFF` | 播放器主标题 | 真实采集 |
| `--player-text-secondary` | `#DEE2ED` | 播放器正文 | 真实采集 |
| `--player-accent-red` | `#F4453C` | 播放按钮、强强调 | 真实采集 |
| `--player-accent-purple` | `#916CEC` | 暗色能力卡光感 | 真实采集 |
| `--player-accent-blue` | `#07DDFA` | 暗色能力卡光感 | 真实采集 |

## 3. Typography Tokens

| Token | Value | 用途 | 来源 |
|---|---:|---|---|
| `--font-family-sans` | `"Microsoft YaHei", "PingFang SC", "Segoe UI", Arial, sans-serif` | 全局字体 | 真实采集 |
| `--font-size-xs` | `12px` | 角标、标签、辅助说明 | 真实采集 |
| `--font-size-sm` | `13px` | 紧凑说明、卡片辅助文字 | 真实采集 |
| `--font-size-md` | `14px` | 默认正文、表格、按钮 | 真实采集 |
| `--font-size-lg` | `16px` | 分组标题、弹窗标题辅助 | 真实采集 |
| `--font-size-xl` | `18px` | 页面标题、小标题 | 真实采集 |
| `--font-size-2xl` | `20px` | 产品标题、重要标题 | 真实采集 |
| `--font-size-3xl` | `24px` | 报告标题 | 真实采集 |
| `--font-size-display` | `40px` | 播放器首页宣传标题 | 真实采集，限定播放器 |
| `--font-weight-regular` | `400` | 正文 | 真实采集 |
| `--font-weight-medium` | `500` | 字段强调 | 真实采集 |
| `--font-weight-semibold` | `700` | 选中项、按钮、标题 | 真实采集 |
| `--font-weight-bold` | `700` | 大标题 | 真实采集 |
| `--line-height-tight` | `1.25` | 标题 | 适配建议 |
| `--line-height-normal` | `1.5` | 正文、表格 | 真实采集与适配建议 |
| `--line-height-relaxed` | `1.7` | 长说明、空状态说明 | 真实采集与适配建议 |

## 4. Spacing Tokens

| Token | Value | 用途 |
|---|---:|---|
| `--spacing-0` | `0` | 清零 |
| `--spacing-1` | `4px` | 极小间距 |
| `--spacing-2` | `8px` | 小间距、图标文字间距 |
| `--spacing-3` | `12px` | 卡片内边距、表格紧凑间距 |
| `--spacing-4` | `16px` | 页面常用间距 |
| `--spacing-5` | `20px` | 工具栏左右间距 |
| `--spacing-6` | `24px` | 模块间距、弹窗边距 |
| `--spacing-8` | `32px` | 大弹窗内容边距 |
| `--spacing-10` | `40px` | 大模块间隔 |
| `--spacing-12` | `48px` | 空状态、大区块 |

来源：观察估算与适配建议。视觉稿中大量间距符合 4px/8px 系列。

## 5. Size Tokens

| Token | Value | 用途 | 来源 |
|---|---:|---|---|
| `--size-titlebar-height` | `56px` | 顶部标题栏 | 真实采集 |
| `--size-sidebar-width` | `266px` | 左侧导航 | 真实采集 |
| `--size-toolbar-height` | `58px` | 紧凑工具栏 | 观察估算 |
| `--size-toolbar-height-lg` | `74px` | 大工具栏 | 观察估算 |
| `--size-control-sm` | `28px` | 小标签、小按钮 | 观察估算 |
| `--size-control-md` | `32px` | 输入框、分页、桌面按钮 | 真实采集 |
| `--size-control-lg` | `36px` | 主按钮、搜索框 | 观察估算 |
| `--size-control-xl` | `40px` | 高优先级按钮 | 真实采集 |
| `--size-click-target-desktop` | `32px` | 鼠标桌面最小点击区 | 适配建议 |
| `--size-click-target-touch` | `44px` | 触控/Web 原型最小点击区 | 适配建议 |
| `--size-icon-sm` | `16px` | 小图标 | 真实采集 |
| `--size-icon-md` | `20px` | 常规工具栏图标 | 真实采集 |
| `--size-icon-lg` | `24px` | 顶部入口图标 | 真实采集 |

## 6. Radius Tokens

| Token | Value | 用途 | 来源 |
|---|---:|---|---|
| `--radius-xs` | `2px` | 分页、基础组件 | 真实采集 |
| `--radius-sm` | `3px` | 小组件、表格内部 | 真实采集 |
| `--radius-md` | `4px` | 输入框、标签、小按钮 | 真实采集 |
| `--radius-lg` | `6px` | 卡片、侧栏选中、浮层 | 真实采集 |
| `--radius-xl` | `8px` | 页面级容器、播放器卡片 | 观察估算 |
| `--radius-full` | `999px` | 圆形图标、角标、胶囊标签 | 真实采集 |

## 7. Shadow Tokens

| Token | Value | 用途 | 来源 |
|---|---|---|---|
| `--shadow-none` | `none` | 表格、普通容器 | 适配建议 |
| `--shadow-sm` | `0 4px 12px rgba(36, 72, 112, 0.04)` | 轻卡片 hover | 真实采集 |
| `--shadow-md` | `0 8px 22px rgba(32, 68, 105, 0.08)` | 工具栏、卡片、浮层 | 真实采集 |
| `--shadow-lg` | `0 12px 34px rgba(25, 54, 84, 0.16)` | 原型画板、大浮层 | 真实采集 |
| `--shadow-modal` | `0 12px 34px rgba(24, 48, 76, 0.18)` | 弹窗 | 观察估算 |

## 8. Border Tokens

| Token | Value | 用途 |
|---|---:|---|
| `--border-width-default` | `1px` | 默认边框 |
| `--border-color-default` | `#DCDFE6` | 输入框、表格、卡片 |
| `--border-color-light` | `#E4E7ED` | 次级边框 |
| `--border-color-muted` | `#EBEEF5` | 分割线 |
| `--border-color-hover` | `#C9E4FF` | hover 弱蓝边 |
| `--border-color-active` | `#2194FF` | focus/selected |
| `--border-color-danger` | `#E34D59` | 错误 |

## 9. Z-Index Tokens

| Token | Value | 用途 |
|---|---:|---|
| `--z-dropdown` | `1000` | 下拉菜单 |
| `--z-sticky` | `1020` | 粘性表头、底部操作 |
| `--z-fixed` | `1030` | 固定工具栏 |
| `--z-popover` | `1060` | 任务列表、tooltip |
| `--z-drawer` | `1080` | 抽屉 |
| `--z-modal` | `1100` | 弹窗 |
| `--z-toast` | `1200` | 全局提示 |

来源：适配建议。

## 10. Motion Tokens

| Token | Value | 用途 |
|---|---:|---|
| `--motion-duration-fast` | `120ms` | hover、focus |
| `--motion-duration-normal` | `160ms` | 下拉、选中切换 |
| `--motion-duration-slow` | `200ms` | 弹窗、抽屉 |
| `--motion-ease-default` | `cubic-bezier(0.2, 0, 0, 1)` | 默认 |
| `--motion-ease-enter` | `cubic-bezier(0, 0, 0.2, 1)` | 进入 |
| `--motion-ease-exit` | `cubic-bezier(0.4, 0, 1, 1)` | 离开 |

来源：适配建议。

## 11. Breakpoint Tokens

| Token | Value | 用途 |
|---|---:|---|
| `--breakpoint-min-desktop` | `1280px` | 最低桌面适配 |
| `--breakpoint-design` | `1366px` | 主设计基准 |
| `--breakpoint-desktop` | `1440px` | 常规桌面 |
| `--breakpoint-wide` | `1920px` | 大屏设计稿 |
| `--breakpoint-mobile-sm` | `390px` | Web 原型移动验证 |
| `--breakpoint-mobile-md` | `430px` | Web 原型移动验证 |

来源：真实采集与适配建议。

## 12. CSS Variables 建议

```css
:root {
  --color-primary: #2194ff;
  --color-primary-hover: #168cff;
  --color-primary-active: #007df1;
  --color-primary-strong: #3067f2;
  --color-primary-light: #ecf5ff;
  --color-primary-soft: #e8f3ff;
  --color-primary-border: #c9e4ff;

  --color-background-page: #f4f6f9;
  --color-background-app: #f3f7fc;
  --color-background-card: #ffffff;
  --color-background-soft: #fbfdff;
  --color-background-table-head: #f4f6f8;
  --color-background-sidebar-active: #ecf5ff;
  --color-background-modal-mask: rgba(0, 0, 0, 0.68);

  --color-text-primary: #303133;
  --color-text-regular: #606266;
  --color-text-secondary: #909399;
  --color-text-muted: #a7b0c9;
  --color-text-disabled: #c0c4cc;
  --color-text-inverse: #ffffff;

  --color-border-default: #dcdfe6;
  --color-border-light: #e4e7ed;
  --color-border-muted: #ebeef5;
  --color-border-hover: #c9e4ff;
  --color-border-active: #2194ff;

  --color-success: #00a870;
  --color-success-soft: #e8fff4;
  --color-warning: #ff8e00;
  --color-warning-soft: #fff4e0;
  --color-danger: #e34d59;
  --color-danger-strong: #f4453c;
  --color-danger-soft: #fff0f0;
  --color-info: #2194ff;

  --font-family-sans: "Microsoft YaHei", "PingFang SC", "Segoe UI", Arial, sans-serif;
  --font-size-xs: 12px;
  --font-size-sm: 13px;
  --font-size-md: 14px;
  --font-size-lg: 16px;
  --font-size-xl: 18px;
  --font-size-2xl: 20px;
  --font-size-3xl: 24px;
  --font-size-display: 40px;

  --font-weight-regular: 400;
  --font-weight-medium: 500;
  --font-weight-semibold: 700;
  --font-weight-bold: 700;

  --line-height-tight: 1.25;
  --line-height-normal: 1.5;
  --line-height-relaxed: 1.7;

  --spacing-1: 4px;
  --spacing-2: 8px;
  --spacing-3: 12px;
  --spacing-4: 16px;
  --spacing-5: 20px;
  --spacing-6: 24px;
  --spacing-8: 32px;
  --spacing-10: 40px;
  --spacing-12: 48px;

  --size-titlebar-height: 56px;
  --size-sidebar-width: 266px;
  --size-toolbar-height: 58px;
  --size-toolbar-height-lg: 74px;
  --size-control-sm: 28px;
  --size-control-md: 32px;
  --size-control-lg: 36px;
  --size-control-xl: 40px;
  --size-click-target-desktop: 32px;
  --size-click-target-touch: 44px;
  --size-icon-sm: 16px;
  --size-icon-md: 20px;
  --size-icon-lg: 24px;

  --radius-xs: 2px;
  --radius-sm: 3px;
  --radius-md: 4px;
  --radius-lg: 6px;
  --radius-xl: 8px;
  --radius-full: 999px;

  --shadow-sm: 0 4px 12px rgba(36, 72, 112, 0.04);
  --shadow-md: 0 8px 22px rgba(32, 68, 105, 0.08);
  --shadow-lg: 0 12px 34px rgba(25, 54, 84, 0.16);
  --shadow-modal: 0 12px 34px rgba(24, 48, 76, 0.18);

  --motion-duration-fast: 120ms;
  --motion-duration-normal: 160ms;
  --motion-duration-slow: 200ms;
  --motion-ease-default: cubic-bezier(0.2, 0, 0, 1);
}

[data-theme="dark-player"] {
  --player-bg: #000000;
  --player-panel: rgba(24, 24, 32, 0.78);
  --player-text-primary: #ffffff;
  --player-text-secondary: #dee2ed;
  --player-accent-red: #f4453c;
  --player-accent-purple: #916cec;
  --player-accent-blue: #07ddfa;
}
```

## 13. Tailwind CSS 配置建议

```js
export default {
  theme: {
    extend: {
      colors: {
        primary: {
          DEFAULT: "#2194ff",
          hover: "#168cff",
          active: "#007df1",
          strong: "#3067f2",
          light: "#ecf5ff",
          soft: "#e8f3ff",
          border: "#c9e4ff"
        },
        background: {
          page: "#f4f6f9",
          app: "#f3f7fc",
          card: "#ffffff",
          soft: "#fbfdff",
          tableHead: "#f4f6f8"
        },
        text: {
          primary: "#303133",
          regular: "#606266",
          secondary: "#909399",
          muted: "#a7b0c9",
          disabled: "#c0c4cc",
          inverse: "#ffffff"
        },
        border: {
          DEFAULT: "#dcdfe6",
          light: "#e4e7ed",
          muted: "#ebeef5",
          hover: "#c9e4ff",
          active: "#2194ff"
        },
        success: "#00a870",
        warning: "#ff8e00",
        danger: "#e34d59",
        info: "#2194ff"
      },
      fontFamily: {
        sans: ["Microsoft YaHei", "PingFang SC", "Segoe UI", "Arial", "sans-serif"]
      },
      fontSize: {
        xs: "12px",
        sm: "13px",
        md: "14px",
        lg: "16px",
        xl: "18px",
        "2xl": "20px",
        "3xl": "24px",
        display: "40px"
      },
      borderRadius: {
        xs: "2px",
        sm: "3px",
        md: "4px",
        lg: "6px",
        xl: "8px",
        full: "999px"
      },
      spacing: {
        1: "4px",
        2: "8px",
        3: "12px",
        4: "16px",
        5: "20px",
        6: "24px",
        8: "32px",
        10: "40px",
        12: "48px"
      },
      boxShadow: {
        sm: "0 4px 12px rgba(36, 72, 112, 0.04)",
        md: "0 8px 22px rgba(32, 68, 105, 0.08)",
        lg: "0 12px 34px rgba(25, 54, 84, 0.16)",
        modal: "0 12px 34px rgba(24, 48, 76, 0.18)"
      },
      screens: {
        "min-desktop": "1280px",
        design: "1366px",
        desktop: "1440px",
        wide: "1920px"
      }
    }
  }
}
```

## 14. 无法确认的 Token

- 不同主题完整变量：当前只整理浅色主题和播放器暗色扩展，深色主题、消防主题未完整提取。
- 真实运行时 Windows 缩放后的字号和控件尺寸：需要补采 100%、125%、150% 缩放截图。
- 所有动效曲线：视觉稿以静态状态为主，motion token 属于适配建议。
- 全部组件变体：当前覆盖高频组件，若新增复杂组件，必须先从现有视觉稿或组件库继续提取。
