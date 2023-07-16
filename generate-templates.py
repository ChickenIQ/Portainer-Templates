import json
from jsonmerge import Merger
import os

base = json.load(open("base/base.json", "r"))

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
                  " with " + template["merge"])

            base["templates"].append(merger.merge(json.load(
                open(os.path.join("base", template["merge"]), "r")), template["data"]))

# Save templates
with open('templates.json', 'w') as outfile:
    json.dump(base, outfile, indent=4)

print("Templates generated successfully!")
