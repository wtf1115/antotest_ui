"""
1、现在有字符串：str1 = 'python cainiao 666'
    1、请找出第 5 个字符。 
"""
str1 = 'python cainiao 666'
print(str1[4])

for i in range(len(str1)):
    if i == 4:
        print(str1[i])

"""
1、现在有字符串：str1 = 'python cainiao 666'
    2、请复制一份字符串，保存为 str_two
"""

#  方法一
import copy


str_two = copy.copy(str1)
print(str_two)

#  方法二
str_two = str1
print(str_two)

#  方法三
str_two = str1[:]
print(str_two)

#  方法四
str_two = "".join(str1)
print(str_two)


"""
1、现在有字符串：str1 = 'python cainiao 666'
    请找出字符串最中间的字符。（字符串长度是偶数。）
"""

#  方法一
print(str1[int(len(str1)/2)],str1[int(len(str1)/2+1)])

"""
卖橘子的计算器：写一段代码，提示用户输入橘子的价格，和重量，最后计算出应该支付的金额
"""

price = input("输入橘子的单价(数字格式)：")
weight = input("输入橘子的重量(数字格式)：")

while True:
    if weight.isnumeric() & price.isnumeric():
        price_yes = int(price)
        weight_yes = int(weight)
        print("橘子价格{}元,请支付".format(price_yes*weight_yes))
        break
    else:
        price = input("输入橘子的单价(数字格式)：")
        weight = input("输入橘子的重量(数字格式)：")


"""
my_hobby = "Never stop learning!"

截取从 位置2 ~ 位置6 的字符串

截取从 位置2 ~ 末尾 的字符串

截取从 开始位置~ 位置6 的字符串

截取完整的字符串

从 索引3 开始，每2个字符中取一个字符

截取字符串末尾两个字符

字符串的倒序

"""
my_hobby = "Never stop learning!"
print(my_hobby[1:7])
print(my_hobby[1:])
print(my_hobby[:7])
print(my_hobby[:])
print(my_hobby[3::2])
print(my_hobby[-2:])
print(my_hobby[::-1])