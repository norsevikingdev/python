class Player:
    def __init__(self, name="player", hp=100, mana=20, attack=5, defence=2):
        self._name = name.capitalize()  # encapsulation
        self._hp = hp
        self._mana = mana
        self._attack = attack
        self._defence = defence

    def run(self, num_of_blocks):
        print(f'{self._name} runs {num_of_blocks} blocks')

    def attack(self):
        return self._attack

    def take_damage(self, damage):
        minus_armor = damage - self._defence
        if(minus_armor > 0):
            self._hp = self._hp - (damage - self._defence)


class Archer(Player):  # inheritance
    def __init__(self, name='player', hp=100, mana=20, attack=5, defence=2, arrows=1):
        super().__init__(name=name, hp=hp, mana=mana, attack=attack, defence=defence)
        self._arrows = arrows

    def shoot(self):
        print(f"{self._name} shoots {self._attack}")

    def run(self, num_of_blocks):  # polymorphism
        Player.run(self, num_of_blocks)
        print(f'while shooting {self._arrows} arrows')

    def attack(self):
        return self._attack * self._arrows


archer1 = Archer("Archer", 250, 10, 2, arrows=10)
player2 = Player(attack=22)

player2.take_damage(archer1.attack())
archer1.take_damage(player2.attack())

print(f'{archer1._name} takes {player2.attack() - archer1._defence} damage and current HP is {archer1._hp}')
print(f'{player2._name} current HP is {player2._hp}')
