a = open('../a.txt', mode='r', encoding='utf-8')
content = a.readlines()
a.close()

content = [x.strip() for x in content]

print('All lines: ', content)

b1 = open('../b1.txt', mode='w', encoding='utf-8')
b2 = open('../b2.txt', mode='w', encoding='utf-8')
evenLines = []
oddLines = []
for i, line in enumerate(content):
    if (i % 2 == 0):
        evenLines.append(line.upper())
        b1.writelines('%s\n' % line.upper())
    else:
        oddLines.append(line.lower())
        b2.writelines('%s\n' % line.lower())
b1.close()
b2.close()
print('Even lines: ', evenLines)
print('Odd lines: ', oddLines)
