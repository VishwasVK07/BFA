# 3. CSS: make it look like Linktree

Same `index.html` as before, plus one new line in the `<head>` and one new
file, [`style.css`](style.css). **Tada**: the plain page becomes the Linktree.

```html
<link rel="stylesheet" href="style.css" />
```

We write `style.css` in two parts. The finished file has both.

## Part 1: how it looks

### A rule

```css
.card {
  padding: 32px;
  border-radius: 16px;
}
```

`.card` is the **selector** (which elements), `padding` is the **property**
(what to change), `32px` is the **value**.

### Selectors

| Selector | Matches |
|----------|---------|
| `p` | every `<p>` (a tag) |
| `.card` | every element with `class="card"` |
| `#theme-btn` | the one element with `id="theme-btn"` |
| `.link img` | an `<img>` **inside** a `.link` |
| `.link:hover` | a link while the mouse is over it |

These are the same selectors `querySelector` uses in JavaScript. Use classes
most of the time.

### Order we type it in

1. `:root` **variables** (colours in one place), then `* { box-sizing: border-box; }`.
2. `body`: font, background, text colour, `margin: 0`.
3. `.card`: background, border, rounded corners, padding, `text-align: center`.
4. `.avatar`: size, `border-radius: 50%` (a circle), `object-fit: cover`.
5. `h1`, `.role`, `.bio`.
6. `.link`: padding, border, rounded, no underline. Add `.link:hover`.
7. `.link img` size, `.footer`, `button` and `button:hover`.

Try each value in DevTools first (right-click, Inspect, Styles), then copy it.

### The box model

Every element is a box: **content**, then **padding** (space inside), then
**border**, then **margin** (space outside). Inspect an element and look at
the coloured box in the Computed tab.

## Part 2: layout (flexbox)

By default elements stack top to bottom. **Flexbox** lines them up. Put
`display: flex` on the **parent**.

```css
.links {
  display: flex;
  flex-direction: column;   /* stack in a column */
  gap: 12px;                /* space between children */
}
.link {
  display: flex;
  align-items: center;      /* icon and label line up */
  gap: 14px;
}
```

| Property | What it does |
|----------|--------------|
| `display: flex` | children line up in a row |
| `flex-direction: column` | children stack instead |
| `justify-content` | spread along the main direction (`center`, `flex-end`, `space-between`) |
| `align-items` | line up the other way (`center`) |
| `gap` | space between children |

Also in Part 2:
- `body` as flex with `justify-content: center; align-items: center;` to centre the card.
- `.page` with `max-width: 420px` so it does not stretch on a wide screen.
- `.top-bar` with `justify-content: flex-end` to put the button on the right.
- `list-style: none` on `.links` to remove the bullets.

### Phones: media query

```css
@media (max-width: 380px) {
  .card { padding: 20px; }
}
```

Rules inside only apply on small screens. Test with DevTools device mode (the
phone icon). The `viewport` meta tag from topic 2 makes this work.

### Grid (homework)

`display: grid` with `grid-template-columns: repeat(3, 1fr)` makes columns. Use
it in homework 2 (the gallery).

## Try it

Open `index.html`, then change the `--brand` variable and watch the whole page
change colour.

## Key points

- A rule is `selector { property: value; }`. Use classes.
- Variables keep colours in one place, and dark mode uses them next.
- Every element is a box. Flexbox lines boxes up. `gap` spaces them.
- Test with DevTools before writing it into the file.
