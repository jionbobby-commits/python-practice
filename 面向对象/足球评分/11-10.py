def fib (n):
   try:
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
   except Exception:
       return 0
print(fib(1))

for i in range(1,10):
    for j in range(1,i+1):
        print(f"{i}*{j}={i*j}",end="\t")
    print()

total = 0
n = 1

for i in range(1,65):
    total += n
    n *= 2

print(total)
print(n//2)
