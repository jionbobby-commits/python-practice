nums = list(map(int, input("输入六个整数：").split()))

# 升序
asc = nums.copy()
asc.sort()
print("升序：", asc)

# 降序
desc = nums.copy()
desc.sort(reverse=True)
print("降序：", desc)

# 原列表反转
rev = nums.copy()
rev.reverse()
print("原反：", rev)