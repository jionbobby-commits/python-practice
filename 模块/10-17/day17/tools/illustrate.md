第4题:理解类与对象
class Dog
    pass
dog1= Dog()
dog2 = Dog()
print(type(dog1))
print(dog1 == dog2)

答：1，dog是类
    2，因为他们是两个对象，存放的内存地址不一样

第6题:分析self
class Phone:
    def show_info(self)：
        print("这是一部手机")

phone = Phone()
phone.show_info()

答：1，好问题，我只知道他是实例对象的，可能指向对象吧.
    2，应为self只是实例化对象的，且函数并无其他形参
    3，肯定是phane2的内存地址
