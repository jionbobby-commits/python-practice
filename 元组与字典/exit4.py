score = {"语文":95,"数学":88,"英语":76}
a = input("输出您想查询的课程：")
print(score.get(a,"没有该课程"))

#第六题
for i in score:
    print(f"{i}:{score[i]}")