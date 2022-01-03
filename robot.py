from weapon import Weapon

class Robot:
    def __init__(self, name) -> None:
        self.name = ''
        self.health = 100
        self.weapon = None
    
    def attack(self,dinosaur):
        self.dinosaur = None