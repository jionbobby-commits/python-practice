#第一题
def divide(a,b):
    if b == 0:
        raise Exception("不能除以0")
    else:
        print(a / b)
        return a / b

#第二题
def get_number():
    try:
     a = int(input())
    except ValueError:
        print("输入必须是整数")
    return a

#第三题
def score():
    try:
        li = []
        for i in range(0,5):
            li[i] = input("成绩：")

    except ValueError:
        print("输入错误，请重新输入")
    print(li,max(li),min(li),sum(li)/len(li))

#第四题
users = {"admin":"123456","zhangsan":"abc123","lisi":"666666"}



