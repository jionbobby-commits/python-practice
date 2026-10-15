#第四题
li = input("输入一个列表：")
x = []
for i in li:
    if i in x:
        x.remove(i)
    else:
        x.append(i)
print(f"去除重复元素后：{x}")

#第五题
s=[9,7,8,3,2,1,55,6]
gs_list = 0
for i in s:
    gs_list += 1
max_list = max(s)
min_list = min(s)
sum_list = sum(s)
av_list = sum_list/len(s)
print(f"元素个数为{gs_list}、最大值{max_list}、最小值{min_list}、元素之和{sum_list}、平均值{av_list}")

#第六题
s1=[9,7,8,3,2,1,5,6]
s2 = [i^2 for i in s1 if i%2==0]
print(f"变换前，s={s1}")
print(f"变换后，s={s1}")