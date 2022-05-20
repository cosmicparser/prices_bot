# a = list(input())
# num = 0
# print(a.count("2"))
c = []
n = int(input("сколько чисел вы хотите ввести?:  "))

for i in range(0, n):
    ele = int(input())
    c.append(ele)

if c.index(20) != True:
    print(c)
else:
    pos = c.index(20)
    c.pop(pos)
    c.insert(pos, 200)
    print(c)

