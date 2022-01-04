from robot import Robot
from weapon import Weapon

class Fleet:
    def __init__(self):
        self.robots_fleet = []
        self.create_fleet()

    def create_fleet(self):
        weapon_one = Weapon('spunch', 15)
        weapon_two = Weapon('sword', 25)
        weapon_three = Weapon('blaster', 35)

        robot_one = Robot('Brian', weapon_one)
        robot_two = Robot('Jeff', weapon_two)
        robot_three = Robot('Joey', weapon_three)

        self.robots_fleet.append(robot_one)
        self.robots_fleet.append(robot_two)
        self.robots_fleet.append(robot_three)

    def fleet_list(self):
        for robots in self.robots_fleet:
            print(robots)

# i want to display the complete fleet for the user