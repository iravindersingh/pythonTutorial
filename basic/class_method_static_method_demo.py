

class Student:
    #class variable
    grade = 4

    #inside the constructor arre instant variable
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        print(f"name : {self.name}, age : {self.age} and grad : {self.grade}")

    @classmethod
    def update_grade(cls, grade):
        cls.grade = grade

    #this this method dont have self or cls object so you cant update class or instant variable
    @staticmethod
    def check_age(age):
        if age > 18:
            print("above age")
        else:
            print("below age")


a = Student("jk", 21)
b = Student("ak", 15)



Student.update_grade(20)

Student.check_age(21)


a.get_info()
b.get_info()