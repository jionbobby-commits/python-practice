def decorator_function(original_function):
    def wrapper(*args, **kwargs):
        # 调用前
        print("执行前")

        result = original_function(*args, **kwargs)

        # 调用后
        print("执行后")

        return result
    return wrapper

@decorator_function
def target_function():
    print("原函数执行")

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # 输出：[2, 4, 6, 8]