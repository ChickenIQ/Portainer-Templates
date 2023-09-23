#!/bin/sh

read -p "Commit message: " message
message=${message:-Update}

python3 update.py
git add .
git commit -m "$message"
git push

echo -e "\nUpdate complete!"
