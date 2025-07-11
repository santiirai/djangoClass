# class hello:
#     name = "Ram"
# h = hello()
# print(h.name)

class hello:
    def __init__(self, name, age): #creating a constructor
        self.name = name
        self.age = age
    def disc(self):
        print(f"My name is {self.name} and age is {self.age}")
    
    def __str__(self):
        return self.name
# a = hello("aaaaaa", 20)
# print(a)
        
# h = hello("shanti", 21) #creating an object
# h.name = "sasa"
# h.disc()
# print(h.disc())
# print(h.name, h.age)





class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def stud(self):
        print("He is {self.name} and his age is {self.age}")

s = student("Ram", 12)
# print(s.name, s.age)
s.stud()


