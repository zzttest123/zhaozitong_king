#coding=utf-8
#输入一个int型整数，按照从右向左的阅读顺序，返回一个不含重复数字的新的整数。
#保证输入的整数最后一位不是0。
a = input()
a = a[::-1]
b = []
for i  in a:
    if  i not in b:
        b.append(i)
#print(c)
d = 0
for i in range(len(b)):
    d = d + int(b[i])*(10**(len(b)-i-1))
    #print(c[i])
print(d)
