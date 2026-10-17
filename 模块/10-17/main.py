import calculator
print(calculator.add(15, 8))
print(calculator.subtract(15, 8))
"""
模块和包有什么区别?
_ini二.py在这里起什么作用?
答：我认为模块和包的区别是：包是对相同类型模块的整理，而模块是对相同类型函数的整理，
    包中含有__inti__文件；__inti__.py的作用有：说明包的版本，作者和*通配的功能
"""

#第七题

from 类.book import Book

book001 = Book("《Python入门》","张三") #1
book001.show_info() #2
book001.borrow()
book001.borrow() #3
book001.return_book() #4
book001.show_info() #5

