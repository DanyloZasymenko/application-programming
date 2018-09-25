from collections import Counter

import re
import xml.etree.cElementTree as ET

words = []
endings = []
pattern1 = re.compile(r'[А-Яа-яіїєІЇ\']+')
pattern2 = re.compile(r'([А-Яа-яіїєІЇ\`]{3})[ .,;\n\t]')
with open('../a.txt', mode='r', encoding='utf-8') as a:
    for i, line in enumerate(a):
        endings.extend(pattern2.findall(line))
        for j, word in enumerate(pattern1.findall(line)):
            words.append((word, i + 1, j + 1))

print(words)
print(endings)

counter = Counter()
for end in endings:
    counter[end] += 1

print(counter)

root = ET.Element("root")
for word in counter:
    string = ''
    for el in words:
        if el[0][len(el[0]) - 3:len(el[0])].find(word) != -1:
            string += ''.join(str(el))
    ET.SubElement(root, "word").text = word + '-' + str(counter[word]) + '-' + string
tree = ET.ElementTree(root)
tree.write("../c.xml", encoding='utf-8')
