---
layout: post
title:  Maple Mono
date:   2024-11-27 12:38:52 +0800
categories:
---

换了个[字体][1]和高亮主题。

![VS Code截图](assets/img/Screenshot 2024-11-27 123608.png){: .shadow }

[1]: https://github.com/subframe7536/maple-font

亮色主题的inlay hints颜色太突兀了，改浅了些

```json
"workbench.colorCustomizations": {
  "[Maple Light]": {
    "editorInlayHint.background": "#ccc"
  }
}
```

没有用搭配的中文字体。严格2:1对应是挺整齐的，但还是有点太散了。
