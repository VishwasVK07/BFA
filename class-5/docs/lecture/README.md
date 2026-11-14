# Class 5 lecture notes: HTML, CSS and JavaScript for the browser

Everything we show in class lives here, one numbered folder per topic (1 to 4).
Each folder has a `README.md` with the notes. The numbers match the headings on
the slides.

> Class 3 taught what JavaScript is and where it runs. Class 4 built the
> backend. Today is the **frontend**: the three languages every web page is
> made of, used to build one small page, live, together.

## What we build

A **Linktree clone**: a link-in-bio page with a photo, a name, a role, a short
bio, a stack of link buttons with icons (LinkedIn, GitHub, Instagram, email),
and a dark/light mode button. Every student builds it on their own laptop
during class, then makes it theirs. In Class 6 we rebuild the same page in
React, so you see what React improves.

## Topics

Each folder is one stage. The finished code of a stage is in its folder.

| # | Folder | What you learn | Code in the folder |
|---|--------|----------------|--------------------|
| 1 | [`01_web_page`](01_web_page) | What a web page is: HTML, CSS, JS, and why `index.html` is the front door | a tiny hello page (not the Linktree) |
| 2 | [`02_html`](02_html) | The tags we use, and the static Linktree | `index.html` and `images/` |
| 3 | [`03_css`](03_css) | `style.css`: looks and flexbox layout | `index.html`, `style.css`, `images/` |
| 4 | [`04_javascript`](04_javascript) | Dark and light mode with vanilla JS | the finished Linktree |

After the four topics we check the page, push it to GitHub and look ahead to
React (Class 6). Those are on the last slides only, with no folder.

We do **not** memorise every tag or CSS property. We learn the core ones by
building, and the rest is homework and a reference you can look up or ask AI
about. If you fall behind during the live build, copy the files from the folder
of the stage you are on and keep going.

## Mac and Windows cheat sheet

| What | Mac | Windows |
|------|-----|---------|
| Open an HTML file in the browser | `open index.html` | `start index.html` |
| Open DevTools | `Cmd + Option + I` | `F12` or `Ctrl + Shift + I` |
| Hard refresh (ignore the cache) | `Cmd + Shift + R` | `Ctrl + Shift + R` |
| Save the file in VS Code | `Cmd + S` | `Ctrl + S` |
| Format the file in VS Code | `Shift + Option + F` | `Shift + Alt + F` |
| Comment a line (HTML, CSS, JS) | `Cmd + /` | `Ctrl + /` |

The workflow all day is: **edit, save, refresh the browser**. If you change
a file and nothing changes on the page, you forgot to save, or you are
looking at a different tab.

## Before you start

- Chrome or Edge, and VS Code, from Class 1.
- No installs today. HTML, CSS and JavaScript need nothing but a browser and
  an editor.
- Make a folder `my-links` for today and open it in VS Code (File, Open Folder).

## Practice

The practice tasks are in the folders next to this one:
[`../../live-practice`](../../live-practice) and [`../../homework`](../../homework).

The live practices are short and simple. You open a page that already works
and **change values**, then save and refresh:

| # | Live practice | You change |
|---|---------------|------------|
| 1 | `01_my_links` | your photo, name, role, bio and links in the HTML |
| 2 | `02_style_a_card` | `color`, `background`, `font-size`, `border-radius` in `style.css` |
| 3 | `03_dark_mode` | the `body.dark` colours and the button label |
