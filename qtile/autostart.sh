#!/bin/zsh

xrandr --output eDP-1 --mode 1366x768 --pos 1920x0 --rotate normal --output DP-1 --off --output HDMI-1 --primary --mode 1920x1080 --pos 0x0 --rotate normal --output DP-2 --off --output HDMI-2 --off &
feh --bg-fill --no-fehbg ~/Pictures/wallpapers/wallpaper.jpg &
picom &
dunst &
pa-applet &
