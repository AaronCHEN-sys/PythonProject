"""
具体需求：输入圆的半径，计算圆的周长和面积，结果要保留两位小数，对圆的半径的输入进行有效性校验
"""
# 全局的变量
PI = 3.1415926


def input_num():
    """
    输入一个有效的数字
    :return: 返回输入的有效数字
    """
    # 使用循环来实现，如果输入无效，则提示重新输入
    while True:
        # 提醒输入
        radii_str = input("请输入圆的半径：")
        # 使用异常处理
        try:
            radii = float(radii_str)
            # 返回
            return radii

        except:
            print("输入的半径无效")


def get_area(radii: float):
    """
    根据半径计算圆的面积
    :param radii: 半径
    :return: 返回计算好的圆的面积
    """
    # 返回圆的面积
    return PI * radii * radii


def get_length(radii: float):
    """
    根据半径计算圆的周长
    :param radii: 半径
    :return: 返回计算好的圆的周长
    """
    # 返回圆的周长
    return 2 * PI * radii


# main函数：程序的入口
if __name__ == '__main__':
    # 调用函数，提醒输入半径，返回一个符合要求的值
    radii = input_num()
    # 计算圆的周长
    print("圆的周长为：%.2f" % get_length(radii))
    print("圆的面积为：%.2f" % get_area(radii))
