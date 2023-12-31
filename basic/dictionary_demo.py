data = {
    1:"rav",
    2:"harsh",
    3:"naveen"
}
print(data)

#fetch by key but it should be exist otherwise it will give error
print(data[1])

#fetch by key but if key not exist. it will not return none but not give error
print(data.get(4))

#ftech by key. if not exist then we can pass message in second parameter
print(data.get(4, 'Not found'))

listA = ["rav", "aj", "tarun"]
listB = ["singh", "rawat", "jk"]

#with zip and convert to dic we can create dict with two list
print(dict(zip(listA,listB)))

data = dict(zip(listA,listB))
data["Monika"] = "Garg"
print(data)

#delete based on key
del data["Monika"]
