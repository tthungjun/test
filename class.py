'''class Person:
    def __init__(self, name):
        self. name = name
    def get_name_uppercase(self):
        return self. name. upper()
    
class Student(Person):
    def __init__(self, name, major):
        super().__init__(name)
        self. major = major
    def get_name_uppercase(self):
        return self. name. capitalize()
    def get_major_upper(self):
        return self. major. upper()
    
s1 = Student("Ha", "computer engineering")
print(super(Student, s1). get_name_uppercase())
print(s1. get_major_upper())'''



class Person:
    __slots__ = ["name", "age"]
    weight = 74
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Park", 20)
Person .weight = 84
print(p.weight)