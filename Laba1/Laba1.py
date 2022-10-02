import xml.etree.ElementTree as ET
import json
import sys

class Bird: # JSON
    def __init__(self, name="", speed=0, color=""):
        self.name = name
        self.speed = speed
        self.color = color

    def __del__(self):
        print("Bird " + self.name + " deleted.")

    def getDict(self):
        data = {}
        data["speed"] = self.speed
        data["color"] = self.color
        return data

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

    def getDict(self):
        data = {}
        data["type"] = self.type
        data["age"] = self.age
        return data

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
            json.dump(data, write_file, indent = 4)
            
    @staticmethod
    def JSONdeserialization(path = "data_file.json"):
        with open(path, "r") as read_file:
            data = json.load(read_file)
            l = []
            for el in data["birds"]:
                print(el)
                l.append(Bird(el, int(data["birds"][el]["speed"]), data["birds"][el]["color"]))
        return l

    @staticmethod
    def XMLserialization(data):
        root = ET.Element("mammals")
        mammalName = ET.SubElement(root, data.name)
        mType = ET.SubElement(mammalName, "Type")
        mType.text = data.type
        mAge = ET.SubElement(mammalName, "Age")
        mAge.text = str(data.age)
        
        s = ET.tostring(root, encoding="utf-8", method="xml")
        s = s.decode("UTF-8")
        with open(f"data_file_{data.name}.xml", "w") as wf:
            wf.write(s)



    @staticmethod
    def XMLdeserialization(path = "data_file.xml"):
        l = []
        tree = ET.parse(path)
        root = tree.getroot()
        for el in root:
            l.append(Mammal(el.tag, el[0].text, int(el[1].text)))
        return l


#bird2 = Bird("1", 1, "bb")
#bird3 = Bird("2", 2, "3b")

#birds = {}

#birds[bird1.name] = bird1.getDict()
#birds[bird2.name] = bird2.getDict()

#data = {}

#data["birds"] = birds

#FileManager.JSONSerialization(data)

#l = FileManager.JSONdeserialization()
#for el in l:
#    print(el.getDict())
a1 = Mammal("Vasya", "Zebra", 12)
a2 = Mammal("Petya", "Wolk", 1)
a3 = Mammal("Tigar", "LEV", 16)

mammals = {}

mammals[a1.name] = a1.getDict()
mammals[a2.name] = a2.getDict()
mammals[a3.name] = a3.getDict()


data = {}

data["mammals"] = mammals

FileManager.XMLserialization(a1)



l = FileManager.XMLdeserialization("data_file_Vasya.xml")
for el in l:
    print(el.__dict__)
GodSkill.allDie()



    