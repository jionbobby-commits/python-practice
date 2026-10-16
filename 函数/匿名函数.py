
"""
#### 任务 1：匿名函数

1. 使用 `lambda` 实现两个数相加。
2. 使用 `sorted()` 和 `lambda`，按照学生成绩从高到低排序。
3. 使用 `map()` 和 `lambda`，将列表 `[1, 2, 3, 4, 5]` 中的每个数平方。

#### 任务 2：递归

1. 编写 `factorial(n)`，递归计算 `n!`；例如 `factorial(5)` 返回 `120`。
2. 编写 `sum_numbers(n)`，递归计算 `1` 到 `n` 的整数之和。
3. 思考：递归的终止条件是什么？没有终止条件会怎样？

#### 任务 3：综合案例——学生成绩统计

编写学生成绩统计程序，要求：

- 使用字典保存至少 4 名学生的成绩。
- 使用函数计算平均分。
- 使用 `max()` 找出最高分学生。
- 使用 `sorted()` 和 `lambda` 排序。
- 输出平均分、最高分学生及完整排名。

**完成标准：**独立完成匿名函数和递归练习；尽量完成综合案例。
"""



#任务1
add = lambda a,b: a+b   #1

order_s = lambda *args: sorted(args,reverse=True)   #2

li = [1,2,3,4,5]
power = lambda a,b: a**b
square = lambda *args: map(*args,power)

#任务 2：递归
def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

def sum_numbers(n):
    if n == 0:
        return 0
    else:
        return n+sum_numbers(n-1)

#任务 3：综合案例——学生成绩统计

def score(**kwargs):
    avg_score = sum(kwargs.values())/len(kwargs.values())
    max_score = max(kwargs.values())
    sort_function = lambda **kwargs: sorted(kwargs.values(),reverse=True)
    sort_score = sort_function(**kwargs)
    print(avg_score,max_score,sort_score)