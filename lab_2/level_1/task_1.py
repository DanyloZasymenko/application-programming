f = open('../a.txt', mode='r', encoding='utf-8')
content = f.readlines()
content = [x.strip() for x in content]
print(content)
