# Design Tokens

## 1. Token 来源说明

- 目标对象：
- 采集方式：
- Token 类型：真实采集 / 观察估算 / 适配建议

## 2. Color Tokens

```css
:root {
  --color-primary: ;
  --color-primary-hover: ;
  --color-primary-active: ;
  --color-primary-light: ;

  --color-background-page: ;
  --color-background-card: ;
  --color-background-sidebar: ;
  --color-background-modal: ;

  --color-text-primary: ;
  --color-text-secondary: ;
  --color-text-muted: ;
  --color-text-disabled: ;

  --color-border-default: ;
  --color-border-muted: ;
  --color-border-active: ;

  --color-success: ;
  --color-warning: ;
  --color-danger: ;
  --color-info: ;
}
```

## 3. Typography Tokens

```css
:root {
  --font-family-sans: ;

  --font-size-xs: ;
  --font-size-sm: ;
  --font-size-md: ;
  --font-size-lg: ;
  --font-size-xl: ;
  --font-size-2xl: ;

  --font-weight-regular: 400;
  --font-weight-medium: 500;
  --font-weight-semibold: 600;
  --font-weight-bold: 700;

  --line-height-tight: ;
  --line-height-normal: ;
  --line-height-relaxed: ;
}
```

## 4. Spacing Tokens

```css
:root {
  --spacing-1: 4px;
  --spacing-2: 8px;
  --spacing-3: 12px;
  --spacing-4: 16px;
  --spacing-5: 20px;
  --spacing-6: 24px;
  --spacing-8: 32px;
  --spacing-10: 40px;
  --spacing-12: 48px;
}
```

## 5. Radius Tokens

```css
:root {
  --radius-sm: ;
  --radius-md: ;
  --radius-lg: ;
  --radius-xl: ;
  --radius-full: 9999px;
}
```

## 6. Shadow Tokens

```css
:root {
  --shadow-sm: ;
  --shadow-md: ;
  --shadow-lg: ;
  --shadow-modal: ;
}
```

## 7. Border Tokens

```css
:root {
  --border-width-default: 1px;
  --border-color-default: ;
  --border-color-muted: ;
  --border-color-active: ;
}
```

## 8. Z-Index Tokens

```css
:root {
  --z-dropdown: 1000;
  --z-sticky: 1020;
  --z-fixed: 1030;
  --z-drawer: 1040;
  --z-modal: 1050;
  --z-toast: 1060;
}
```

## 9. Motion Tokens

```css
:root {
  --motion-duration-fast: 120ms;
  --motion-duration-normal: 200ms;
  --motion-duration-slow: 300ms;

  --motion-ease-default: ease;
  --motion-ease-enter: ease-out;
  --motion-ease-exit: ease-in;
}
```

## 10. Breakpoint Tokens

```css
:root {
  --breakpoint-sm: 640px;
  --breakpoint-md: 768px;
  --breakpoint-lg: 1024px;
  --breakpoint-xl: 1280px;
  --breakpoint-2xl: 1536px;
}
```

## 11. Tailwind CSS 配置建议

```js
theme: {
  extend: {
    colors: {
      primary: '',
      background: '',
      foreground: '',
      muted: '',
      border: '',
      success: '',
      warning: '',
      danger: ''
    },
    borderRadius: {
      sm: '',
      md: '',
      lg: '',
      xl: ''
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
      12: '48px'
    },
    boxShadow: {
      sm: '',
      md: '',
      lg: '',
      modal: ''
    }
  }
}
```

## 12. 无法确认的 Token

| Token | 原因 | 需要补充材料 | 当前建议 |
|---|---|---|---|
|  |  |  |  |
