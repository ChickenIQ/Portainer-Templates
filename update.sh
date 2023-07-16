#!/bin/sh

read -p "Commit message: " message
message=${message:-Update}

python templates.py
git add .
git commit -m "$message"
git push

echo -e "\nUpdate complete!"
