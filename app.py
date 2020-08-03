bows = [
    {'name': 'Hell Bow', 'dmg': 20},
    {'name': 'Winter Bow', 'dmg': 10},
    {'name': 'Star Bow', 'dmg': 50},
]

arrow_types = [
    {'name': 'normal arrows', 'dmg': 5},
    {'name': 'fire arrows', 'dmg': 3}
]


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
        return minus_armor


class Archer(Player):  # inheritance
    def __init__(self, name='player', hp=100, mana=20, attack=5, defence=2, bow=bows[0], arrow=arrow_types[0]):
        super().__init__(name=name, hp=hp, mana=mana, attack=attack, defence=defence)
        self._bow = bow
        self._arrow = arrow

    def shoot(self):
        print(f"{self._name} shoots {self._attack}")

    def run(self, num_of_blocks):  # polymorphism
        Player.run(self, num_of_blocks)
        print(f'while shooting arrows')

    def attack(self):
        return self._attack * (self._bow['dmg'] + self._arrow['dmg'])


archer1 = Archer("Archer", attack=1, bow=bows[2])
player2 = Player(attack=22)

print(f'{archer1._name} takes {archer1.take_damage(player2.attack())} damage and current HP is {archer1._hp}')
print(f'{player2._name} takes {player2.take_damage(archer1.attack())} damage and current HP is {player2._hp}')
