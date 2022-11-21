#/bin/bash

SRC="../obs"
DEST="../"
DEST_EXT=mp4
# HANDBRAKE_CLI=HandBrakeCLI

HANDBRAKE_CLI='./HandBrakeCLI.exe'
PRESET='Discord Tiny 5 Minutes 240p30'
cd ~/Videos/obs

for FILE in $(ls)
do
	cd ~/Videos/HandBrakeCLI
	echo FILE: $FILE
	filename=$(basename "$FILE")
	extension=${filename##*.}
	filename=${filename%.*}
	$HANDBRAKE_CLI -i "$SRC/$FILE" -o "$DEST"/"$filename".$DEST_EXT "$PRESET"
done

mkdir -p ~/trash
mv $SRC ~/trash
mkdir -p $SRC
