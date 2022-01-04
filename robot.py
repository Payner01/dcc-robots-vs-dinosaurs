from weapon import Weapon

class Robot:
    def __init__(self, name, Weapon):
        self.name = name
        self.health = 100
        self.weapon = Weapon
        self.weapon_choice = ['sword', 'blaster', 'punch']

    def attack_dinosaur (self,dinosaur):
        self.dinosaur = dinosaur
        
#wager example
