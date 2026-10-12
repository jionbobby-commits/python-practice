#第一题

def square(num):
    return num*num
print(square(3))
print(square(4))

#第二题

def introduce(name,age,major):
    print(f"我叫{name},今年{age}岁,专业是{major}。")

#第三题

def login(username,password="123456"):
    return username,password

#第四题

def  sum_all(*nums):
    return sum(nums)

#第五题

def student_info(**info):
    for key,value in info.items():
        print(f"{key}: {value}")

student_info(姓名="张文博",年龄=21,专业="信管")

#第六题

def average(lst):
    return sum(lst)/len(lst)
def judge(lst):
    if average(lst) >= 60:
        return "及格"
    else:
        return "不及格"

scores = [78,66,90,55]
print(judge(scores))

#第七题

students = {"张三":88,"李四":95,"王五":76,"赵六":95}
def beststdent(dic):
    g = max(dic,key=dic.get)
    s = dic.get(g)
    a = sum(dic.values())/len(dic)
    return g,s,a

#第八题

def count_char(text):
    dic = {}
    for ch in text:
        if ch not in dic:
            dic[ch] = 1