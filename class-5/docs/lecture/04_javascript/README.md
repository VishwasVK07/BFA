# 4. Vanilla JavaScript: dark and light mode

"Vanilla" means plain JavaScript, no libraries. This is the browser JavaScript
from Class 3 (the DOM), now used on our Linktree page. Three moves:

1. **Find** an element: `document.getElementById("x")`.
2. **Listen** for an event: `element.addEventListener("click", () => { ... })`.
3. **Change** something: `textContent`, `classList`, `value`.

## What we add

1. The CSS for dark mode. Every colour in our CSS comes from a variable, so dark
   mode only needs to swap the variables when `<body>` has the class `dark`:

```css
body.dark {
  --bg: #0f172a;
  --card: #1e293b;
  --text: #e2e8f0;
}
```

2. The script tag, last in the `<body>`:

```html
<script src="script.js"></script>
```

3. [`script.js`](script.js):

```js
const themeBtn = document.getElementById("theme-btn");           // find

themeBtn.addEventListener("click", () => {                       // listen
  document.body.classList.toggle("dark");                        // change
});
```

`classList.toggle("dark")` adds the class if it is missing and removes it if it
is there. One line and the whole page changes.

**The pattern:** JavaScript does not set colours. It switches a class. CSS
decides what that class looks like. Keep the looks in CSS.

The finished `script.js` also changes the button text between "Dark mode" and
"Light mode" with `classList.contains("dark")` and an `if`.

## Try it

Click the button. Open DevTools, Elements: watch `class="dark"` appear and
disappear on `<body>`.

## Debugging checklist

When a button does nothing:
1. Open DevTools, **Console**. Read the red error.
2. `Cannot read properties of null`: the id in JavaScript does not match the id
   in HTML. Check spelling and capital letters.
3. Is `<script src="script.js">` at the **bottom** of `<body>`?
4. Did you save, and hard refresh (`Cmd/Ctrl + Shift + R`)?

## Key points

- Every interaction is find, listen, change.
- To restyle, switch a class with `classList`.
- Console errors tell you what is wrong. Read them first.
