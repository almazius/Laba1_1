from asyncore import write
import json
import sys
import os

class ErrorType(Exception):
    """ """
    def __init__(self, message="This type dont serelization."):
        self.message = message;
        super().__init__(self.message)

#end ErrorType

class Bird: # JSON
    def __init__(self, name="", speed=0, color=""):
        self.name = name
        self.speed = speed
        self.color = color

    def __del__(self):
        print("Bird " + self.name + " deleted.")


    def getStart(self):
        print("Bird like fly! They're already flying!")

    def die(self):
        print("Minus one bird... We will remember her as one of the best!")
        del self
# end Bird

class Mammal:
    def __init__(self, name="", Type="", age=0):
        self.name = name
        self.type = Type
        self.age = age

    def __del__(self):
        print("Mammal " + self.name + " deleted.")


    def getSound(self):
        print("*noise*")

    def born(self):
        print(self.name + " created descendant")
        return Mammal(self.name+"_1", self.type, 0)

# end Mammal

class GodSkill:
    @staticmethod 
    def allDie():
        print("World is lost...")
        sys.exit()

    @staticmethod 
    def killBird(obj):
        obj.die()

    @staticmethod 
    def bornBird():
        return Bird("Alex", 12, "red")

    @staticmethod 
    def bornMammal():
        return Mammal("Tapok", "zebra", 0)

# end GodSkill

bird1 = GodSkill.bornBird()
print(bird1.name + " " + str(bird1.speed) + "  " + bird1.color)


class FileManager:
    @staticmethod
    def JSONSerialization(data):
        with open("data_file.json", "w") as write_file:
            write_file.write("[\n")
            for i  in range(len(data)-1):
                json.dump(data[i].__dict__, write_file, indent = 4)
                write_file.write(',\n')
            json.dump(data[-1].__dict__, write_file, indent = 4)
            write_file.write("\n]")

    @staticmethod
    def JSONdeserialization(path = "data_file.json"):
        l=[]
        with open(path, "r") as read_file:
            data = json.load(read_file)
            for el in data:
                l.append(Bird(el["name"], el["speed"], el["color"]))
        return l

bird2 = Bird("1", 1, "bb")
bird3 = Bird("2", 2, "3b")

#l = [bird1, bird2, bird3]

#FileManager.JSONSerialization(l)

l = FileManager.JSONdeserialization("data_file.json")
for el in l:
    print("Name: " + el.name + " Speed: " + str(el.speed) + " clolor: " + el.color + "\n")

GodSkill.allDie()
