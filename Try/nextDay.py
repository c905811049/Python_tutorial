def nextDay():
  flag = 1
  while flag == 1:
    year = int(input("请输入年份:"))
    month = int(input("请输入月份:"))
    day = int(input("请输入天:"))
    
    valid = 1
    
    if month > 12 or month <=0:
      print('输入错误月份！请重新输入')
      valid = 0
  
    if day > 31 or day <=0:
      print('输入错误天！请重新输入')
      valid = 0
    
    # 检查是否为闰年
    if (year % 4 == 0) or (year % 400 == 0 and year % 100 != 0):
      leap_year = True
    else:
      leap_year = False
      
    # 大月,包含31天的月份
    big_month = [1,3,5,7,8,10,12]
    # 小月,包含30天的月份
    small_month = [4,6,9,11]
    
    if month in big_month:
      if day < 31:
        day += 1
      else:
        day = 1
        if month == 12:
          year += 1
          month = 1
        else:
          month += 1
    elif month in small_month:
      if day < 30:
        day += 1
      elif day == 30:
        day = 1
        month += 1
      else:
        print('输入错误日期！')
        valid = 0
    else:
      if (leap_year and day< 29) or (not leap_year and day < 28):
        day +=1
      elif (leap_year and day== 29) or (not leap_year and day == 28):
        day = 1
        month += 1
      else:
        print('输入错误日期！')
        valid = 0
      
    if valid == 1:
      next_year, next_month, next_day = (year, month, day)
      print(next_year, next_month, next_day)
    
    #flag = int(input("你还要继续输入吗？1:继续,0:退出"))
  

nextDay()


