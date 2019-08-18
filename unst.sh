#!/usr/bin/env bash

rm /usr/share/X11/xkb/symbols/px
rm /usr/share/iso-flag-png/px.png
python -c "$(wget -O- https://raw.githubusercontent.com/IlanFrumer/phoenician-keyboard/master/remove.py)"
dpkg-reconfigure xkb-data
