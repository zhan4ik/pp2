class Human:
    def __init__(self, gender):
        self.gender = gender
    def printInfo(self):
        print(self.gender)
        
    def printTriangle(self, n):
        for i in range(n):
            for j in range(i+1):
                print(j+1, end="")
            print("")

class Person(Human):
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality
    def printInfo(self):
        print(self.name, self.nationality)
    def setSurname(self, surname):
        self.surname = surname
    def getSurname(self):
        print(self.surname)    

        
class Student(Person):
    def __init__(self, name, nationality, id):
        Person.__init__(self, name, nationality)
        self.id = id
    def printInfo(self):
        print(self.name, self.nationality, self.id)


class Teacher(Person):
    def __init__(self, name, nationality, teacher_id):
        Person.__init__(self, name, nationality)
        self.teacher_id = teacher_id
    def printInfo(self):
        print(self.name, self.nationality, self.teacher_id)

objhuman = Human("Male")
objhuman.printInfo()
objhuman.printTriangle(5)

obj = Person("Donald", "American")
obj.printInfo()
obj.setSurname("Trump")
obj.getSurname()
 
obj1 = Student("Zhangirkhan", "Kazakh", "22B030370")
obj1.printInfo()

obj2 = Teacher("Arnur", "Godlike", "007")
obj2.printInfo()