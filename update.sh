#!/bin/sh

read -p "Commit message: " message
echo -e "\n"
message=${message:-Update}

python generate-templates.py
git add .
git commit -m "$message"
git push

echo -e "\nUpdate complete!"
