#!/bin/bash

selected=$(echo "Lavender
Purple
Orange
Space
Blue
Red
Sky
Planetic
Leaves" | rofi -dmenu -theme ~/.config/bspwm/rofi/themes/launcher.rasi)

echo "$selected"

if [ "$selected" = "Lavender" ]
then
	cp ~/Pictures/Mono/lavender.png ~/.config/wallpapers/wall.jpg
	bspc wm -r
fi

if [ "$selected" = "Purple" ]
then
	cp ~/Pictures/Mono/Pink.png ~/.config/wallpapers/wall.jpg
	bspc wm -r
fi

if [ "$selected" = "Blue" ]
then
	cp ~/Pictures/Mono/Purple.png ~/.config/wallpapers/wall.jpg
	bspc wm -r
fi

if [ "$selected" = "Red" ]
then
	cp ~/Pictures/Mono/Red.png ~/.config/wallpapers/wall.jpg
	bspc wm -r
fi

if [ "$selected" = "Orange" ]
then
	cp ~/Pictures/Mono/Orange.png ~/.config/wallpapers/wall.jpg
	bspc wm -r
fi

if [ "$selected" = "Space" ]
then
	cp ~/Pictures/Mono/dark-blue.jpg ~/.config/wallpapers/wall.jpg
	bspc wm -r
fi

if [ "$selected" = "Sky" ]
then
	cp ~/Pictures/Mono/sky-blue.jpg ~/.config/wallpapers/wall.jpg
	bspc wm -r
fi
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

if [ "$selected" = "Planetic" ]
then
	cp ~/Pictures/wallpapers/wall.png ~/.config/wallpapers/wall.jpg
	bspc wm -r
fi

if [ "$selected" = "Leaves" ]
then
        cp ~/Pictures/wallpapers/cat_leaves.png ~/.config/wallpapers/wall.jpg
        bspc wm -r
fi
