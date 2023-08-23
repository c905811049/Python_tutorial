"""
输入一个日期 计算这个日期是当前年的第几天  2019-3-19   19  31+19+31 =81 
""" 

def CountDay(year,month,day):
    big_month = [1,3,5,7,8,10,12]
    small_month = [4,6,9,11]
    special_month = 2
    
    if month<=0 or month>12:
        print("输入错误数据!")
        return 0
    
    if day<=0 or day > 31:
        print("输入错误数据!")
        return 0
        
    if (year % 400 == 0) or (year % 100 !=0 and year % 4 ==0):
        leaf_year = True
        if month == 2 and day > 29:
            print("输入错误数据!")
            return 0
    else:
        leaf_year = False
        if month == 2 and day > 28:
            print("输入错误数据!")
            return 0
    
    monthDays = {}
    for i in range (1,month):
        if i in big_month:
           # print(i)
            monthDays[i] = 31
            # print(monthDays[i])
        elif i in small_month:
            monthDays[i] = 30
        else: 
            if leaf_year:
                monthDays[i] = 29
            else:
                monthDays[i] = 28
    sum = 0
    for i in monthDays:
        sum = sum + monthDays[i]
    
    sum = sum + day
    return sum

year = int(input("输入年份"))
month = int(input("输入月份"))
day = int(input("输入日"))

result = CountDay(year, month, day)
if result != 0:
    print(f"{year}年{month}月{day}日是该年的第{result}天")