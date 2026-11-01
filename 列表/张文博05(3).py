# -*- coding: utf-8 -*-
# 姓名：张文博
# 内容：教材第128页 第8、9题 + 第129页 第11题


# ---------------- 第8题：星期字典 ----------------
def question8():
    # 键是数字1~7，值是星期的缩写
    week = {1: 'Mon', 2: 'Tues', 3: 'Wed', 4: 'Thur', 5: 'Fri', 6: 'Sat', 7: 'Sun'}

    keys = list(week.keys())        # 键列表
    values = list(week.values())    # 值列表
    items = list(week.items())      # 键值列表（每项是 (键, 值)）

    print(*keys)      # * 的作用：把列表拆开，用空格隔开输出
    print(*values)
    print(items)


# ---------------- 第9题：按学号顺序输出成绩 ----------------
def question9():
    studs = [{'sid': '103', 'Chinese': 90, 'Math': 95, 'English': 92},
             {'sid': '101', 'Chinese': 80, 'Math': 85, 'English': 82},
             {'sid': '102', 'Chinese': 70, 'Math': 75, 'English': 72}]

    # 把列表里的数据提取出来，放到字典 scores：学号 -> [语文, 数学, 英语]
    scores = {}
    for stu in studs:
        scores[stu['sid']] = [stu['Chinese'], stu['Math'], stu['English']]

    # 按学号从小到大输出
    for sid in sorted(scores):
        print("%s:%s" % (sid, scores[sid]))


# ---------------- 第11题：回文字符串（5种方法） ----------------
def show(method, s, result):
    """统一输出判断结果"""
    if result:
        print("%s：%s是回文字符串" % (method, s))
    else:
        print("%s：%s不是回文字符串" % (method, s))


# 方法一：字符串逆序切片 [::-1]
def method1(s):
    return s == s[::-1]


# 方法二：for 循环遍历，逐字符比较（第i个和倒数第i个比）
def method2(s):
    n = len(s)
    for i in range(n // 2):
        if s[i] != s[n - 1 - i]:
            return False
    return True


# 方法三：转换为 list 后用 reverse() 反转
def method3(s):
    lst = list(s)
    lst.reverse()              # reverse() 直接改变列表本身，没有返回值
    return s == "".join(lst)


# 方法四：使用 reversed() 函数
def method4(s):
    return s == "".join(reversed(s))


# 方法五：递归（首尾相同，且去掉首尾后的中间部分也是回文）
def method5(s):
    if len(s) <= 1:            # 递归出口：0个或1个字符一定是回文
        return True
    if s[0] != s[-1]:
        return False
    return method5(s[1:-1])


def question11():
    s = input("输入字符串：")
    show("方法一", s, method1(s))
    show("方法二", s, method2(s))
    show("方法三", s, method3(s))
    show("方法四", s, method4(s))
    show("方法五", s, method5(s))


# ---------------- 主程序 ----------------
if __name__ == "__main__":
    print("=" * 10, "第8题", "=" * 10)
    question8()
    print("=" * 10, "第9题", "=" * 10)
    question9()
    print("=" * 10, "第11题", "=" * 10)
    question11()
