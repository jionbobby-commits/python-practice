# 第一题
student = {"name":"张文博","age":20,"专业":"信息管理与信息系统"}
print(student["专业"])

# 第二题
student["年龄"] = 21
student["city"] = "平凉"
del(student["age"])
print(student)

# 第三题
score = {"Python":95,"Java":80,"Linux":88}
for name in score:
    print(f"{name}:{score[name]}")

# 第四题
A = {1,2,3,4,5}
B = {4,5,6,7}
print(A & B)
print(A | B)
print(A - B)

# 第五题
x = (input("输入一串数字(用空格隔开)"))
y = set()
y.update(x)
z = []
for i in y:
    z.append(i)
z.remove(" ")
print(z)

#第六题
st = input("输入一句英文")
se = set()
li = []
s = 0
for i in st:
    se.add(i)
for i in se:
    li.append(i)
li.remove(" ")
for i in li:
    s += 1
print(s)

#第七题
goods = {"苹果":5,"牛奶":8,"面包":6}
name = input("输入商品名：")
if name in goods:
    print(goods[name])
else:
    print("没有该商品")

#第八题
cal1 =input("请输入一班学生的姓名：")
cal2 =input("请输入二班学生的姓名：")
se1 = set()
se2 = set()
for i in cal1:
    se1.add(i)
for i in cal2:
    se2.add(i)
print(se1|se2)
print(se1&se2)
print(se1-se2)