class Note:
    def __init__(self, *title,**content):
        self.title = title
        self.content = content

    def __str__(self):
        return f'{self.title} {self.content}'

    def shoe(self):
        print(f'{self.title} {self.content}')

n1 = Note(["1","2","3","4","5","6","7","8","9"],{"a":"A","b":"B","c":"C","d":"D"})
n1.shoe()

n2 = Note(["a","b","c"],{"a":"A","b":"B","c":"C"})
n2.shoe()

for n in [n1,n2]:
    print(n)