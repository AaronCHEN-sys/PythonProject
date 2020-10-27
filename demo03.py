str = "fdsafdsaYYYYdsafdRRR43243243!@^%$#复读机啊发动机范德萨就开了发fdafdsa的撒娇"
# 定义变量
# dict ---key_value
num = {'upper': 0, 'lower': 0, 'number': 0, 'chinese': 0, 'other': 0}
# 遍历每一个字符
for char in str:
    # 判断大写字母
    if char.isupper():
        num['upper'] += 1

    # 判断小写字母
    elif char.islower():
        num['lower'] += 1

    # 判断数字
    elif char.isdigit():
        num['number'] += 1

    # 判断汉字
    elif char >= '\u4E00' and char <= '\u9FA5':
        num['chinese'] += 1
        # 其他
    else:
        num['other'] += 1

print("大写字母：%d\n小写字母：%d\n数字：%d\n汉字：%d\n其他字符:%d" % (
    num['upper'], num['lower'], num['number'], num['chinese'], num['other']))
