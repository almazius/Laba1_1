from abc import abstractmethod
import xml.etree.ElementTree as ET
import json
import sys
import xml
import os
from msvcrt import getch

class Animal:
    @abstractmethod
    def getDict():
        """Get dictionary"""


class Bird(Animal): # JSON
    def __init__(self, name: str = "", speed: int = 0, color: str = ""):
        self.name = name
        self.speed = speed
        self.color = color
        #except AttributeError:
        #    print("Uncorrected object")
        #except Exception:
        #    print("Error")


    def __del__(self):
        try:
            print("Bird " + self.name + " deleted.")
        except AttributeError:
            print("Uncorrected object")
        except Exception:
            print("Error")

    def getDict(self):
        data = {}
        data["speed"] = self.speed
        data["color"] = self.color
        return data

    def getStart(self):
        print("Bird like fly! They're already flying!")

    def die(self):
        try:
            print("Minus one bird... We will remember her as one of the best!")
            del self
        except AttributeError:
            print("Uncorrected object")
        except Exception:
            print("Error")

# end Bird

class Mammal(Animal):
    def __init__(self, name="", Type="", age=0):
        try:
            self.name = name
            self.type = Type
            self.age = age
        except AttributeError:
            print("Uncorrected object")
        except Exception:
            print("Error")


    def __del__(self):
        try:
            print("Mammal " + self.name + " deleted.")
        except TypeError:
            print("Uncorrected value")
        except Exception:
            print("Error")

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
    birds = []
    mammals = []

    @staticmethod
    def begin():
        print("Hi, this god simulator!")
        
        while True:
            print("What you want?\n  1) Create bird\n  2) Create mammal\n  3) Kill bird\n  4) Kill mammal\n  5) Create JSON on bird")
            print("  6) Create XML on mammal\n  7) Create bird from JSON\n  8) Create mammal from XML\n  9) Kill this f*cking world")
            print("  SPASE) check population")
            print("P.S. press key (1-9 or SPACE)")
            n = ord(getch())
            os.system('CLS')
            if n == 49:
               GodSkill.createBird() 
            elif n==50:
                GodSkill.createMammal()
            elif n==51:
                GodSkill.killBird()
            elif n==52:
                GodSkill.killMammal()
            elif n==53:
                GodSkill.createJSON()
            elif n == 54:
                GodSkill.createXML()
            elif n == 55:
                GodSkill.CreateBirdFromJSON()
            elif n == 56:
                GodSkill.CreateMammalFromXML()
            elif n==57:
                GodSkill.KillWorld()
            elif n==32:
                print("Brids:")
                for el in GodSkill.birds:
                    print(el.__dict__)
                print("Mammals:")
                for el in GodSkill.mammals:
                    print(el.__dict__)

    @staticmethod
    def createBird():
        print("Write data (name speed color)")
        try:
            name = input()
            if name >= '0' and name<='9':
                raise Exception
            speed = input()
            color = input()
            if color >= '0' and color<='9':
                raise Exception
            GodSkill.birds.append(Bird(name, int(speed), color))
        except ValueError:
            print("Incorrect value")
        except Exception:
            print("Error")


    @staticmethod
    def createMammal():
        print("Write data (name type age)")
        try:
            name = input()
            if name >= '0' and name<='9':
                raise Exception
            Type = input()
            if Type >= '0' and Type<='9':
                raise Exception
            age = input()
            GodSkill.mammals.append(Mammal(name, Type, int(age)))
        except ValueError:
            print("Incorrect value")
        except Exception:
            print("Error")


    @staticmethod
    def killBird():
        try:
            print("I don't like what you're doing")
            GodSkill.birds[-1].die()
            GodSkill.birds.pop()
        except IndexError:
            print("Error index. Mb all birs is die?")
        except Exception:
            print("Error")
    @staticmethod 
    def allDie():
        print("World is lost...")
        sys.exit()


    @staticmethod
    def killMammal():
        try:
            GodSkill.mammals.pop()
        except IndexError:
            print("Error index. Mb all mammal is die?")
        except Exception:
            print("Error")

    @staticmethod
    def createJSON():
        try:
            dBirds = {}
            data = {}
            if len(GodSkill.birds) == 0:
                print("We have't birs!")
            else:
                for el in GodSkill.birds:
                    dBirds[el.name] = el.getDict()
                data["birds"] = dBirds
                FileManager.JSONSerialization(data)
        except Exception:
            print("Error")


    @staticmethod
    def createXML():
        try:
            if len(GodSkill.mammals) == 0:
                print("We have't mammals")
            else:
                FileManager.XMLserialization(GodSkill.mammals)
        except Exception:
            print("Error")


    @staticmethod 
    def CreateBirdFromJSON():
        try:
            print("Write path or send emply string")
            l = []
            s = input()
            if s == "":
                l = FileManager.JSONdeserialization()
            else:
                l = FileManager.JSONdeserialization(s)
            birds = birds+l
        except Exception:
            print("Error")
        else:
            print("Success")

    @staticmethod 
    def CreateMammalFromXML():
        try:
            print("Write path or send emply string")
            l = []
            s = input()
            if s == "":
                l = FileManager.XMLdeserialization()
            else:
                l = FileManager.XMLdeserialization(s)
            mammals = mammals+l
        except Exception:
            print("Error")
        else:
            print("Success")

    @staticmethod 
    def KillWorld():
        try:
            GodSkill.allDie()
        except Exception:
            print("Error")


    @staticmethod 
    def killBird(obj):
        try:
            obj.die()
        except AttributeError:
            print("Uncorrected object")
        except Exception:
            print("Error")


    @staticmethod 
    def bornBird():
        try:
            return Bird("Alex", 12, "red")
        except Exception:
            print("Error")


    @staticmethod 
    def bornMammal():
        try:
            return Mammal("Tapok", "zebra", 0)
        except Exception:
            print("Error")

# end GodSkill



class FileManager:
    @staticmethod
    def JSONSerialization(data, path:str = "data_file.json"):
        try:
            with open(path, "w") as write_file:
                json.dump(data, write_file, indent = 4)
        except AttributeError:
            print("Uncorrected object")
        except Exception:
            print("Error")


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
        for el in data:
            mName = ET.Element(el.name)
            mType = ET.SubElement(mName, "Type")
            mType.text = el.type
            mAge = ET.SubElement(mName, "Age")
            mAge.text = str(el.age)
            root.append(mName)

        print(root)
        s = ET.tostring(root, encoding="utf-8", method="xml")
        s = s.decode("UTF-8")
        with open(f"data_file_name.xml", "w") as wf:
            wf.write(s)


    @staticmethod
    def XMLdeserialization(path: str = "data_file.xml"):
        try:
            l = []
            tree = ET.parse(path)
            root = tree.getroot()
            for el in root:
                l.append(Mammal(el.tag, el[0].text, int(el[1].text)))
            return l
        except FileNotFoundError:
            print("File not found")
        except xml.etree.ElementTree.ParseError: 
            print("File uncorrected")
        except Exception:
            print("Error")

#end FileManager

GodSkill.begin()

#m = []
#m.append(Mammal("oleg", "volk", 12))
#m.append(Mammal("igo", "lev", 12))
#m.append(Mammal("inav", "tigar", 12))

#FileManager.XMLserialization(m)

#l =[]

#l = FileManager.XMLdeserialization("data_file_name.xml")
#for el in l:
#    print(el.__dict__)