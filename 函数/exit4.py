#第一题

comp = lambda x,y: x if x > y else y

#第二题

num = input("输入一数")

pd = lambda num :True if num%2==0 else False

#第三题

zn = lambda num :"正数" if num >0 else "负数或0"

#第四题

nums = [3, 8, 1, 6, 9]

mi = lambda x : x*x
vul = map(mi,nums)
print(vul)

#第五题

scores = [78, 92, 65, 100, 88]

print(max(scores))
print(min(scores))
print(sum(scores))
print(float(sum(scores)/len(scores)),2)

#第六题

sorted(scores,reverse=True)

#第七题

fruits = ["苹果", "香蕉", "橘子"]
enumerate(fruits)
print(enumerate(fruits))

#第八题

names = ["张三", "李四", "王五"]
scores1 = [90, 85, 98]

print(zip(names,scores1))

#第九题

student = ("张文博", 20, "信管241")

a, b, c = student
print(a, b, c)

#第十题

numsS = [10, 20, 30, 40, 50]

first, last, *middle = numsS
print(first, last, middle)

#第十一题

students = [("张三", 80), ("李四", 95), ("王五", 70)]
sorted(student,reverse = True,key=lambda *x: x)
