# 1. What is a web page?

A tiny page, **not** the Linktree, to see how a web page is put together. It has
four files:

| File | Language | Job |
|------|----------|-----|
| [`index.html`](index.html) | HTML | the **structure**: a logo, a heading, an input, a button |
| [`style.css`](style.css) | CSS | the **style**: colours, spacing, rounded corners |
| [`script.js`](script.js) | JavaScript | the **action**: on click, show a greeting |
| [`images/logo.svg`](images/logo.svg) | image | a picture the HTML points to |

## `index.html` is the front door

- When someone opens a website, the server sends **`index.html` first**. It is
  the default file name every host looks for (GitHub Pages, Netlify, Vercel and
  so on). Other pages can have other names, like `about.html`.
- `index.html` does **not** contain everything. It *points* to the other files:

```html
<link rel="stylesheet" href="style.css" />   <!-- the style -->
<script src="script.js"></script>            <!-- the action -->
<img src="images/logo.svg" alt="Logo" />     <!-- the picture -->
```

- The browser reads `index.html`, sees those lines, and then **downloads each
  file separately**. Even a giant site like Facebook works like this: a small
  `index.html` that loads many CSS and JavaScript files.

## Try it

1. Open the page: `open index.html` (Mac) or `start index.html` (Windows).
2. Type a name, click **Say hello**.
3. Open DevTools (`Cmd + Option + I` / `F12`), go to the **Network** tab, and
   refresh. You will see four requests: `index.html`, `style.css`,
   `script.js`, `logo.svg`. The first one is always `index.html`.
4. **Break it on purpose:**
   - Delete the `<link ... style.css>` line and refresh: no style.
   - Delete the `<script ...>` line and refresh: the button does nothing.
5. Rename `index.html` to `home.html` and open it with a double-click: it still
   works on your laptop. On a web host, the home page would be missing,
   because the host looks for `index.html`.

## Build tools (later)

In React (Class 6) a tool called Vite takes many source files and **bundles**
them into a few optimised files. That is the "many files become fewer files"
idea. Even then, `index.html` stays the front door and loads the bundle.

## Key points

- HTML = structure, CSS = style, JavaScript = action.
- The server opens `index.html` first. It then points to every other file.
- The browser downloads each file separately. See them in the Network tab.
