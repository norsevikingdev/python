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
        self._name = name.capitalize()
        self._hp = hp
        self._mana = mana
        self._attack = attack
        self._defence = defence

    def run(self, num_of_blocks):
        print(f'{self._name} runs {num_of_blocks} blocks')


class Archer(Player):
    def __init__(self, name='player', hp=100, mana=20, attack=5, defence=2):
        super().__init__(name=name, hp=hp, mana=mana, attack=attack, defence=defence)

    def shoot(self):
        print(f"{self._name} shoots {self._attack}")


player1 = Archer("robin", attack=30)
player1.shoot()
player1.run(10)
