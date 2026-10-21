# Newsletter

The quarterly newsletter lives on the site at `/newsletter`. All of its content is
driven by YAML data files; you shouldn't need to touch any HTML or CSS to publish
a new issue.

This guide covers:

1. [How it fits together](#how-it-fits-together)
2. [Adding a new issue](#adding-a-new-issue)
3. [Writing the content](#writing-the-content)
4. [Navigation and links](#navigation-and-links)
5. [Announcing the issue with a post](#announcing-the-issue-with-a-post)
6. [Previewing locally](#previewing-locally)
7. [Checklist](#checklist)

## How it fits together

| File | What it is | Edit it when… |
|---|---|---|
| `_data/newsletters/<issue>.yml` | All the content for one issue | Every issue (new file) |
| `newsletters/<issue>.md` | A tiny page that publishes that issue at `/newsletter/<issue>` | Every issue (new file) |
| `newsletter.md` | The `/newsletter` page; always shows the issue with the latest `date` | Never |
| `_posts/<date>-<issue>-newsletter.md` | The announcement on the Latest Updates page | Every issue (new file) |
| `_data/navigation.yml` | Top navigation; already links to `/newsletter` | Never |
| `_layouts/newsletter.html` | Page structure: header, table of contents, sections, footer | Only to change the design |
| `_includes/newsletter/*.html` | One template per block (callout, software item, event, job, research item, …) | Only to change the design |
| `_sass/components/_newsletter.scss` | Newsletter styles | Only to change the design |
| `documentation/newsletter.yml.example` | Blank template for a new issue | When adding new fields |

Each issue has a short **issue key** in the form `<season>-<year>`, e.g. `fall-2026`
or `winter-2027`. The key is used for the YAML filename, the page filename, and the
URL, so keep it lowercase with hyphens.

## Adding a new issue

Using `winter-2027` as the example key:

1. **Create the data file.** Copy the template:

   ```sh
   cp documentation/newsletter.yml.example _data/newsletters/winter-2027.yml
   ```

   Delete the header comment, then fill in every `TODO` (see
   [Writing the content](#writing-the-content)). `grep -n TODO
   _data/newsletters/winter-2027.yml` should come back empty when you're done.

   `date:` is required: it's the publication date, and the issue with the latest
   date is the one shown at `/newsletter`. The subscribe and unsubscribe form URLs
   are pre-filled; change them only if the forms change.

2. **Create the issue page** at `newsletters/winter-2027.md`:

   ```yaml
   ---
   title: Winter 2027 Newsletter
   layout: newsletter
   issue: winter-2027
   permalink: /newsletter/winter-2027
   ---
   ```

   `issue` must match the YAML filename (without `.yml`). This page gives the issue
   a permanent URL, so links to it keep working after the next issue comes out.

3. **Announce it** with a post (see [below](#announcing-the-issue-with-a-post)).

4. **Preview, then commit** all three files together.

Older issues need no changes: they stay available at their own URLs.

## Writing the content

Open `documentation/newsletter.yml.example` alongside this section. Every field is
also annotated there, and every value you need to write is marked `TODO`.

### General rules

- **Markdown.** Fields marked *(markdown)* accept `**bold**`, `*italic*`,
  `` `code` ``, and `[link text](https://…)`. Other fields are plain text.
- **Multi-paragraph text** uses a block with a blank line between paragraphs:

  ```yaml
  body: |
    First paragraph.

    Second paragraph.
  ```

- **Quote values that YAML would misread:** anything containing `": "`, or starting
  with `#`, `*`, `@`, `&`, `!`, `[`, `{`, `>`, `|`, or a quote character.
  A sentence ending in a colon is the most common case:
  `description: "New features include:"`.
- **Unfinished links.** A link whose `url:` is empty is not shown, so you can leave
  `url:  # TODO …` in place until the real link is ready. Remember it will be
  missing from the page until you fill it in.
- **Order.** Sections appear in the order they're listed, and so do items within a
  section.

### Issue-level fields

| Field | Required | Notes |
|---|---|---|
| `title` | yes | e.g. `Winter 2027` |
| `date` | yes | `YYYY-MM-DD`. The newest date is shown at `/newsletter` |
| `toc_title` | no | Heading above the table of contents. Default: "Contents" |
| `header.eyebrow` / `header.issue` | yes | Small text above the title (left / right) |
| `header.title` | yes | Large title |
| `header.subtitle` | no | Line under the title |
| `header.image` / `header.image_alt` | no | Image shown below the header, scaled to fit (up to 25rem tall; 10rem on phones). Put the file in `_uploads/` and use a path like `/uploads/georgia-graph.png`. Always set `image_alt` |
| `subscribe.label` / `subscribe.url` | if any callout uses `show_subscribe` | The subscribe button |
| `footer` | no | `lines` (plain text), `links` (`label` + `url`), `copyright` |

### Sections

`sections` is a list. Each entry has a `type`, which is one of `callout`,
`software`, `events`, `jobs`, `research`, or `outreach`. You can repeat types, leave
any out, and reorder them freely.

These fields work on **any** section:

| Field | Notes |
|---|---|
| `toc` | Label in the table of contents. Defaults to `heading`. A section with neither isn't listed |
| `id` | Anchor for links like `/newsletter/winter-2027#jobs`. Defaults to the heading, slugified |

These work on **software, events, jobs, research, and outreach** sections:

| Field | Notes |
|---|---|
| `heading` | Section title (required) |
| `tinted` | `true` for a light blue-gray background. Alternating helps break up the page |
| `color` | Accent for the pill beside the heading, bullet points, and event card stripes: `blue`, `yellow`, `green`, `lime`, `magenta`, `purple`, or `coral`. Default: dark blue. The colors are defined in `$newsletter-accents` in `_sass/components/_newsletter.scss` |
| `collapsible` | `true` lets readers open and close the section by clicking its heading. The colored pill beside the heading becomes an arrow |
| `open` | With `collapsible`, `true` starts it expanded |
| `closing` | *(markdown)* Text after the items, e.g. thanks or a feedback address |
| `link` | `label` + `url`, shown after the closing text |

#### `callout`

A tinted block with a large pull quote. Use it for the introduction and sign-off.

| Field | Notes |
|---|---|
| `pullquote` | Large headline sentence |
| `body` | *(markdown)* |
| `show_subscribe` | `true` adds the subscribe button |
| `toc` | Set this if the callout should appear in the table of contents |

#### `software`

Each item is an accordion: readers see only the version badge and project name until
they click to expand it.

| Item field | Notes |
|---|---|
| `name` | Project name (required) |
| `version` | Badge text, e.g. `v2.0` |
| `color` | Badge and bullet color, from the same list as the section `color`. Give each project its own |
| `open` | `true` to start expanded |
| `description` | *(markdown)* Shown before the bullets |
| `features` | List of bullets, each *(markdown)* |
| `note` | *(markdown)* Shown after the bullets |
| `link` | `label` + `url` |

The section itself can also be `collapsible`; readers then open the section by
its heading, and each project within it separately.

#### `events`

One card per talk or event, in the order listed (chronological is usually best).

| Item field | Notes |
|---|---|
| `format` | `in-person`, `hybrid`, or `remote`. Sets the card and badge color |
| `badge` | Badge text, e.g. `In Person`, `In Person + Zoom`, `Remote` |
| `when` | List of pieces, joined with " · " (date, time, place) |
| `speaker` | Speaker name |
| `affiliation` | Speaker's title and institution |
| `title` | Talk title (shown in italics) |
| `description` | *(markdown)* |
| `links` | List of `label` + `url`. Add `secondary: true` for a lighter link (e.g. Zoom) |

#### `jobs`

| Item field | Notes |
|---|---|
| `title` | Job title |
| `meta` | List, joined with " · " (e.g. Full-time · University of Chicago · Open until filled) |
| `description` | *(markdown)* |
| `link` | `label` + `url`, e.g. Apply |

#### `research` and `outreach`

One entry per paper, project, partnership, or other piece of work. Both types take
the same item fields; use `research` for research output and `outreach` for
partnerships and community work.

| Item field | Notes |
|---|---|
| `name` | Title, e.g. `Chicago City Council (July 2026)` |
| `description` | *(markdown)* A sentence or two on what it found |
| `link` | `label` + `url`, e.g. See paper |

## Navigation and links

- **Top navigation.** The "Newsletter" item in `_data/navigation.yml` points to
  `/newsletter`, which always shows the issue with the latest `date`. Publishing a
  new issue updates it automatically; don't add a nav item per issue.
- **Table of contents.** The sidebar is built from the YAML: every section with a
  `heading` (or a `toc` label) gets an entry that jumps to it and highlights while
  you're reading it. Rename an entry with `toc:`; leave a callout out by omitting
  `toc:`.
- **Linking to an issue** from anywhere else (posts, emails, Slack): use the
  permanent URL `/newsletter/<issue>`, not `/newsletter`, which will move on to the
  next issue. Link to a section with its id, e.g. `/newsletter/fall-2026#jobs`.

## Announcing the issue with a post

Add `_posts/<YYYY-MM-DD>-<issue>-newsletter.md`, e.g.
`_posts/2027-01-15-winter-2027-newsletter.md`:

```markdown
---
title: "Winter 2027 Newsletter"
date: 2027-01-15 00:00:00 Z
categories:
  - news
authors: Data & Democracy Lab
featured: true
href: /newsletter/winter-2027
excerpt_separator: "<!--more-->"
---

One or two sentences on the highlights of this issue. [Read the Winter 2027 newsletter.](/newsletter/winter-2027)
<!--more-->
```

- `categories: news` puts it on the Latest Updates page (`/news`).
- `href` makes the card's title link straight to the newsletter instead of to a
  separate post page.
- The text above `<!--more-->` is the teaser shown on the card.
- A post dated in the future won't be published until a build runs on or after
  that date.

## Previewing locally

```sh
bundle install                # first time only
bundle exec jekyll serve
```

Then open:

- `http://localhost:4000/newsletter`: should show the new issue
- `http://localhost:4000/newsletter/<issue>`: the permanent page
- `http://localhost:4000/news`: the announcement card at the top

Things to check:

- Every section and item appears, in the right order.
- Each table-of-contents entry jumps to its section and highlights while scrolling.
- Software accordions open and close.
- Links go to the right places, and placeholder links are hidden.
- The page looks right on a narrow (phone-width) window.

If the build fails:

- **A YAML error** gives a line number in the data file. The usual cause is an
  unquoted value containing `": "`.
- **`comparison of String with Date failed`** means an issue's `date:` isn't a
  valid `YYYY-MM-DD` date (for example, it's still `TODO-YYYY-MM-DD`).

An issue with no `date:` at all builds, but never appears at `/newsletter`.

## Checklist

- [ ] `_data/newsletters/<issue>.yml` created from the template, with `date` set
- [ ] Header comment deleted, every `TODO` filled in (`grep -n TODO` is empty),
      unused optional fields removed
- [ ] `newsletters/<issue>.md` created, with `issue` matching the YAML filename
- [ ] `_posts/<date>-<issue>-newsletter.md` created, linking to `/newsletter/<issue>`
- [ ] Previewed `/newsletter`, `/newsletter/<issue>`, and `/news` locally
