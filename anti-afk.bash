#!/bin/bash

stop_macro() {
    running=false
}


eval $(xdotool getmouselocation --shell)
Start_x=$X
Start_y=$Y

( while $running; do
    read -rsn1 key
    if [[ $key == "v" ]]; then
        stop_macro
    fi
done ) &



while true; do

# Move the cursor back by 1 pixel (left)
xdotool mousemove $((X-1)) $Y

# Sleep for a short time
sleep 1.0

# Start Pos.
xdotool mousemove $X $Y

done

xdotool mousemove $Start_x $Start_y


kill $!