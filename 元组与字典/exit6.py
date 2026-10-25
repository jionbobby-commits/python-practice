totle = {}
totle[input("输入您的姓名：")] = input("输入您的电话：")
p = input("输入您想查询电话拥有者的姓名：")
print(totle.get(p,"联系人不存在"))