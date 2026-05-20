#!/bin/bash

name="$*"

clean_name=$(echo "$name" | sed 's/[ .]/_/g')
file_name="${clean_name}.py"

if [ -f "$file_name" ]; then
    echo "File $file_name already exists."
else
    echo "# Write your code here" > "$file_name"
    echo "File $file_name created."
fi