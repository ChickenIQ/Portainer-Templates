#!/bin/sh

python generate-templates.py
git add .
git commit -m "Update"
git push
