from 函数.exit1 import introduce


class Student:
    def __init__(self, name,age):
        self.name = name
        self.age = age
    def introduce(self):
        print(f"我叫{self.name},今年{self.age}岁")
    def have_birthday(self):
        age_add1 = self.age + 1
        print(age_add1)

xiaoming = Student('xiaoming',18)
print(xiaoming.name)
xiaohong = Student('xiaohong',19)
print(xiaohong.name)

Bobbyzhang = Student('Bobbyzhang',20)
Bobbyzhang.introduce()
Bobbyzhang.have_birthday()
