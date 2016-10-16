import re
f = open('wordread.txt')
read = f.read()
result = re.findall(r'[Сс]и[дж][а-я]*', read)
resset = set(result)
for word in resset:
    print(word)
