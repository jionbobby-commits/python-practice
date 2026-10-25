class BankAccount:
    def __init__(self,name,__balance):
        self.name = name
        self.__balance = __balance

    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
            print(f"存款成功，当前余额为：{self.__balance}")
        else:
            print("存款金额必须大于0")

    def withdraw(self,amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"取款成功，当前余额为：{self.__balance}")
        else:
            print("取款金额无效或余额不足")

    def show_balance(self):
        print(f"{self.name}的当前余额为：{self.__balance}")


if __name__ == "__main__":
    account = BankAccount("张三", 1000)
    account.show_balance()
    account.deposit(500)
    account.withdraw(200)
    account.show_balance()