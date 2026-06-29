# Apple Design Style Tokens

## 1. Token 来源说明

- `真实采集`：来自 Apple 官网、iPhone 页面、Apple Developer 页面 DOM 样式读取。
- `观察估算`：来自公开页面视觉观察，未进行像素级测量。
- `适配建议`：为了让 Apple 风格适配 Web、SaaS、AI Coding 和通用前端项目而定义。

## 2. Color Tokens

```css
:root {
  /* Accent */
  --color-primary: #0071e3;              /* 真实采集：iPhone 页 CTA */
  --color-primary-hover: #0077ed;        /* 适配建议 */
  --color-primary-active: #006edb;       /* 适配建议 */
  --color-primary-light: #e8f2ff;        /* 适配建议 */
  --color-focus-ring: rgba(0, 113, 227, 0.35);

  /* Neutral backgrounds */
  --color-background-page: #f5f5f7;      /* 真实采集：Apple 浅灰页面 */
  --color-background-canvas: #ffffff;    /* 真实采集 */
  --color-background-card: #ffffff;
  --color-background-sidebar: #f5f5f7;
  --color-background-modal: #ffffff;
  --color-background-elevated: #ffffff;

  /* Dark mode backgrounds */
  --color-background-dark: #000000;      /* 真实采集：Developer 深色页 */
  --color-background-dark-elevated: #161617;

  /* Text */
  --color-text-primary: #1d1d1f;         /* 真实采集 */
  --color-text-secondary: #6e6e73;       /* 真实采集 */
  --color-text-muted: #86868b;           /* 真实采集 */
  --color-text-disabled: #a1a1a6;
  --color-text-inverse: #f5f5f7;         /* 真实采集 */

  /* Borders */
  --color-border-default: #d2d2d7;       /* 适配建议 */
  --color-border-muted: #e8e8ed;         /* 适配建议 */
  --color-border-active: #0071e3;
  --color-divider: rgba(0, 0, 0, 0.12);
  --color-divider-dark: rgba(255, 255, 255, 0.16);

  /* Status */
  --color-success: #34c759;              /* 适配建议 */
  --color-warning: #ff9500;              /* 适配建议 */
  --color-danger: #ff3b30;               /* 适配建议 */
  --color-info: #007aff;                 /* 适配建议 */

  /* Controls */
  --color-button-neutral: #1d1d1f;       /* 真实采集：中性 CTA */
  --color-control-fill: #f5f5f7;
  --color-control-fill-hover: #e8e8ed;
}
```

## 3. Dark Mode Color Tokens

```css
[data-theme="dark"] {
  --color-background-page: #000000;
  --color-background-canvas: #000000;
  --color-background-card: #161617;
  --color-background-sidebar: #161617;
  --color-background-modal: #1d1d1f;
  --color-background-elevated: #1d1d1f;

  --color-text-primary: #f5f5f7;
  --color-text-secondary: #a1a1a6;
  --color-text-muted: #86868b;
  --color-text-disabled: #6e6e73;
  --color-text-inverse: #1d1d1f;

  --color-border-default: rgba(255, 255, 255, 0.18);
  --color-border-muted: rgba(255, 255, 255, 0.1);
  --color-divider: rgba(255, 255, 255, 0.14);
  --color-control-fill: rgba(255, 255, 255, 0.08);
  --color-control-fill-hover: rgba(255, 255, 255, 0.12);
}
```

## 4. Typography Tokens

```css
:root {
  --font-family-sans: "SF Pro Text", "SF Pro Icons", -apple-system, BlinkMacSystemFont, "Helvetica Neue", Helvetica, Arial, "PingFang SC", "Microsoft YaHei", sans-serif;
  --font-family-display: "SF Pro Display", "SF Pro Text", -apple-system, BlinkMacSystemFont, "Helvetica Neue", Helvetica, Arial, "PingFang SC", sans-serif;
  --font-family-mono: "SF Mono", ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;

  --font-size-xs: 12px;
  --font-size-sm: 14px;
  --font-size-md: 17px;       /* 真实采集：Apple 页面 body 和按钮 */
  --font-size-lg: 21px;
  --font-size-xl: 24px;
  --font-size-2xl: 28px;
  --font-size-3xl: 32px;
  --font-size-4xl: 48px;
  --font-size-5xl: 56px;

  --font-weight-regular: 400;
  --font-weight-medium: 500;
  --font-weight-semibold: 600;
  --font-weight-bold: 700;

  --line-height-tight: 1.1;
  --line-height-snug: 1.2;
  --line-height-normal: 1.47;
  --line-height-relaxed: 1.6;

  --letter-spacing-default: 0;
}
```

## 5. Spacing Tokens

```css
:root {
  --spacing-0: 0;
  --spacing-1: 4px;
  --spacing-2: 8px;
  --spacing-3: 12px;
  --spacing-4: 16px;
  --spacing-5: 20px;
  --spacing-6: 24px;
  --spacing-8: 32px;
  --spacing-10: 40px;
  --spacing-12: 48px;
  --spacing-16: 64px;
  --spacing-20: 80px;
  --spacing-24: 96px;
  --spacing-30: 120px;

  --page-gutter-sm: 24px;
  --page-gutter-md: 40px;
  --page-gutter-lg: 64px;
  --section-gap: 64px;
  --section-gap-large: 96px;
  --card-padding: 24px;
  --card-padding-large: 32px;
}
```

## 6. Radius Tokens

