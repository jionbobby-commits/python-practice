#第一题
from 字符串 import count

student = {"姓名":None,"年级":None,"专业":None}
print(student["专业"])

#第二题

student["年龄"] = 21
student["城市"] = "平凉"

#第三题

vul = input("输入您想查询的建：")
print(student.get(vul,"没有该信息"))

#第四题

se = {1,2,3,3,4,5}
print(se)      #因为集合的唯一性所以消除重复项

#第五题

nums = input("输入八个整数（可重复但要用空格隔开）".split( ))
nums1 = set(nums)
nums1.remove(" ")
print(nums1)

#第六题

st = "information management"
dc1 = {}

for i in st:
    if i not in dc1:
        dc1[i] = 1
    else:
        dc1[i] += 1

print(dc1)

#第七题

st1 = input("输入一些英文单词：".split( ))
se1 = set(st1)
li = len(list(se1))
print(f"不重复单词的集合为{se1},单词的总种类数为{li}")

#第八题

li1 = [3,5,3,8,5,1,9,1]
se2 = set(li1)
li2 = list(se2)
print(li2.sort())

#第九题

dic1 = {"语文":88,"数学":99,"英语":100}
avg = (dic1["语文"]+dic1["数学"]+dic1["英语"])/3
if dic1["语文"]>dic1["数学"]:
    if dic1["语文"]>dic1["英语"]:
        print("语文分数最高")
    elif dic1["语文"]<dic1["英语"]:
        print("英语分数最高")
    else:
        print("语文和英语的分数都最高")
elif dic1["语文"]<dic1["数学"]:
    if dic1["数学"] > dic1["英语"]:
        print("数学分数最高")
    elif dic1["语文"] < dic1["英语"]:
        print("英语分数最高")
    else:
        print("数学和英语的分数都最高")
else:
    print("语文和数学的分数都最高")

#第十题

st5 = input("输入一句话".split())
dc4 = {}

for i in st5:
    if i not in dc4:
        dc4[i] = 1
    else:
        dc4[i] += 1

print(dc4)

#挑战

tz = [2,4,5,6,7,8,9,10]
lb = [i*2 for i in tz if i%2==0]
print(lb)