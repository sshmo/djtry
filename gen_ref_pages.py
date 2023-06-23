"""Generate the code reference pages."""

from pathlib import Path

import mkdocs_gen_files

apps = ["djtry", "blog"]

for app in apps:

    for path in sorted(Path(app).rglob("*.py")):

        module_path = path.relative_to(app).with_suffix("")

        doc_path = path.relative_to(app).with_suffix(".md")

        full_doc_path = Path("reference", doc_path)

        parts = list(module_path.parts)

        if parts[-1] == "__init__":

            parts = parts[:-1]
            doc_path = doc_path.with_name("index.md")
            full_doc_path = full_doc_path.with_name("index.md")

        elif parts[-1] == "__main__":
            continue

        with mkdocs_gen_files.open(full_doc_path, "w") as fd:

            identifier = ".".join(parts)

            print(f"::: {app}." + identifier if identifier else f"::: {app}", file=fd)

        mkdocs_gen_files.set_edit_path(full_doc_path, path)
