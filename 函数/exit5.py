#第一题
from 函数.exit3 import name


def add(a,b):
    return a+b
s = add(12,8)
print(s)
# 第二题
def check_num(n):
    if n%2==0:
        return "偶数"
    else:
        return "奇数"
print(check_num(7))
print(check_num(12))
#第三题
def get_max(nums):
    m_x =0
    for num in nums:
        if num>m_x:
            m_x = num
    return m_x
print(get_max([12,5,28,9,16]))
#第四题
scores = {
    "张三":85,
    "李四":92,
    "王五":78,
}
def get_score(name):
    if name in scores:
        return scores[name]
    else:
        return "查无此人"
#第五题
def greet(name,message="你好"):
    print(name,message)
greet("小明")
greet("小明","晚上好")
#第六题
class StuDent:
    StuDent.name = ""
    StuDent.score = ""
    def show(self):
        print(name,score)
zwb = StuDent()
print(zwb())
#第七题
def analyze(*args):
    print(max(args))
    print(min(args))
    print(sum(args))
nums = [10,20,5,35,15]
analyze(nums)
