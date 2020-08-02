class Person:
    isAlive = False

    def __init__(self, name):
        self.name = name

    def run(self):
        print("run ")

    @classmethod
    def existential_crisis(cls, msg):
        return f"Why are we here, just to {msg}"


person = Person("daus")
print(Person.existential_crisis("suffer"))
