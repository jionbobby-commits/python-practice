class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says woof!"


li = [90,85,75,95,80]

def main(*args):
    avg = sum(li) / len(li)

    print(f"Average score: {avg}")

dic = {"小明": 90, "小红": 85, "小刚": 75, "小李": 95, "小王": 80}

for name, score in dic.items():
    print(f"{name}: {score}")