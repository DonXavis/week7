import random

class Pokemon: 
    def __init__(self, name, typo, attacks, hp, weakness):
        self.name = name
        self.type = typo
        self.attacks = attacks
        self.hp = hp
        self.weakness = weakness
        self.status = "awake"

    #print print hp
    def get_status(self):
        print(f"{self.name}: HP: {self.hp} STATUS: {self.status}")

    #print move list
    def get_attacks(self):
        for k, v in self.attacks.items():
            print (k, v)

    def run_attack(self):
        attack = random.choice(list(self.attacks.keys()))
        damage = self.attacks[attack]
        print(f"You attacked with {attack} and it did {damage} damage")


bulba = Pokemon("balbasaur", "Grass", {"tackle": 10, "vine whip": 20, "razor leaf": 25, "hyper beam": 35}, 100, "Fire")
squirt = Pokemon("squirtle", "Water", {"tackle": 10, "water gun": 20, "bubble": 25, "hydro pump": 35}, 100, "Electric")
charchar = Pokemon("charmander", "Fire", {"tackle": 10, "ember": 20, "fire blast": 25, "flame wheel": 35}, 100, "Water")

squirt.run_attack()
squirt.run_attack()
charchar.run_attack()