#!/bin/sh

read -p "Commit message: " message
message=${message:-Update}

git add .
git commit -m "$message"
git push

echo -e "\nUpdate complete!"
