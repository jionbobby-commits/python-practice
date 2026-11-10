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
