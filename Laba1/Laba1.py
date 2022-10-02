import json
import sys

class ErrorType(Exception):
    """ """
    def 

class Bird:
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
            if type(data)==type(list):
                for el in data:
                    json.dump(el.__dict__, write_file, indent = 4)
            elif type(data)==type(Bird):
                json.dump(el.__dict__, write_file, indent = 4)
            elif type(data) == type(Mammal):
                json.dump(el.__dict__, write_file, indent = 4)
            else:
                return Exception 


bird2 = Bird("1", 1, "bb")
bird3 = Bird("2", 2, "3b")

l = [bird1, bird2, bird3]

FileManager.JSONSerialization(l)

GodSkill.allDie()
