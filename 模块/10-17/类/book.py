class Book:
    def __init__(self,title,author,is_borrowed = "未借出"):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed

    def show_info(self):
        print(self.title,self.author,self.is_borrowed)

    def borrow(self):
        if self.is_borrowed == "未借出":
            self.is_borrowed = "已借出"
        else:
            print("该书已被借出")

    def return_book(self):
        self.is_borrowed = "未借出"
        print(f"{self.title}未借出")

print("_________________________________________________")

book001 = Book("《Python入门》","张三") #1
book001.show_info() #2
book001.borrow()
book001.borrow() #3
book001.return_book() #4
book001.show_info() #5

