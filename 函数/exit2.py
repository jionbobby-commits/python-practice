#第一题

def max_three(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    elif c>a and c>b:
        return c

print(max_three(2,3,4))

#第二题

def login(username,password="123456"):
    print(f"{username}您已登录")
    return username,password

#第三题

def  student(name,age,major,city="兰州"):
    return name,age,major,city
print(student("张文博","20","信管"))
print(student("张文博","20","信管","深圳"))

#第四题

def total_score(*scores):
    print(sum(scores))
    print(sum(scores)/len(scores))
    return

#第五题

def  show_info(**kwargs):
    for k,v in kwargs.items():
        print(f"{k}:{v}")

#第六题

def calculator(a,b):
    def add(a,b):
        return a+b
    def multiply(a,b):
        return a*b
    return add,multiply

#第七题

scores = {"语文":88,"数学":95,"英语":79,"Python":100}

def  best_subject(dic):
    return max(dic,key=dic.get),dic[max(dic,key=dic.get)]
print(best_subject(scores))

#第八题

def password_check(password):
    s = "abcdefghijklmnopqrstuvwxyz"
    c = s.upper()
    z = s + c
    if password < 8 or password not in range(10) or password not in z:
        return "密码不合格（必须包含数字和字母）"
    else:
        return "密码合格"
