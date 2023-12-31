class Student:

    def __init__(self, name, role_no):
        self.name = name
        self.role_no = role_no
        self.laptop = self.Laptop()

    def show(self):
        print(f"name : {self.name} role no : {self.role_no}")
        self.laptop.show()

    class Laptop:
        def __init__(self):
            self.brand = "HP"
            self.processor = "i5"

        def show(self):
            print(f"brand : {self.brand} processor : {self.processor}")


s1 = Student("naveen", 1)
s1.show()
