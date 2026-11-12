for i in range(9,0,-1):
    for j in range(i,0,-1):
        print(f"{i}*{j}={i*j}",end="\t")
    print()

#冒泡排序
def bubbleSort(arr):
    n = len(arr)

    # 遍历所有数组元素
    for i in range(n):

        # 最后 i 个元素已经处于正确的位置（无需再比较）
        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


arr = [64, 34, 25, 12, 22, 11, 90]

bubbleSort(arr)

print("排序后的数组:")
for i in range(len(arr)):
    print("%d" % arr[i]),