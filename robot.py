from weapon import Weapon

class Robot:
    def __init__(self, name, weapon):
        self.name = name
        self.health = 100
        self.weapon = weapon

    def attack_dinosaur (self, attack_dinosaur, dinosaur_list):
        attack_dinosaur.health -= self.weapon.attack_power
        print(f"{attack_dinosaur.name}'s health is now {attack_dinosaur.health}")
        if attack_dinosaur.health <= 0:
            dinosaur_list.remove(attack_dinosaur)
            print(f'{attack_dinosaur.name} has been eliminated from the game by {self.name}')
        

