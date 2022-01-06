from dinosaur import Dinosaur
from fleet import Fleet
from herd import Herd



class Battlefield:
    def __init__(self) -> None:
        self.fleet = Fleet()
        self.herd = Herd()

    def run_game(self):
        self.display_welcome()
        self.battle()
        self.display_winners()
        
    def display_welcome(self):
        print("welcome to Robots vs Dinosaurs")
        print('Each Dinosaur and Robot will start with 100 health')
        print('Dinosaurs belong to a heard while Robots belong to a fleet')
        print('The game will be over once you have defeted the Dinosaurs or the Dinosaurs have defeated you')

    def battle(self):
        print('Robots go first')
        while len(self.fleet.robots_fleet) > 0 and len(self.herd.dinosaurs_herd) > 0:
            self.robo_turn()
            if len(self.herd.dinosaurs_herd) == 0:
                pass
            else:
                self.dino_turn()

    def dino_turn(self):
        self.show_dino_opponent_options()
        dino_index = int(input("Selected the Dinosaur you want to attack with "))
        self.show_robo_opponent_options()
        robot_index = int(input("Select the Robot you want to attack  "))
        print(f'{self.fleet.robots_fleet[robot_index].name} will be attacked by {self.herd.dinosaurs_herd[dino_index].name}')
        self.herd.dinosaurs_herd[dino_index].attack_robot(self.fleet.robots_fleet[robot_index], self.fleet.robots_fleet)

    def robo_turn(self):
        self.show_robo_opponent_options()
        robot_index = int(input("Select the Robot you want to attack with  "))
        self.show_dino_opponent_options()
        dino_index = int(input("Select the Dinosaur you want to attack  "))
        print(f'{self.herd.dinosaurs_herd[dino_index].name} will be attacked by {self.fleet.robots_fleet[robot_index].name}')
        self.fleet.robots_fleet[robot_index].attack_dinosaur(self.herd.dinosaurs_herd[dino_index], self.herd.dinosaurs_herd)
        
        
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
        if self.herd.dinosaurs_herd == 0:
            print('The Dinosaurs have won!')
        else:
            print('The Robots have won!')
