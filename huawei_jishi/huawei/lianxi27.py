a = input()
s = a.split()
d = []
# print(s)
for i in s[1:int(s[0])+1]:
    #print(i)
    if len(i) == len(s[-2]) and i != s[-2]:
        c = 0
        for j in i:
            if i.count(j) == s[-2].count(j):
                c =  c + 1
                # print(c)
        if c == len(s[-2]):
            d.append(i)
print(len(d))
d.sort()
#print(d)
f = int(s[-1])-1
if f >= 0 and f < len(d):
    print(d[f])
