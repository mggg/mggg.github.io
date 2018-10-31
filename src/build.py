import csv
import itertools


def render_cell(item, link=None):
    if item == "":
        item = "?"
    if item == "?":
        return '<td class="unknown">?</td>'
    try:
        parsed_content = "{:,d}".format(int(item))
    except ValueError:
        parsed_content = item

    if link is not None:
        parsed_content = '<a href="{link}">{content}</a>'.format(
            content=parsed_content, link=link
        )
    return "<td>{}</td>".format(parsed_content)


links = {
    ("4x4", "4"): "/metagraph/",
    ("5x5", "5"): "/metagraph/5x5.html",
    ("7x7", "7"): "/metagraph/7x7.html",
}


def get_row_label(grid, parts):
    content = "{grid} &rarr; {parts}".format(grid=grid, parts=parts)
    return "<th>{}</th>".format(content)


def render_row(row, links=links):
    grid, parts = str(row[0]), str(row[1])
    row_label = get_row_label(grid, parts)
    row_cells = [render_cell(item) for item in row[2:]]

    if (grid, parts) in links:
        row_cells[0] = render_cell(row[2], link=links[(grid, parts)])

    return "<tr>" + row_label + "".join(row_cells) + "</tr>"


def thead():
    return """
    <colgroup class="row-labels"></colgroup>
    <colgroup class="rook" span="5"></colgroup>
    <colgroup class="queen" span="5">
    </colgroup>
    <thead>
      <tr>
        <th></th>
        <th colspan="5" scope="colgroup" class="rook-heading">Rook</th>
        <th colspan="5" scope="colgroup" class="queen-heading">Queen</th>
      </tr>
      <tr>
        <th></th>

        <th class="rook-label">equal size</th>
        <th class="rook-label">&plusmn; 1</th>
        <th class="rook-label">&plusmn; 2</th>
        <th class="rook-label">&plusmn; 3</th>
        <th class="rook-label">all, non-&empty;</th>

        <th class="queen-label">equal size</th>
        <th class="queen-label">&plusmn; 1</th>
        <th class="queen-label">&plusmn; 2</th>
        <th class="queen-label">&plusmn; 3</th>
        <th class="queen-label">all, non-&empty;</th>
      </tr>
    </thead>"""


def tbody(rows):
    return "<tbody>\n" + "\n".join(render_row(row) for row in rows) + "\n</tbody>"


def table(rows):
    row_sets = [
        list(group) for key, group in itertools.groupby(rows, lambda row: row[0])
    ]
    return (
        "<table>\n"
        + thead()
        + "\n"
        + "\n".join(tbody(row_set) for row_set in row_sets)
        + "\n</table>"
    )


def render_template(template_stream, *args, **template_fields):
    document = "".join(template_stream)
    for key, value in template_fields.items():
        document = document.replace("{{" + key + "}}", value)
    return document


def build_template(
    data_path="../_data/table.csv", output_path="../_includes/metagraph-table.html"
):
    with open(data_path) as f:
        next(f)
        rows = csv.reader(f)
        table_html = table(rows)

    with open(output_path, "w") as f:
        f.write(
            """
<style>
{% include table.css %}
</style>

<div class="table-container">
"""
        )
        f.write(table_html)
        f.write("\n</div>")


def main():
    build_template()


if __name__ == "__main__":
    main()
