class Person:

    def __init__(self, name="Ilya"):
        self.name = name

    def say_hi(self):
        print("Hi, " + self.name)


p = Person()
p.name = input('Print your name\n')
p.say_hi()
