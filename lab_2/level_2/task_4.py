from collections import Counter
import xml.etree.cElementTree as ET
import re

words = []
pattern = re.compile(r'\w{3}\b')
with open('../a.txt', mode='r', encoding='utf-8') as a:
    for line in a:
        for word in pattern.findall(line):
            words.append(word)

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

