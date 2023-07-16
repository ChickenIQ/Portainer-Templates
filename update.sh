#!/bin/sh

read -p "Commit message: " message
message=${message:-Update}

python generate-templates.py
git add .
git commit -m "$message"
git push

echo "Done"
