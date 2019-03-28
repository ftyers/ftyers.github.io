
import xml.etree.ElementTree as ET

parser = ET.XMLParser(encoding='utf-8')
tree = ET.parse('isl-ex.xml', parser=parser)
root = tree.getroot()

for tier in root.findall('.//tier'):
    if tier.attrib['id'] == 'n':
        for item in tier.findall('.//item'):
            if item.attrib['tag'] == 'T':
                print(item.text)

