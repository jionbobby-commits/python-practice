
class Goods:
    """商品类：负责保存和修改单个商品的信息"""

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def update(self, price=None, quantity=None):
        """修改商品价格和数量"""
        if price is not None:
            self.price = price
        if quantity is not None:
            self.quantity = quantity

    def __str__(self):
        return (
            f"商品名：{self.name} | "
            f"价格：{self.price:.2f} 元 | "
            f"数量：{self.quantity} | "
            f"小计：{self.price * self.quantity:.2f} 元"
        )


class ShoppingCart:
    """购物车类：负责管理多个商品"""

    system = "购物车管理系统"
    version = "1.0.0"

    def __init__(self, name):
        self.name = name
        self.goods_list = []

    def add_goods(self, goods):
        """添加商品，商品名称不能重复"""
        for item in self.goods_list:
            if item.name == goods.name:
                print("商品已经存在，不能重复添加！")
                return

        self.goods_list.append(goods)
        print("商品添加成功！")

    def update_goods(self, name, price=None, quantity=None):
        """根据商品名称修改信息"""
        for goods in self.goods_list:
            if goods.name == name:
                goods.update(price, quantity)
                print("商品信息修改成功！")
                return

        print("未找到该商品！")

    def remove_goods(self, name):
        """根据商品名称删除商品"""
        for goods in self.goods_list:
            if goods.name == name:
                self.goods_list.remove(goods)
                print("商品删除成功！")
                return

        print("未找到该商品！")

    def show_goods(self):
        """查询购物车中的全部商品"""
        if not self.goods_list:
            print("购物车为空！")
            return

        print(f"\n购物车名称：{self.name}")
        print("-" * 65)

        for index, goods in enumerate(self.goods_list, start=1):
            print(f"{index}. {goods}")

        total = sum(
            goods.price * goods.quantity
            for goods in self.goods_list
        )
        print("-" * 65)
        print(f"商品种类：{len(self.goods_list)}")
        print(f"商品总价：{total:.2f} 元")

    def run(self):
        """运行购物车菜单"""
        while True:
            print(f"\n===== {self.system} =====")
            print(f"当前购物车：{self.name}")
            print("1. 添加商品")
            print("2. 修改商品")
            print("3. 删除商品")
            print("4. 查询商品")
            print("0. 退出系统")

            choice = input("请选择操作：").strip()

            if choice == "1":
                name = input("请输入商品名称：").strip()
                if not name:
                    print("商品名称不能为空！")
                    continue

                price = self.input_price()
                if price is None:
                    continue

                quantity = self.input_quantity()
                if quantity is None:
                    continue

                goods = Goods(name, price, quantity)
                self.add_goods(goods)

            elif choice == "2":
                name = input("请输入要修改的商品名称：").strip()

                if not any(g.name == name for g in self.goods_list):
                    print("未找到该商品！")
                    continue

                price = self.input_price()
                if price is None:
                    continue

                quantity = self.input_quantity()
                if quantity is None:
                    continue

                self.update_goods(name, price, quantity)

            elif choice == "3":
                name = input("请输入要删除的商品名称：").strip()
                self.remove_goods(name)

            elif choice == "4":
                self.show_goods()

            elif choice == "0":
                print("已退出购物车管理系统。")
                break

            else:
                print("输入错误，请重新选择！")

    @staticmethod
    def input_price():
        """获取合法的商品价格"""
        try:
            price = float(input("请输入商品价格："))
            if price < 0:
                print("价格不能小于 0！")
                return None
            return price
        except ValueError:
            print("价格必须是数字！")
            return None

    @staticmethod
    def input_quantity():
        """获取合法的商品数量"""
        try:
            quantity = int(input("请输入商品数量："))
            if quantity <= 0:
                print("数量必须大于 0！")
                return None
            return quantity
        except ValueError:
            print("数量必须是整数！")
            return None


# 主程序：创建购物车对象并运行系统
if __name__ == "__main__":
    cart_name = input("请输入购物车名称：").strip()

    if not cart_name:
        cart_name = "默认购物车"

    cart = ShoppingCart(cart_name)
    cart.run()