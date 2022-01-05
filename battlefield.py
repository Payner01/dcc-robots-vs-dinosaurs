from fleet import Fleet
from herd import Herd


class Battlefield:
    def __init__(self) -> None:
        self.fleet = Fleet()
        self.herd = Herd()
    def run_game(self):
        self.display_welcome()
        #self.fleet.fleet_list()
        self.robo_turn()
        pass
    def display_welcome(self):
        print("welcome to RvD")
        pass
    def battle(self):
        pass
    def dino_turn(self):
        pass
    def robo_turn(self):
        self.show_robo_opponent_options()
        robot_index = int(input("Select the Robot you want to attack with  "))
        self.show_dino_opponent_options()
        dino_index = int(input("Select the dinosaur you want to attack"))
        print(self.fleet.robots_fleet[robot_index].name)
        print(f'{self.herd.dinosaurs_herd[dino_index].name} will be attacked by {self.fleet.robots_fleet[robot_index].name} ')
        pass
    def show_dino_opponent_options(self):
        print("Current Dino Herd")
        i = 0
        for dino in self.herd.dinosaurs_herd:
            print(f'Press {i} to select {dino.name} ({dino.health} health)')
            i += 1

    def show_robo_opponent_options(self):
        print("Current Robot Fleet")
        i = 0
        for robot in self.fleet.robots_fleet:
            print(f'Press {i} to select {robot.name} ({robot.health} health)')
            i += 1
    def display_winners(self):
        pass
