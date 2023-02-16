class Human:
    def __init__(self, gender):
        self.gender = gender
    def printInfo(self):
        print(self.gender)
        
obj = Human("Male")
obj.printInfo()