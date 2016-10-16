import re

read = 'А я сижу на берегу. Сидя у окна, считаю ворон. Сидит девица в терему. Сидючи дома, мир не увидишь.'
result = re.findall('[Сс]и[дж][а-я]*', read)
for word in result:
    print(word)


print()

read1 = 'Я пришел, а ты ушел. Петя зашел в подъезд. Сначала вошел, потом вышел. Его нет, он отошел.'
result1 = re.findall('[при|во|за|ото]+шел', read1)
for word in result1:
    print(word)

print()

read2 = ' a.xls b.xls abc.xls def f.xlsx london.xls hello.xml'
result2 = re.findall('\S*\.xls[\S]*', read2)
for word in result2:
    print(word)

