#第一题

name ="张文博"
def show():
    name ="小明"
    print(name)
show()
#结果是小明，因为以“张文博”为值的变量name是全局变量，而调用函数时只牵扯函数show（）内的局部变量

#第二题

num= 10
def change():
    global num
    num=20
change()

#第三题

age = 20
def student(age):
    age =age + 1
    print(age)
student(age)
#21

#第四题

def outer(name):
    def inner():
        print(f"你好，{name}!")

    inner()

#第五题

city="兰州"

def test():
    school = "甘肃农业大学"
    print(city)
    print(school)
#city是全局变量，school是局部变量

#第六题

def report(name, score):
    print(f"{name}的成绩是{score}分。")
