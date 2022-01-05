from dinosaur import Dinosaur
from fleet import Fleet
from herd import Herd



class Battlefield:
    def __init__(self) -> None:
        self.fleet = Fleet()
        self.herd = Herd()

    def run_game(self):
        self.display_welcome()
        #self.fleet.fleet_list()
        self.battle()
        
    def display_welcome(self):
        print("welcome to Robots vs Dinosaurs")
        print('Each Dinosaur and Robot will start with 100 health')
        print('Dinosaurs belong to a heard while Robots belong to a fleet')
        print('The game will be over once you have defeted the Dinosaurs')

    def battle(self):
        print('Robots are always first')
        self.robo_turn()
        self.dino_turn()



    def dino_turn(self):
        self.herd.dinosaurs_herd[0].attack_robot(self.fleet.robots_fleet[0])

    def robo_turn(self):
        self.show_robo_opponent_options()
        robot_index = int(input("Select the Robot you want to attack with  "))
        self.show_dino_opponent_options()
        dino_index = int(input("Select the dinosaur you want to attack  "))
        print(f'{self.herd.dinosaurs_herd[dino_index].name} will be attacked by {self.fleet.robots_fleet[robot_index].name}')
        self.fleet.robots_fleet[0].attack_dinosaur(self.herd.dinosaurs_herd[0])
        
        
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
