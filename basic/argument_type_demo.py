

#default argument
def person(name,age=18):
    print(name)
    print(age)

#position argument
person("aj",19)

#keyword argument
person(age=21, name="rahul")

#variable length
def sum(a,*b):
    print(type(b))
    c = 0
    for i in b:
        c+= i
    print(a + c)
sum(10,20,20)


#* args means taking parameter as tuple
#**kwargs means taking parameter as dic





