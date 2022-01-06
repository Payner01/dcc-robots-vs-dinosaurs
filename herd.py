from dinosaur import Dinosaur


class Herd:
    def __init__(self):
        self.dinosaurs_herd = []
        self.create_herd()

    def create_herd(self):
        dino_one = Dinosaur("T-rex")
        dino_two = Dinosaur("Triceratops")
        dino_three = Dinosaur("Velociraptor")

        self.dinosaurs_herd.append(dino_one)
        self.dinosaurs_herd.append(dino_two)
        self.dinosaurs_herd.append(dino_three)

    def herd_list(self):
        for dino in self.dinosaurs_herd:
            print(dino.name)