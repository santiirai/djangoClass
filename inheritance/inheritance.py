# class animal:
#     def __init__(self, name):
#         self.name =name

# class person(animal):
#     def __init__(self,age,name):
#         super().__init__(name) #animal.__init__
#         self.age = age

# p = person(4,"Ram")
# print(p.name)

class animal:
    def __init__(self, name):
        self.name = name

class human:
    def __init__(self, age):
        self.age = age

class student(animal, human):
    def __init__(self, name, age, faculty):
        animal.__init__(self, name)
        human.__init__(self, age)
        self.faculty = faculty

a = student("Hari", 12, "BCA")
print(a.name)
print(a.age)
print(a.faculty)

        