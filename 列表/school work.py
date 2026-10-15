# 第四题：删除列表中的重复元素，保留第一次出现的顺序
import ast

s = ast.literal_eval(input("请输入一个列表（例如 [1, 2, 1, 3]）："))
unique_list = []
for x in s:
    if x not in unique_list:
        unique_list.append(x)
print(f"去除重复元素后：{unique_list}")


# 第五题：求列表的元素个数、最大值、最小值、元素之和和平均值
s = [9, 7, 8, 3, 2, 1, 55, 6]

# 用一次 for 循环计算个数、总和、最大值和最小值
count = 0
total = 0
max_value = s[0]
min_value = s[0]

for x in s:
    count += 1
    total += x
    if x > max_value:
        max_value = x
    if x < min_value:
        min_value = x

average = total / count
print(
    f"元素个数为{count}、最大值{max_value}、最小值{min_value}、"
    f"元素之和{total}、平均值{average}"
)

# 也可以使用内置函数：
# count = len(s)
# max_value = max(s)
# min_value = min(s)
# total = sum(s)
# average = total / count


# 第六题：偶数变成平方，奇数保持不变
s = [9, 7, 8, 3, 2, 1, 5, 6]
print(f"变换前，s={s}")
s = [x ** 2 if x % 2 == 0 else x for x in s]
print(f"变换后，s={s}")
