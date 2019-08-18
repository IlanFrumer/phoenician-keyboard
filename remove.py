#!/usr/bin/env python

import xml.etree.ElementTree as ET 
EVDEV = '/usr/share/X11/xkb/rules/evdev.xml'

tree = ET.parse(EVDEV)
layoutList = tree.find('./layoutList') 
for layout in layoutList.findall('./layout'):
    for elem in layout.findall('./configItem/name'):
        if elem.text == 'px':
            layoutList.remove(layout)

tree.write(EVDEV)