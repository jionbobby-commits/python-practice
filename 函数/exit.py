"""
日期：2026-10-12

主题：Python 函数基础与进阶

学习内容：函数说明文档、嵌套调用、变量作用域、传参方式、

默认参数、不定长参数、参数类型

今日任务：

1. 编写 get_average(nums)，计算列表平均值，并添加函数说明文档。

2. 编写 square(n) 和 sum_square(a, b)，练习函数嵌套调用。

3. 验证局部变量与全局变量的区别，练习使用 global 修改全局变量。

4. 分析位置参数和关键字参数，解释函数调用的输出结果。

5. 编写 order_food(name, count=1)，练习默认参数。

6. 编写 calculate(*nums)，计算任意数量数字的总和与最大值。

7. 编写 show_info(name, *args, **kwargs)，理解不定长参数的接收方式。

8. 编写学生成绩统计程序，实现平均分、最高分和成绩报告功能。

9. 分析可变默认参数的问题，解释列表默认参数可能导致的结果。

完成要求：

1. 独立完成，尽量不查答案。

2. 每道题都进行测试，考虑边界情况。

3. 代码规范，函数职责清晰，适当添加文档说明。

4. 完成后上传 GitHub，作为每日 Python 学习记录。
"""

#任务1
def get_average(*args):
    """
   用于计算列表平均值
   :param args: 被计算列表
   :return: 平均值
    """
    a_vg = sum(args)/len(args)
    return a_vg

#任务2
def square(n):
    return n*n

def sum_square(a,b):
    sum_s = square(a)+square(b)
    return sum_s

#任务3
num = 1

def exi_t():
    num = 2
    print(num)      #局部变量

def exi_t1():
    global num      #声明全局变量
    num = 3
    print(num)

print(num)          #全局变量

#任务4
def introduce(name, age, city):
    print(name, age, city)

introduce("张三", 20, city="兰州") #位置参数为张三和20，关键字参数为city=兰州；输出应为：张三 20 兰州

#任务5
def order_food(name, count=1):
    print(f"{name}, {count}份")

order_food("惠林顿牛排")
order_food("酸辣土豆丝",4)

#任务6
def calculate(*nums):
    if nums == []:
        return 0
    else:
        sum_x = sum(nums)
        max_x = max(nums)
        return sum_x,max_x

print(calculate(3, 5, 8))
print(calculate(10, 20))

#任务7
def show_info(name, *args, **kwargs):
    print(name, args, kwargs)

show_info("张三", 18, "学生", city="兰州", major="信管")    #应返回：张三 [18,学生] {city:"兰州",major:"信管"}

#任务8(get_average()在任务1已经定义)
def get_max_score(*scores):
    """
    用于返回输入成绩的最高分(保留两位小数)
    :param scores:
    :return:
    """
    max_score = max(scores)
    return round(max_score,2)

def show_report(name, *scores, city="兰州"):
    avg_score = get_average(*scores)
    max_score = get_max_score(*scores)
    if scores == []:
        return "您未输入成绩。"
    else:
        print(f"学生：{name}\n, 城市：{city}\n成绩：{scores}\n平均分：{avg_score}\n最高分：{max_score}")
        return 1

#加分题
def add_item(item, items=[]):   #我认为第二个形参应该为*items,但实际应为items = None
    items.append(item)
    return items

print(add_item("Python"))
print(add_item("Linux"))