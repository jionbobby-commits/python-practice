class Student:
    def __init__(self,__name,__age):
        self.__name = __name
        self.__age = __age

    def show_info(self):
        print(f"姓名：{self.__name}, 年龄：{self.__age}")

z3 = Student("张三", 20)
l4 = Student("李四", 21)
z3.show_info()
l4.show_info()
