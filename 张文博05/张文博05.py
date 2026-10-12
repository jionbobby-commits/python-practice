"""第三题"""
principal = float(input("请输入本金："))
r = float(input("请输入年利率"))
r = r * 0.01
n = int(input("请输入年份："))
amount =  principal * (1+r) ** n
print("本金利率和为：{0:2.2f}".format(amount))
"""第四题"""
from math import pi
r = float(input("请输入球的半径："))
area = 4*pi*r**2
volume = 4/3*pi*r**3
print("球的表面积为：{0:2.2f},体积为：{1:2.2f}".format(area,volume))
"""第五题"""
def getvalue(b,r,n):
    return b * (1 + r) ** n

b = float(input("请输入本金："))
r = float(input("请输入年利率"))
r = r * 0.01
n = int(input("请输入年份："))
v=getvalue(b,r,n)
print("复利为：{:.2f}".format(v))
"""第六题"""
from math import sqrt
a = 1
b = -10
c = 16
beta = b**2-4*a*c
x1 = (-b+sqrt(beta))/(2*a)
x2 = (-b-sqrt(beta))/(2*a)
print("方程x*x -10*x + 16 = 0 的解为{} {}".format(x1,x2))
"""第七题"""
import datetime
sName = input("请输入您的姓名：")
year = input("请输入您的出生年份：")
age = datetime.date.today().year - int(year)
print("您好！{0}。您{1}岁".format(sName,age))
