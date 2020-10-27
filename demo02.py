# 输入年份转为整数
year = int(input("请输入年份："))
# 输入月份转为整数
month = int(input("请输入月份："))
# 定义一个天数
days = 0
# 判断
if month in [1, 3, 5, 7, 8, 10, 12]:
    days = 31
elif month in [4, 6, 9, 11]:
    days = 30
else:
    # 处理2月份
    if year % 400 == 0 or (year % 4 == 0 and year % 400 != 0):
        days = 29
    else:
        days = 28
# 输入
print("%d年%d月:%d天" % (year, month, days))
