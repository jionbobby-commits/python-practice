
def add(a,b):
    return a+b

def is_even(n):
    if n % 2 == 0:
        return "是偶数"
    else:
        return "是奇数"

def get_max(numbers):
    return max(numbers)

if __name__ == "__main__":
    print(add(3,5))