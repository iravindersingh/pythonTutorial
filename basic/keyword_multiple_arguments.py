def person(name, **data):
    print(name)
    print(data)
    for i,v in data.items():
        print(i,v)

person("naveen", age=28, phone="4567890", city="Mumbai")