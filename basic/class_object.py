class Person:
    #class variable is for class variable not for object
    amount = 0

    #constructor
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
        Person.amount +=1

    #deconstructor
    def __del__(self):
        Person.amount -= 1



    def __str__(self):
        return "Name : {}, Age : {}, height : {}".format(self.name, self.age, self.height)

person1 = Person("aj", 22, 1.71)
person2 = Person("jk", 22, 1.71)
del person2

# print(person1)
print(Person.amount)




