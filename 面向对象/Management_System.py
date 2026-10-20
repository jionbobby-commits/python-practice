class Student:
    def __init__(self,name,chinese,math,english):
        self.name = name
        self.chinese = chinese
        self.math = math
        self.english = english

    def __str__(self):
        return f"姓名：{self.name}|语文：{self.chinese}分|数学：{self.math}分|英语：{self.english}分|"

    def __eq__(self,other):
        return True if self.name == other.name and self.chinese == other.chinese and self.math == other.math and self.english == other.english else False

    def update_score(self,chinese=None,math=None,english=None):
        if chinese is not None:
            self.chinese = chinese
        if math is not None:
            self.math = math
        if english is not None:
            self.english = english


class Management_System:

    version = "1.0.0"
    system = "教务管理系统"

    def __init__(self):
        self.students = []

    def add_score(self):

        name = input("输入学生姓名：")

        for s in self.students:
            if s.name == name:
                print("该学生已添加！")
                return
        chinese = int(input("输入语文成绩："))
        math = int(input("输入数学成绩："))
        english = int(input("输入英语成绩："))

        if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
            stu = Student(name,chinese,math,english)
            self.students.append(stu)
            print(f"学生信息添加成功OwO\n{self.students}")
        else:
            print("成绩应在0~100以内！(V^V)")

    def modify_score(self):

        name = input("输入学生姓名：")

        for s in self.students:
            if s.name == name:
                print(s)

                chinese = int(input("输入要修改的语文成绩："))
                math = int(input("输入要修改的数学成绩："))
                english = int(input("输入要修改的英语成绩："))

                if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:

                    s.update_score(chinese,math,english)
                    print(f"已修改{s}")
                    return
                else:

                    print("成绩应在0~100以内！(V^V)")
                    return
        print("未找到学生，请先添加")


    def dle_student(self):
        name = input("请输入要删除的学生的姓名")
        for s in self.students:
            if s.name == name:
                self.students.remove(s)
                return
        print("未找到学生，请先添加")

    def show_students(self):
        name = input("请输入要查找的学生的姓名")
        for s in self.students:
            if s.name == name:
                print(f"学生信息为：{s}")
                return
        print("未找到学生，请先添加")


    def list_students(self):
        for s in self.students:
            print(f"学生信息为：{s}")

    def run(self):
        print(f"欢迎使用学生管理系统V{self.version}")

        while True:
            print()
            print("####################################################################")
            print("#1.添加学生2.修改学生信息3.删除学生信息4.查找指定学生5.查找所有学生6.退出系统#")
            print("####################################################################")

            choice = input("输入您要进行的服务（仅输入数字）")
            match choice:
                case "1":
                    self.add_score()
                case "2":
                    self.modify_score()
                case "3":
                    self.dle_student()
                case "4":
                    self.show_students()
                case "5":
                    self.list_students()
                case "6":
                    print("Bye~")
                    break
                case _:
                    print("输入错误请选择1~6")

if __name__ == "__main__":
    stu = Management_System()
    stu.run()