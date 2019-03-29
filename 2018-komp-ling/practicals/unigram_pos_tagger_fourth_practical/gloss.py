import xml.etree.ElementTree as ET

tree = ET.parse('isl-ex.xml')
root = tree.getroot()

for tier in root.findall('.//tier'):
        if tier.attrib['id'] == 'n':
                for item in tier.findall('.//item'):
                        print(item.text)