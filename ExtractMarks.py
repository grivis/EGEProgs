def isbad(marklist):
    before = len(marklist)
    marklist = list(filter(lambda x: x != '2', marklist))
    #print('isbad',marklist)
    after = len(marklist)
    return before > after


def numbads(marklist):
    marklist = list(filter(lambda x: x == '2', marklist))
    #print('numbads', marklist)
    return len(marklist)


def isbad1(marklist):
    return numbads(marklist) > 0

f = open('StudentMarks.txt', 'r', encoding='utf8')

studlines = []
for line in f:
    studlines.append(line[:-1])

students = list(map(lambda x: x.split(), studlines))

f.close()

badstudents = list(filter(isbad, students))
s_badstudents = sorted(badstudents, reverse=True,  key=numbads)

for stud in s_badstudents:
    list(map(lambda x: print(x, end=' '), stud))
    print()

