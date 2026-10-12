# 第一题
st = int(input("输入一个整数"))
print(st + 10)

# 第二题
hight = float(input("输入你的身高（公斤）"))
print(hight)

# 第三题
name = input("输入您的姓名：")
age = str(input("输入您的年龄："))
print("我叫"+name+","+"今年"+age+"岁。")

# 第四题

pi = 3.14
print(type(pi))
print(int(pi))

# 第五题

li = "[1,2,3,4]"
print(len(eval(li)))

# 第六题

li1 = [10,20,30,40]
tuple(li1)
print(li1[1])

# 第七题
st1 = "Python"
list(st1)
print(st1[0:2])

# 第八题
U = int(input("输入一个数字"))
chr(U)
print(f"它对应的字符为：{U}")

# 第九题
a = input("输入第一个数字：")
b = input("输入第二个数字：")
print(f"他们的和为：{eval(a+"+"+b)}")
print(f"他们的积为：{eval(a+"*"+b)}")
print(f"他们的平均值为：{eval("("+a+"+"+b+")"+"/2")}")

# 第十题
st2 ="13245"
li2 = [int(i) for i in st2]
print(type(li2),li2)
tuple(li2)
print(type(li2),li2)

# 加分
nums = 48
print(chr(nums))
ord(nums) #语法错误我做不到
