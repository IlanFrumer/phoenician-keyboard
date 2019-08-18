#!/usr/bin/env python

import xml.etree.ElementTree as ET 
EVDEV = '/usr/share/X11/xkb/rules/evdev.xml'

tree = ET.parse(EVDEV)
layoutList = tree.find('./layoutList') 
for layout in layoutList.findall('./layout'):
    for elem in layout.findall('./configItem/name'):
        if elem.text == 'px':
            layoutList.remove(layout)

layout = ET.XML('''<layout>
    <configItem>
        <name>px</name>        
        <shortDescription>Phoenician</shortDescription>
        <description>Phoenician</description>
        <languageList>
          <iso639Id>phn</iso639Id>
        </languageList>
    </configItem>
</layout>''')

layoutList.append(layout)
tree.write(EVDEV)