import random

class Dinosaur:
    def __init__(self, name):
        self.name = name
        self.attack_power = random.randint(0, 25)
        self.health = 100

    def attack_robot(self, attack_robot):
        attack_robot.health -= self.attack_power
        print (f' {attack_robot.name} health is now {attack_robot.health}')
