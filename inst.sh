#!/usr/bin/env bash

wget https://raw.githubusercontent.com/IlanFrumer/phoenician-keyboard/master/px -O /usr/share/X11/xkb/symbols/px
wget https://raw.githubusercontent.com/IlanFrumer/phoenician-keyboard/master/px.png -O /usr/share/iso-flag-png/px.png
python -c "$(wget -O- https://raw.githubusercontent.com/IlanFrumer/phoenician-keyboard/master/add.py)"
dpkg-reconfigure xkb-data
