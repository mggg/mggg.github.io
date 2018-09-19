import csv
import itertools


def render_cell(item):
    if item == "":
        item = "?"
    if item == "?":
        return "<td class=\"unknown\">?</td>"
    try:
        parsed_content = int(item)
        return "<td>{:,d}</td>".format(parsed_content)
    except ValueError:
        parsed_content = item
        return "<td>{}</td>".format(parsed_content)


def get_row_label(grid, parts):
    links = {"4x4": "/metagraph/4x4.html",
             "5x5": "/metagraph/5x5.html", "7x7": "/metagraph/7x7.html"}

    content = "{grid} &rarr; {parts}".format(grid=grid, parts=parts)

    if grid in links:
        content = "<a href=\"{href}\">{content}</a>".format(
            content=content, href=links[grid])
        return "<th class=\"link\">{}</th>".format(content)

    return "<th>{}</th>".format(content)


def render_row(row):
    row_label = get_row_label(row[0], row[1])
    row_cells = [render_cell(item) for item in row[2:]]
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
        <th colspan="5" scope="colgroup">Rook</th>
        <th colspan="5" scope="colgroup">Queen</th>
      </tr>
      <tr>
        <th></th>

        <th>equal size</th>
        <th>&plusmn; 1</th>
        <th>&plusmn; 2</th>
        <th>&plusmn; 3</th>
        <th>all, non-&empty;</th>

        <th>equal size</th>
        <th>&plusmn; 1</th>
        <th>&plusmn; 2</th>
        <th>&plusmn; 3</th>
        <th>all, non-&empty;</th>
      </tr>
    </thead>"""


def tbody(rows):
    return "<tbody>\n" + "\n".join(render_row(row) for row in rows) + "\n</tbody>"


def table(rows):
    row_sets = [list(group)
                for key, group in itertools.groupby(rows, lambda row: row[0])]
    return "<table>\n" + thead() + "\n" + "\n".join(tbody(row_set) for row_set in row_sets) + "\n</table>"


def render_template(template_stream, *args, **template_fields):
    document = "".join(template_stream)
    for key, value in template_fields.items():
        document = document.replace("{{" + key + "}}", value)
    return document


def build_template(template_path="./table_template.html", data_path="./table.csv", output_path="./table.html"):
    with open(data_path) as f:
        next(f)
        rows = csv.reader(f)
        table_html = table(rows)

    with open(template_path) as f:
        document = render_template(f, table=table_html)

    with open(output_path, "w") as f:
        f.write(document)


def main():
    build_template()


if __name__ == '__main__':
    main()
