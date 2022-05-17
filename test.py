#
# print("Hello python")
# price = float(input("请输入苹果单价:"))
# print("苹果的单价 %.2f" % price)
#
import random
import numpy

# zwy_weight = int(input("请输入张维宇的体重kg: "))
# if zwy_weight >= 65 :
#     print ("你还是别吃饭了")
# elif zwy_weight < 65 and zwy_weight >=50:
#         print("继续加油减肥 ")
# elif zwy_weight < 50 and zwy_weight >47:
#         print("就快成功了 ")
# elif zwy_weight <= 47 and zwy_weight >43:
#     print("恭喜你获得5000元")
# elif zwy_weight <= 43 :
#     print("太瘦了! 记得多吃点饭")

def print_result(numinput, name):
    if numinput == 1:
        print(name + "出的是石头")
    elif numinput == 2:
        print(name + "出的是剪刀")
    elif numinput == 3:
        print(name + "电脑出的是布")


hum_output = int(input("选择你要出的是 石头（1） 剪刀（2） 布（3）:"))
com_output = random.randint(1, 3)

print_result(hum_output, "玩家")
print_result(com_output, "电脑")

if ((hum_output == 1 and com_output == 2)
        or (hum_output == 2 and com_output == 3)
        or (hum_output == 3 and com_output == 1)):
    print("你赢了")
elif hum_output == com_output:
    print("平局")
else:
    print("你输了")
