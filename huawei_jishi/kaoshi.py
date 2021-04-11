a = input()
a = a.split(',')
b = int(input())
c = []
d = []
e = []
f = []
for i in a:
    if '-' in i :
        i = i.split('-')
        for j in range(int(i[0]),int(i[-1])+1):
            c.append(j)
    else:
        c.append(int(i))
c.sort()
for v in c:
    if v == b :
        continue
    else:
        f.append(v)

for k in range(len(f)):
    if f[k] != b:
        if f[k] not in e:
                l = 0
                while (f[k+l+1] - f[k+l]) == 1 :
                    l = l + 1
                    e.append(f[k+l])
                    if (k+l+1) == len(f):
                        break
                if l == 0:
                    d.append(c[k])
                else:
                    m = '{}-{}'.format(f[k],f[k+l])
                    d.append(m)
for i in range(len(d)):
    if i == len(d)-1:
        print(d[i],end='')
    else:
        print("{},".format(d[i]),end = '')
