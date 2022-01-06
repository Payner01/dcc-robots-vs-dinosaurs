import random

class Dinosaur:
    def __init__(self, name):
        self.name = name
        self.attack_power = random.randint(25, 50)
        self.health = 100

    def attack_robot(self, attack_robot, robot_list):
        attack_robot.health -= self.attack_power
        print (f"{attack_robot.name}'s health is now {attack_robot.health}")
        if attack_robot.health <= 0:
            robot_list.remove(attack_robot)
            print(f'{attack_robot.name} has been eliminated from the game by {self.name}')
