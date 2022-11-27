import xml.etree.ElementTree as ET
import pyflp
import gzip
flp = pyflp.parse("NewStuff.flp")
print(flp)
als_file = gzip.open("beat.als", 'r')
als = ET.fromstring(als_file.read())
print(als)