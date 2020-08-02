class Person:
    isAlive = False

    def __init__(self, name):
        self.name = name

    def run(self):
        print("run ")


person = Person("daus")
print(Person.isAlive)
