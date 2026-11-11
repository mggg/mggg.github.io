# Project Map

The Projects page (`/projects`, "Project Map" in the sub-navigation) shows the
places the lab has studied: a US map with a pin or outlined state for each one, a two-level legend that filters by kind of work and governing body,
and a card per project. Everything on it comes from one data file,
`_data/projects.yml`; adding a project never requires touching HTML, CSS, or
JavaScript.

This guide covers:

1. [How it fits together](#how-it-fits-together)
2. [Adding a project](#adding-a-project)
3. [Finding coordinates](#finding-coordinates)
4. [Adding a study to an existing project](#adding-a-study-to-an-existing-project)
5. [Adding national or international work](#adding-national-or-international-work)
6. [Adding a category](#adding-a-category)
7. [Legend groups](#legend-groups)
8. [Previewing](#previewing)
9. [Limitations](#limitations)
10. [Checklist](#checklist)

## How it fits together

| File | What it is | Edit it when… |
|---|---|---|
| `_data/projects.yml` | Every project and study, plus the category list | Adding or changing a project, study, or category |
| `_data/us_map.json` | Pre-projected state outlines and the projection settings (`insets`) | Never by hand; regenerate it if the map itself must change |
| `_category_pages/projects.md` | The page: title, sub-nav label, and intro text | Changing the intro |
| `_includes/projects.html` | Assembles the map, count line, and card list | Only to change the design |
| `_includes/projects/map.html` | Map, legend/filter, and hover popup markup | Only to change the design |
| `_includes/projects/card.html` | One card | Only to change the design |
| `_includes/projects/sidecar.html` | The National/International list beside the map | Only to change the design |
| `_includes/projects/script.html` | Places pins, filters, runs the popup and the sidecar dropdowns | Only to change behavior |
| `_sass/components/_projects.scss` | Styles, including each category's color (`$projects-type-colors`) | Changing a category's color, or the design |

When the site builds, Jekyll turns each entry into a card and either outlines
its state (statewide studies) or records its coordinates (local studies). In the
browser, the script projects those coordinates onto the map to place the pins,
nudging overlapping pins apart and drawing a short leader line back to the true
spot.

## Adding a project

Add an entry under `projects:` in `_data/projects.yml`. Cards are sorted by
`name`, so the entry can go anywhere in the list, though keeping the file
alphabetical makes it easier to scan.

First decide the **scope**:

- **`statewide`**: the work covers a whole state (a congressional or legislative
  plan, statewide redistricting). The state gets a border in its category's
  color, or a border split diagonally into all of their colors if it has
  several (50/50, corner to corner, for two).
- **`local`**: the work covers a city, county, school district, or similar. A pin
  is placed at the entry's coordinates.

A local project in a state that also has a statewide entry is fine: the state is
outlined and the pin sits on top of it.

### Statewide example

```yaml
  - id: georgia
    name: Georgia
    state: GA
    scope: statewide
    types: [congressional]
    description: One or two sentences on the work, in plain language.
    studies:
      - title: Georgia congressional analysis
        year: 2026
        url: /posts/georgia-congressional
```

### Local example

```yaml
  - id: san-diego-ca
    name: San Diego, California
    state: CA
    scope: local
    lat: 32.716
    lon: -117.161
    types: [city-council]
    description: Simulations of how alternative election systems would perform for the San Diego City Council.
    studies:
      - title: San Diego City Council Election Analysis
        year: 2026
        url: https://mggg.github.io/San-Diego-Election-Analysis/
```

### Fields

| Field | Required | Notes |
|---|---|---|
| `id` | yes | Unique, lowercase, hyphens. Becomes the card's anchor (`/projects#san-diego-ca`); map pins and outlined states link to it. For local entries, end with the state code (`beaverton-or`) |
| `name` | yes | Card title, popup title, and sort key. Cities: `City, State`; counties: `Name County, State`; states: the state name |
| `state` | yes | Two-letter postal code. Sets the card's locator map, and for statewide entries, which state is outlined |
| `scope` | yes | `statewide` or `local` |
| `lat`, `lon` | local only | Decimal degrees. See [Finding coordinates](#finding-coordinates) |
| `types` | yes | One or more category keys from `filter_groups` (see [Legend groups](#legend-groups)), e.g. `[city-council]` or `[congressional, expert-report]`. They also decide which legend group the project falls under (see [Legend groups](#legend-groups)). The **first** sets a pin's color; a statewide entry with several gets a border split diagonally into their colors, the first at top left, in the order listed |
| `description` | yes | *(markdown)* One or two sentences on the work there |
| `studies` | yes | List of studies; see below |
| `image` | no | Path to a header image (e.g. `/uploads/…`). Without it, the card shows a locator map of the state with a dot for local entries |

Each study has:

| Field | Required | Notes |
|---|---|---|
| `title` | yes | Link text. Quote it if it contains `": "`, e.g. `"Mathematics of Nested Districts: The Case of Alaska"` |
| `year` | no | Shown after the link in parentheses |
| `url` | yes | A page on this site (`/posts/…`, `/publications/….pdf`) or a full external URL (`https://…`). Prefer the page that presents the study; link a PDF only if there's no such page |

Studies are listed in the order written; oldest first matches the existing
entries.

Write descriptions in plain language for a general reader. Markdown works
(`*italic*` for case names, `[text](url)` for links), and a value containing
`": "` must be quoted.

## Finding coordinates

Coordinates are entered by hand; nothing looks them up automatically.

1. Find the place in Google Maps, right-click the spot, and click the
   coordinates at the top of the menu to copy them (`32.7157, -117.1611`).
   Wikipedia's infobox coordinates work too.
2. The first number is `lat`, the second `lon`. Longitudes in the US are
   **negative**; a positive `lon` places the pin far off the map.
3. Round to three decimal places. That is about 100 m, far finer than the map
   can show: one map unit is roughly 6 km, and a pin is about 66 km across.

What point to pick:

- **City**: the city center or downtown (city hall is a good choice).
- **County or school district**: roughly the middle of its area, or the main city
  if most of the population is there.

Pins that land close together (the Portland suburbs, for example) are spread
apart automatically, with leader lines back to their true positions, so there's
no need to adjust coordinates to avoid overlap.

## Adding a study to an existing project

Add an item to that project's `studies` list, and update its `description` if
the new work changes the summary. Don't create a second entry for the same
place: it would make a second card and a second pin.

## Adding national or international work

Work that isn't tied to one place (UK Boundaries, the Fair Representation Act,
the data practices notes) is listed beside the map rather than on it, and gets
a card in the list below like any project. It lives
under `beyond_map:` at the bottom of `_data/projects.yml`, in groups:

```yaml
beyond_map:
  - label: International
    items:
      - id: uk-boundaries
        name: UK Boundaries
        description: One or two sentences on the work.
        studies:
          - title: UK Boundaries
            year: 2025
            url: /posts/uk-boundaries
```

Add an item to a group's `items`, or add a new group with its own `label`.

- **Beside the map**, each group is a dropdown section, closed to start, and
  only one can be open at a time. It lists each item's `name` and study links
  (like the map's hover popup), in the order listed. The list is never taller
  than the map and scrolls if an open section needs more room.
- **In the card list**, each item gets a card sorted in by `name`, with its
  `description`, its studies, and its group's label as both the header and a
  badge. Like projects, they can take `types`, which place them in the
  legend's groups (the Fair Representation Act has `[congressional]`, so it
  shows under Election Modeling); items without any fall under the `untyped` group, Other. Types
  here don't put anything on the map.

Items take `id`, `name`, `description`, `studies`, and optionally `types`, but
no `state`, `scope`, coordinates, or `image`. The `id` is the
card's anchor (`/projects#uk-boundaries`), so it must not match any project's.

A study can appear in both places. The Fair Representation Act is listed here
as national work and also under its five focus states on the map.

## Adding a category

A category has two parts: its entry in a legend group in `filter_groups` in
`_data/projects.yml`, and its color in `_sass/components/_projects.scss`.

```yaml
filter_groups:
  - key: election-modeling
    label: Election Modeling
    types:
      - key: city-council
        label: City Council
```

```scss
$projects-type-colors: (
  "city-council": #9e4ae6,
  …
);
```

To add one:

1. Add it to the `types` of the legend group it belongs in (see
   [Legend groups](#legend-groups)), with a new `key` (lowercase, hyphens) and
   a `label` for the legend and badges. Every category must be in a group, or
   its badges show no label and no filter selects it.
2. Add the same key with its color to `$projects-type-colors`. Every element
   tagged with that key (`data-type="city-council"`) picks the color up: pins,
   state borders, legend swatches, badges, and card locator dots. A key missing
   from the list shows in gray.

The legend button, its count, and its swatches are generated automatically.
To change a category's color, edit only `$projects-type-colors`.

The colors come from the Districtr palette that the newsletter also uses
(`$newsletter-accents` in `_sass/components/_newsletter.scss`). Lime (`#a3cc3f`)
and magenta (`#bd2795`) are the accents still free. Beyond that,
pick a color that stays distinct from the others and from the gray of unstudied
states, and consider adding it to `$newsletter-accents` so the two stay in step.

## Legend groups

The legend has two levels. The first row is `filter_groups` in
`_data/projects.yml`, one selectable at a time; each group lists its
categories, which make up the second row:

```yaml
filter_groups:
  - key: election-modeling
    label: Election Modeling
    types:
      - key: city-council
        label: City Council
      - key: school-board
        label: School Board
      …
  - key: expert-reports
    label: Expert Reports
    types:
      - key: expert-report
        label: Expert Report
  - key: other
    label: Other
    untyped: true
    types:
      - key: redistricting
        label: Redistricting
```

- A project (or national/international item) is in a group if it has any of
  the group's `types`, so it can be in more than one: Texas has both FRA
  modeling and an expert report, `[congressional, expert-report]`.
- `untyped: true` also puts everything with no `types` in that group (UK
  Boundaries and Data & Data Practices, in Other).
- A group with more than one type opens a second row of those types when it's
  selected, to narrow it further (any of the selected types). Groups with one
  type don't need one.
- The order here is the order on the legend and in each group's row of colored
  dots.
- Counts on the buttons are cards, including national/international ones.

## Previewing

```sh
bundle exec jekyll serve
```

Open `http://localhost:4000/projects` and check:

- The count line ("Showing all N projects") went up by the number of new
  studies. It counts studies, not cards, and a study linked from several cards
  (same `url`) counts once.
- The pin is in the right place, or the right state is outlined, in the right color.
- Hovering the pin or state shows a popup with the project's name and its study
  links, and clicking it jumps to the card.
- The card's locator map shows the right state, with a dot in the right spot for
  local entries.
- The card reads well in all three layouts above the list: Grid, Icons (smaller,
  without the description), and List (one per row). Visitors' choice is
  remembered in their browser, so switch back to check the others. Screens
  900px wide or narrower always show Grid, with no switcher.
- Each legend group and type that includes the project shows and hides it.
- Every study link opens the right page.

If the page looks unstyled after switching branches, hard-reload (⌘⇧R). The
stylesheet URL now changes on every build, so this should be rare.

If the build fails, the usual cause is a YAML error in `_data/projects.yml`:
the message gives a line number, and it's most often an unquoted value containing
`": "`.

## Limitations

- **One statewide entry per state.** The map outlines and links a state for its
  first statewide entry only. Put all statewide work for a state in one entry
  with several `studies` and `types`.
- **US states, DC, and Puerto Rico only on the map.** Other places have no outline in
  `_data/us_map.json`, so there's no locator map, and pins outside the map's
  areas (the lower 48, Alaska, Hawaii, Puerto Rico) won't be placed correctly.
  List work elsewhere beside the map instead (see
  [Adding national or international work](#adding-national-or-international-work)).
- **The map data and the script must agree.** The `insets` in
  `_data/us_map.json` are the projection settings the script uses to place pins.
  If the map is ever regenerated with different settings, update `insets` with
  it or every pin will be misplaced.

## Checklist

- [ ] Entry added under `projects:` with a unique `id`
- [ ] `scope` set; local entries have `lat` and a **negative** `lon`
- [ ] `types` uses existing keys, with the main one first
- [ ] Description written; values containing `": "` are quoted
- [ ] Every study has a `title` and a working `url`
- [ ] Previewed `/projects`: pin or state, popup, card, filters, and links
