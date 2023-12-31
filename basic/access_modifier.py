class A:
    def show(self):
        print("this is A class public show")

    def __private_show(self):
        print("this is A class private show")

    def _protected_show(self):
        print("this is protected show")

class B(A):
    def show(self):
        print("this is B class show")


    a = A()
    a._protected_show()

# a = A()
b = B()
# a.show()
b.show()

