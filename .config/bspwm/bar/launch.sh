#!/usr/bin/env bash

DIR="$HOME/.config/bspwm/bar"

killall -q polybar
#while pgrep -u $UID -x polybar >/dev/null; do sleep 1; done

# launch the bars
# polybar -q border-menu -c "$DIR"/config.ini &
#polybar -q border-center -c "$DIR"/config.ini &
#polybar -q border-left -c "$DIR"/config.ini &
#polybar -q border-right -c "$DIR"/config.ini &
# polybar -q border-power -c "$DIR"/config.ini &
#sleep 3s
# polybar -q bar-menu -c "$DIR"/config.ini &
polybar -q bar-left -c "$DIR"/config.ini &
polybar -q bar-center -c "$DIR"/config.ini &
polybar -q bar-right -c "$DIR"/config.ini &
# polybar -q bar-power -c "$DIR"/config.ini &
