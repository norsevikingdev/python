# class Person:
#     isAlive = False

#     def __init__(self, name, age):
#         self._name = name
#         self._age = age

#     def run(self):
#         print("run ")

#     @classmethod
#     def existential_crisis(cls, msg):
#         return f"Why are we here, just to {msg}"

#     # static methods doesn't have access to cls
#     @staticmethod
#     def add(num1, num2):
#         return num1 + num2


class Player:
    def __init__(self, name="player", hp=100, mana=20, attack=5, defence=2):
        self._name = name.capitalize()  # encapsulation
        self._hp = hp
        self._mana = mana
        self._attack = attack
        self._defence = defence

    def run(self, num_of_blocks):
        print(f'{self._name} runs {num_of_blocks} blocks')


class Archer(Player):  # inheritance
    def __init__(self, name='player', hp=100, mana=20, attack=5, defence=2, arrows=1):
        super().__init__(name=name, hp=hp, mana=mana, attack=attack, defence=defence)
        self._arrows = arrows

    def shoot(self):
        print(f"{self._name} shoots {self._attack}")

    def run(self, num_of_blocks):  # polymorphism
        Player.run(self, num_of_blocks)
        print(f'while shooting {self._arrows} arrows')


player1 = Archer("Archer", arrows=10)
player2 = Player()

player2.run(1)  # abstraction
player1.shoot()
player1.run(10)
