import os
import json
from jsonmerge import Merger


def generate_templates(config):
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

    print("Generating templates...\n")
    # Load and merge templates
    for root, files in os.walk("templates"):
        for file in files:
            if file.endswith(".json") and ".merge" not in file:
                with open(os.path.join(root, file), "r") as template:
                    base["templates"].append(json.load(template))
            else:
                template = json.load(open(os.path.join(root, file), "r"))
                base["templates"].append(
                    merger.merge(
                        json.load(open(os.path.join("base", template["merge"]), "r")),
                        template["data"],
                    )
                )

    # Replace variables in templates
    template = json.dumps(base, indent=4)
    for setting in config:
        template = template.replace(f"${setting.upper()}", config[setting])

    return template


if __name__ == "__main__":
    templates = generate_templates(json.load(open("config.json")))
    with open("templates.json", "w") as file:
        file.write(templates)

    print("\nTemplates generated successfully!\n")
