import json
from jsonmerge import Merger
import os

merger = Merger({
    "properties": {
        "env": {
            "mergeStrategy": "arrayMergeById",
            "mergeOptions": {"idRef": "name"},
        }
    },
})

base = {
    "version": "2",
    "templates": []
}

# Load and merge templates
for root, dirs, files in os.walk("templates"):
    for file in files:
        if file.endswith(".json") and ".merge" not in file:
            print("Adding template: " + file)

            with open(os.path.join(root, file), "r") as template:
                base["templates"].append(json.load(template))
        else:
            print("Merging template: " + file.replace(".merge", ""))

            template = json.load(open(os.path.join(root, file), "r"))
            basefile = json.load(
                open(os.path.join("base", template["merge"]), "r"))

            base["templates"].append(merger.merge(basefile, template["data"]))

# Save templates
with open('templates.json', 'w') as outfile:
    json.dump(base, outfile, indent=4)

print("Templates generated successfully!")
