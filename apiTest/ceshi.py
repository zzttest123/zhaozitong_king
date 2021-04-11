# 给定一个数组nums,编写一个函数将所有的0移动到数组的末尾，同时保持非零元素的相对顺序
# 输入：[0,1,3,0,3,2,88]
# 输出：[1,3,3,2,88,0,0]
# 必须在原数组上操作，不能额外定义新的数组
num = input()
i = 0
while i<len(nnum):
    for j in range(len(num)):
        if num[j] == 0:
            for k in range(j,len(num)):
                num[j] = num[j+1]
            num[-1] = 0
        continue
    i = i + 1
