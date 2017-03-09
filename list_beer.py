# -*- coding: utf-8 -*
import io
from kitchen.text.converters import to_bytes, to_unicode

import xml.etree.ElementTree as ET 
#tree = ET.parse('Sortiment.xml')


with open('Sortiment.xml', 'r') as xml_file:
    tree = ET.parse(xml_file)
root = tree.getroot()

f = io.open("test", "w")


#Print child attributes of root
for article in root.iter('artikel'): 
	if article.find('Varugrupp').text == u'Öl':
		line = '%s\n' % to_unicode(article.find('Namn').text)
		f.write(line)
		

# Print all neighbors in the childs of the root
#for neighbor in root.iter('neighbor'):
#	print neighbor.attrib

