#!/bin/sh
if pgrep -x "polybar" > /dev/null
then
    killall polybar
else
    polybar
fi
