import json
from jsonmerge import Merger
import os

base = json.load(open("base/base.json", "r"))
config = json.load(open('config.json'))

merger = Merger({
    "properties": {
        "env": {
            "mergeStrategy": "arrayMergeById",
            "mergeOptions": {"idRef": "name"},
        }
    },
})


# Load and merge templates
for root, dirs, files in os.walk("templates"):
    for file in files:
        if file.endswith(".json") and ".merge" not in file:
            print("Adding template: " + file)

            with open(os.path.join(root, file), "r") as template:
                base["templates"].append(json.load(template))
        else:
            template = json.load(open(os.path.join(root, file), "r"))
            print("Merging template: " + file.replace(".merge", "") +
                  " with base file: " + template["merge"])

            base["templates"].append(merger.merge(json.load(
                open(os.path.join("base", template["merge"]), "r")), template["data"]))


# Replace variables in templates
template = json.dumps(base, indent=4)
for setting in config:
    template = template.replace(f"${setting.upper()}", config[setting])

# Write templates to templates.json
with open("templates.json", "w") as file:
    file.write(template)


print("Templates generated successfully!")
