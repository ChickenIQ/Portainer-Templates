import json
import os

base = {
    "version": "2",
    "templates": []
}

for root, dirs, files in os.walk("templates"):
    for file in files:
        if file.endswith(".json"):
            with open(os.path.join(root, file), "r") as template:
                base["templates"].append(json.load(template))

with open('templates.json', 'w') as outfile:
    json.dump(base, outfile, indent=4)

print("Templates generated successfully!")
