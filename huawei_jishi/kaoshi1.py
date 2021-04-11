a = int(input())
b = input()
c = int(input())
d = []
b = b.split()
for i in range(a):
    if int(b[i]) not in d:
        d.append(int(b[i]))

d.sort()
print(d)
min = 0
max = 0
if c*2 > len(d):
    print(-1)
else:
    for i in range(c):
        min = min + d[i]
        max = max + d[-1-i]

    print(min+max)
#测试增加注释
