import os
import json
from jsonmerge import Merger


def generate_templates():
    base = json.load(open("base/base.json", "r"))

    merger = Merger(
        {
            "properties": {
                "env": {
                    "mergeStrategy": "arrayMergeById",
                    "mergeOptions": {"idRef": "name"},
                }
            },
        }
    )
    # Load and merge templates
    for root, dirs, files in os.walk("templates"):
        for file in files:
            template = json.load(open(os.path.join(root, file), "r"))
            if file.endswith(".merge.json"):
                base["templates"].append(
                    merger.merge(
                        json.load(open(os.path.join("base", template["merge"]), "r")),
                        template["data"],
                    )
                )
            else:
                base["templates"].append(template)

    return json.dumps(base, indent=4)


def replace_vars(template, config):
    for setting in config:
        template = template.replace(f"${setting.upper()}", config[setting])
    return template


if __name__ == "__main__":
    templates = replace_vars(generate_templates(), json.load(open("config.json")))
    with open("templates.json", "w") as file:
        file.write(templates)

    print("\nTemplates generated successfully!\n")
