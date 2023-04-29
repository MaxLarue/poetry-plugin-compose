#!/bin/bash

set -e

echo '####### generate doc'
poetry compose run -d scripts -- python generate_doc.py

echo '####### publishing doc'
poetry compose run -d doc -- mkdocs gh-deploy

echo '####### bump version'
cd plugin
poetry version $1
cd ..
git add .
git commit -m"$1"

echo '####### tagging'
git tag -a v$1 -m v$1

echo '####### publish'
cd plugin
poetry publish --build

echo '####### send tag to git'
git push origin v$1