import re
import xml.etree.cElementTree as ET
from collections import Counter

words = []
pattern = re.compile('\w+\'\w+|\w+')
with open('../a.txt', mode='r', encoding='utf-8') as a:
    for line in a:
        for word in pattern.findall(line):
            words.append(word)

counter = Counter()
for word in words:
    counter[word] += 1

root = ET.Element("root")
for word in counter:
    ET.SubElement(root, "word", number=str(counter[word])).text = word
tree = ET.ElementTree(root)
tree.write("../c.xml", encoding='utf-8')
