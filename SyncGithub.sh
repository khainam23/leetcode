#!/bin/bash

git add .

files=$(git status --porcelain | awk '{print $2}')

commit_names=()

while IFS= read -r file; do
    base=$(basename "$file")

    if [[ $base =~ ^[0-9] ]]; then
        name="${base%.*}"
        name="${name//_/ }"
        commit_names+=("$name")
    fi
done <<< "$files"

commit_message=$(IFS=' & '; echo "${commit_names[*]}")

if [ -z "$commit_message" ]; then
    echo "No valid files found."
    exit 1
fi

git commit -m "$commit_message"
git push