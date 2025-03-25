class Animal:
    def __init__(self, breed, name, colour):
        self.breed = breed
        self.name = name
        self.colour = colour
    def hunt(self):
        print(f"{self.name} the {self.colour} {self.breed} is hunting ")


    def sleep(self):
        print(f"{self.name} the {self.colour} {self.breed} is sleeping")


    def eat(self):
        print(f"{self.name} the {self.colour} {self.breed} is eating ")




class Lion(Animal):
    def __init__(self, breed, name, colour, mane, strength):
        super().__init__(breed, name, colour)                    
        self.mane = mane
        self.strength = strength 


class Shark(Animal):
    def __init__(self, breed, name, colour, speed, movement):
        super().__init__(breed, name, colour)
        self.speep = speed
        self.movement = movement  


class Human(Animal):
    def __init__(self, breed, name, colour, walk, talk):
        super().__init__(breed, name, colour)
        self.walk = walk
        self.talk = talk
lion = Lion("African lion", "King", "brown", "long", "supper strength")
shark = Shark("Hunter_shark", "Mega", "Grey", "swimmer", "lightening_speed")
human = Human("Asian", "Hun", "white", "walking", "walking_pace") 
print(shark.breed)
print(lion.strength)
print(human.walk)                  