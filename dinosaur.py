

class Dinosaur:
    def __init__(self, name):
        self.name = name
        self.attack_power = 10
        self.health = 100

    def attack(self, attack_robot):
        attack_robot
        attack_robot.health -= self.attack_power
        print (f' {attack_robot.name} health is now {attack_robot.health}')
        