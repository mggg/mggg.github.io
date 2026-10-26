# Location mapping

The Locations page (`/locations`) shows the places the lab has studied: a US map
with a pin or shaded state for each one, a legend that filters by governing body,
and a card per location. Everything on it comes from one data file,
`_data/locations.yml`; adding a location never requires touching HTML, CSS, or
JavaScript.

This guide covers:

1. [How it fits together](#how-it-fits-together)
2. [Adding a location](#adding-a-location)
3. [Finding coordinates](#finding-coordinates)
4. [Adding a study to an existing location](#adding-a-study-to-an-existing-location)
5. [Adding a category](#adding-a-category)
6. [Previewing](#previewing)
7. [Limitations](#limitations)
8. [Checklist](#checklist)

## How it fits together

| File | What it is | Edit it when… |
|---|---|---|
| `_data/locations.yml` | Every location and study, plus the category list | Adding or changing a location, study, or category |
| `_data/us_map.json` | Pre-projected state outlines and the projection settings (`insets`) | Never by hand; regenerate it if the map itself must change |
| `_category_pages/locations.html` | The page: title and intro text | Changing the intro |
| `_includes/locations.html` | Assembles the map, count line, and card list | Only to change the design |
| `_includes/locations/map.html` | Map, legend/filter, and hover popup markup | Only to change the design |
| `_includes/locations/card.html` | One card | Only to change the design |
| `_includes/locations/script.html` | Places pins, filters, runs the popup | Only to change behavior |
| `_sass/components/_locations.scss` | Styles | Only to change the design |

When the site builds, Jekyll turns each entry into a card and either shades its
state (statewide studies) or records its coordinates (local studies). In the
browser, the script projects those coordinates onto the map to place the pins,
nudging overlapping pins apart and drawing a short leader line back to the true
spot.

## Adding a location

Add an entry under `locations:` in `_data/locations.yml`. Cards are sorted by
`name`, so the entry can go anywhere in the list, though keeping the file
alphabetical makes it easier to scan.

First decide the **scope**:

- **`statewide`**: the work covers a whole state (a congressional or legislative
  plan, statewide redistricting). The state is shaded on the map in its
  category's color, or striped in all of their colors if it has several.
- **`local`**: the work covers a city, county, school district, or similar. A pin
  is placed at the entry's coordinates.

A local location in a state that also has a statewide entry is fine: the state is
shaded and the pin sits on top of it.

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
| `id` | yes | Unique, lowercase, hyphens. Becomes the card's anchor (`/locations#san-diego-ca`); map pins and states link to it. For local entries, end with the state code (`beaverton-or`) |
| `name` | yes | Card title, popup title, and sort key. Cities: `City, State`; counties: `Name County, State`; states: the state name |
| `state` | yes | Two-letter postal code. Sets the card's locator map, and for statewide entries, which state is shaded |
| `scope` | yes | `statewide` or `local` |
| `lat`, `lon` | local only | Decimal degrees. See [Finding coordinates](#finding-coordinates) |
| `types` | yes | One or more category keys from `types:` at the top of the file, e.g. `[city-council]` or `[congressional, state-legislature]`. The **first** sets a pin's color; a statewide entry with several is striped in all of their colors, in the order listed |
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

## Adding a study to an existing location

Add an item to that location's `studies` list, and update its `description` if
the new work changes the summary. Don't create a second entry for the same
place: it would make a second card and a second pin.

## Adding a category

Categories live under `types:` at the top of `_data/locations.yml`:

```yaml
types:
  - key: city-council
    label: City Council
    color: "#4396c8"
```

To add one, add an entry with a new `key` (lowercase, hyphens), a `label` for
the legend and badges, and a `color`. The legend button, its count, and its
swatches are generated automatically.

The colors come from the Districtr palette that the newsletter also uses
(`$newsletter-accents` in `_sass/components/_newsletter.scss`). Six of its seven
colors are taken; coral (`#eb8777`) is free for the next category. Beyond that,
pick a color that stays distinct from the others and from the gray of unstudied
states, and consider adding it to `$newsletter-accents` so the two stay in step.

## Previewing

```sh
bundle exec jekyll serve
```

Open `http://localhost:4000/locations` and check:

- The count line ("Showing all N locations") went up by one.
- The pin is in the right place, or the right state is shaded, in the right color.
- Hovering the pin or state shows a popup with the location's name and its study
  links, and clicking it jumps to the card.
- The card's locator map shows the right state, with a dot in the right spot for
  local entries.
- Each legend filter that includes the location shows and hides it.
- Every study link opens the right page.

If the page looks unstyled after switching branches, hard-reload (⌘⇧R). The
stylesheet URL now changes on every build, so this should be rare.

If the build fails, the usual cause is a YAML error in `_data/locations.yml`:
the message gives a line number, and it's most often an unquoted value containing
`": "`.

## Limitations

- **One statewide entry per state.** The map shades and links a state for its
  first statewide entry only. Put all statewide work for a state in one entry
  with several `studies` and `types`.
- **US states, DC, and Puerto Rico only.** Other places have no outline in
  `_data/us_map.json`, so there's no locator map, and pins outside the map's
  areas (the lower 48, Alaska, Hawaii, Puerto Rico) won't be placed correctly.
- **The map data and the script must agree.** The `insets` in
  `_data/us_map.json` are the projection settings the script uses to place pins.
  If the map is ever regenerated with different settings, update `insets` with
  it or every pin will be misplaced.

## Checklist

- [ ] Entry added under `locations:` with a unique `id`
- [ ] `scope` set; local entries have `lat` and a **negative** `lon`
- [ ] `types` uses existing keys, with the main one first
- [ ] Description written; values containing `": "` are quoted
- [ ] Every study has a `title` and a working `url`
- [ ] Previewed `/locations`: pin or state, popup, card, filters, and links
