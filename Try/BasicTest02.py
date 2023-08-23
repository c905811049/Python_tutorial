"""
求 1 2 3 4 能够组成多少个三位互不重复的三数位？打印出来三位数，打印多少个？
123 
"""

count = 0
list = []
for i in range(1,5):
    one = i
    for j in range(1,5):
        two = j
        if one == two:
            continue
        for k in range(1,5):
            three = k
            if one == three or two == three:
                continue
            sum = int(str(one)+str(two)+str(three))
            count += 1
            list.append(sum)

for i in range(len(list)):
    print(list[i])
    
print(f'总个数{count}')