```css
:root {
  --radius-xs: 6px;
  --radius-sm: 8px;
  --radius-md: 12px;
  --radius-lg: 18px;
  --radius-xl: 24px;
  --radius-2xl: 28px;
  --radius-full: 999px;       /* 真实采集：Apple CTA 为 980px，项目中统一为 999px */
}
```

## 7. Shadow Tokens

```css
:root {
  --shadow-none: none;
  --shadow-sm: 0 2px 8px rgba(0, 0, 0, 0.06);
  --shadow-md: 0 8px 24px rgba(0, 0, 0, 0.08);
  --shadow-lg: 0 18px 44px rgba(0, 0, 0, 0.12);
  --shadow-modal: 0 18px 60px rgba(0, 0, 0, 0.18);
  --shadow-dark-modal: 0 24px 80px rgba(0, 0, 0, 0.48);
}
```

## 8. Border Tokens

```css
:root {
  --border-width-default: 1px;
  --border-width-strong: 2px;
  --border-color-default: var(--color-border-default);
  --border-color-muted: var(--color-border-muted);
  --border-color-active: var(--color-primary);
  --border-default: 1px solid var(--color-border-default);
  --border-muted: 1px solid var(--color-border-muted);
}
```

## 9. Z-Index Tokens

```css
:root {
  --z-dropdown: 1000;
  --z-sticky: 1020;
  --z-fixed: 1030;
  --z-drawer: 1040;
  --z-modal: 1050;
  --z-toast: 1060;
  --z-tooltip: 1070;
}
```

## 10. Motion Tokens

```css
:root {
  --motion-duration-fast: 120ms;
  --motion-duration-normal: 200ms;
  --motion-duration-slow: 300ms;
  --motion-duration-enter: 220ms;
  --motion-duration-exit: 160ms;

  --motion-ease-default: cubic-bezier(0.2, 0, 0, 1);
  --motion-ease-enter: cubic-bezier(0.16, 1, 0.3, 1);
  --motion-ease-exit: cubic-bezier(0.7, 0, 0.84, 0);
}
```

## 11. Breakpoint Tokens

```css
:root {
  --breakpoint-xs: 480px;
  --breakpoint-sm: 640px;
  --breakpoint-md: 768px;
  --breakpoint-lg: 1024px;
  --breakpoint-xl: 1280px;
  --breakpoint-2xl: 1536px;

  --container-sm: 640px;
  --container-md: 980px;
  --container-lg: 1200px;
  --container-xl: 1440px;
}
```

## 12. Component Tokens

```css
:root {
  --button-height-md: 44px;
  --button-padding-md: 11px 21px;      /* 真实采集：Apple CTA */
  --button-radius: var(--radius-full);
  --button-font-size: 17px;
  --button-line-height: 20px;

  --input-height-md: 44px;
  --input-padding-md: 0 14px;
  --input-radius: var(--radius-md);
  --input-font-size: 16px;

  --table-row-height: 48px;
  --table-cell-padding: 12px 16px;

  --topbar-height: 52px;
  --sidebar-width: 260px;
  --modal-radius: var(--radius-xl);
}
```

## 13. Tailwind CSS 配置建议

```js
theme: {
  extend: {
    colors: {
      primary: {
        DEFAULT: '#0071e3',
        hover: '#0077ed',
        active: '#006edb',
        light: '#e8f2ff'
      },
      apple: {
        ink: '#1d1d1f',
        gray: '#6e6e73',
        muted: '#86868b',
        cloud: '#f5f5f7',
        line: '#d2d2d7',
        lineMuted: '#e8e8ed'
      },
      success: '#34c759',
      warning: '#ff9500',
      danger: '#ff3b30',
      info: '#007aff'
    },
    fontFamily: {
      sans: ['SF Pro Text', 'SF Pro Icons', '-apple-system', 'BlinkMacSystemFont', 'Helvetica Neue', 'Helvetica', 'Arial', 'PingFang SC', 'sans-serif'],
      display: ['SF Pro Display', 'SF Pro Text', '-apple-system', 'BlinkMacSystemFont', 'Helvetica Neue', 'Helvetica', 'Arial', 'PingFang SC', 'sans-serif']
    },
    borderRadius: {
      sm: '8px',
      md: '12px',
      lg: '18px',
      xl: '24px',
      full: '999px'
    },
    spacing: {
      1: '4px',
      2: '8px',
      3: '12px',
      4: '16px',
      5: '20px',
      6: '24px',
      8: '32px',
      10: '40px',
      12: '48px',
      16: '64px',
      20: '80px',
      24: '96px'
    },
    boxShadow: {
      sm: '0 2px 8px rgba(0, 0, 0, 0.06)',
      md: '0 8px 24px rgba(0, 0, 0, 0.08)',
      lg: '0 18px 44px rgba(0, 0, 0, 0.12)',
      modal: '0 18px 60px rgba(0, 0, 0, 0.18)'
    },
    transitionTimingFunction: {
      apple: 'cubic-bezier(0.2, 0, 0, 1)'
    }
  }
}
```

## 14. 无法确认的 Token

| Token | 原因 | 需要补充材料 | 当前建议 |
|---|---|---|---|
| 原生 iOS/macOS 控件尺寸 | Web 页面不能代表原生平台控件 | 目标平台和官方控件文档 | 按平台 HIG 复核 |
| 复杂业务表格密度 | Apple 官网不是后台系统 | 业务截图或数据结构 | 使用 48px 行高和 12px 16px 内距作为起点 |
| 卡片精确圆角 | 未做像素级测量 | 目标参考截图 | 使用 18px 到 24px |
| 深色主题全部状态色 | 未逐项采集 | 具体深色页面 | 使用半透明边框和高对比文本复核 |
