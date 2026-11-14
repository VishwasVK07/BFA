# 2. HTML: build the Linktree structure

Today we build a **Linktree clone**: a link-in-bio page. In this topic we write
**only HTML**. No colours, no layout yet. The result looks plain, and that is
the point: this is the structure.

The finished file is [`index.html`](index.html). We type it together, tag by
tag. Do not copy it. Copy it only for the live practice at the end.

## Set up (2 minutes)

1. Make a folder `my-links` and open it in VS Code.
2. Copy the [`images`](images) folder from here into `my-links`.
3. Create `index.html`, type `!` and press `Tab`. VS Code writes the page
   skeleton. Three lines matter:
   - `<html lang="en">`: the language of the page.
   - `<meta charset="utf-8">`: so letters and emojis show correctly.
   - `<meta name="viewport" ...>`: so the page fits a phone.
4. Change `<title>` to your name. That is the browser tab text.

## The tags we use

Tags are the words in angle brackets. Most come in pairs (`<h1>` ... `</h1>`)
and can sit inside each other.

### Semantic tags: boxes that say what they are

| Tag | What it means |
|-----|---------------|
| `header` | the top part of a page or a card (here: photo, name, role, bio) |
| `nav` | a group of links that take you somewhere |
| `main` | the main content of the page |
| `article` | one card that makes sense on its own |
| `footer` | the bottom part (here: credits) |

**Why semantic?** A `div` looks the same in the browser, but it says nothing.
A `header`, `nav` or `footer` says what the part *is*. That helps:
- **screen readers**, so a blind user can jump straight to the menu or the content;
- **search engines** and the browser's **reader mode**, which find the main content;
- **you, your team and AI**, who read the code faster.

`div` is a plain box with no meaning. Use it only when no semantic tag fits
(here: the top bar that holds the button).

### Text

| Tag | What it means |
|-----|---------------|
| `h1` | the main title. One per page |
| `h2` | a sub-heading under the title |
| `p` | a paragraph |
| `strong` | **bold**, for an important word |
| `em` | *italic*, for an emphasised word |
| `span` | a small piece of text inside a line, with no meaning of its own |

### Lists, links, pictures and buttons

| Tag | What it means |
|-----|---------------|
| `ul` | a bullet list (unordered) |
| `ol` | a numbered list (ordered) |
| `li` | one item in either kind of list |
| `a` | a link. `href` says where it goes |
| `img` | a picture. `src` is the file, `alt` describes it |
| `button` | something the user clicks |

`<a>` (a link you click) is not the same as `<link>` (a line in the `<head>`
that loads a CSS file). We use `<link>` in the next topic.

### Attributes

Extra settings written inside the opening tag: `src="images/avatar.svg"`,
`href="https://github.com/"`, `alt="..."`, `id="theme-btn"`, `class="link"`.
`id` names **one** element. `class` is a label many elements can share. CSS and
JavaScript find elements with them.

## The build order (live)

1. `<main>` with a `<div>` (for the top bar) and an `<article>` (the card).
2. Inside the `div`: a `<button>` for dark mode. It does nothing yet.
3. `<header>`: an `<img>` (your photo), an `<h1>` (name), an `<h2>` (role), a
   `<p>` (bio).
4. `<nav>` with a `<ul>`, and four `<li>`. Each `<li>` holds an `<a>` that has
   an `<img>` (the icon) and a `<span>` (the label).
   You write the same shape four times. Remember this for Class 6.
5. `<footer>` with a `<p>` that uses `<strong>` and `<em>`.

Save and refresh after each step. Open it with `open index.html` (Mac) or
`start index.html` (Windows).

## What you should see

A plain page: a button, a picture, your name, a role, a bio, and four bulleted
links with icons. The links already work.

## Live practice 1

Copy this page into `live-practice/01_my_links/` and make it about you. See
the instructions in that folder's `index.html`.

## Key points

- HTML is the structure: the tags say **what** each piece is.
- `header`, `nav` and `footer` tell the browser (and screen readers) what each
  part is. Use a `div` only when nothing else fits.
- `id` is unique, `class` is reusable.
- Tags nest: `ul` > `li` > `a` > `img` + `span`.
