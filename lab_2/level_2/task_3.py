import xml.etree.cElementTree as ET
from collections import Counter
from lab_2.utils import readByPattern

path = '../a.txt'
pattern = '\w+\'\w+|\w+'

words = readByPattern(path, pattern)

print(words)

counter = Counter()
for word in words:
    counter[word] += 1

print(counter)

root = ET.Element("root")
for word in counter:
    ET.SubElement(root, "word", number=str(counter[word])).text = word
tree = ET.ElementTree(root)
tree.write("../c.xml", encoding='utf-8')
