#!/bin/bash

CONFIG_PATH=~/.conky
MERGED_FILE="$CONFIG_PATH/conky.conf"

order=(
    "system"
    "cpu"
    "memory"
    "ram"
    "network"
)

# Start by writing the conky.config section (ensure a base config is used)
cat "$CONFIG_PATH/configs/header.conky" > "$MERGED_FILE"

# Begin the conky.text block
echo -e "\nconky.text = [[" >> "$MERGED_FILE"

for item in "${order[@]}"; do
    cat "$CONFIG_PATH/configs/$item.conky" >> "$MERGED_FILE"
    echo -e "" >> "$MERGED_FILE"
    #echo $item
done

# Close the conky.text block
echo -e "]]" >> "$MERGED_FILE"

# Start Conky with the merged config
#conky -c "$MERGED_FILE" &

# Append each section
#cat "$CONFIG_PATH/configs/system.conky" >> "$MERGED_FILE"
#echo -e "" >> "$MERGED_FILE"

#cat "$CONFIG_PATH/configs/cpu.conky" >> "$MERGED_FILE"
#echo -e "" >> "$MERGED_FILE"

#cat "$CONFIG_PATH/configs/memory.conky" >> "$MERGED_FILE"
#echo -e "" >> "$MERGED_FILE"

#cat "$CONFIG_PATH/configs/ram.conky" >> "$MERGED_FILE"
#echo -e "" >> "$MERGED_FILE"

#cat "$CONFIG_PATH/configs/network.conky" >> "$MERGED_FILE"
#No newline at the end
