#/bin/bash

SRC="/home/davidvalorwork/Videos/obs"
DEST="/home/davidvalorwork/Videos"
DEST_EXT=mp4
HANDBRAKE_CLI=HandBrakeCLI
PRESET=Discord Tiny 5 Minutes 240p30
FILE="$SRC"/"$1"

filename=$(basename "$FILE")
extension=${filename##*.}
filename=${filename%.*}
$HANDBRAKE_CLI -i "$FILE" -o "$DEST"/"$filename".$DEST_EXT "$PRESET"

#mkdir -p ~/trash
#mv $SRC/* ~/trash
