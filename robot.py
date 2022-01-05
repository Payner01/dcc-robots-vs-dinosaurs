from weapon import Weapon

class Robot:
    def __init__(self, name, weapon):
        self.name = name
        self.health = 100
        self.weapon = weapon

    def attack_dinosaur (self, attack_dinosaur):
        attack_dinosaur.health -= self.weapon.attack_power
        print(f'{attack_dinosaur.name} health is now {attack_dinosaur.health}')
        

