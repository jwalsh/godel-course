#!/bin/bash

# Loop through directories that match the pattern "week-*"
for old_directory in week-*; do
    # Extract the week number from the directory name
    week_number="${old_directory#week-}"
    week_number="${week_number%%-*}"

    # Pad the week number with leading zeros
    padded_week_number=$(printf "%02d" "${week_number}")

    # Construct the new directory name
    new_directory="${old_directory/week-${week_number}/week-${padded_week_number}}"

    # Rename the directory if the new directory name is different
    if [ "${old_directory}" != "${new_directory}" ]; then
        mv "${old_directory}" "${new_directory}"
        echo "Renamed '${old_directory}' to '${new_directory}'"
    fi
done
