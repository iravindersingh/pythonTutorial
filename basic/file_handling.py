
#open a file in write mode and if file is not there then it will create a new file
f = open('new_file', 'w')
f.write("something")

f = open('new_file', 'a')
f.write("  mobile")

f = open('new_file', 'r')
print(f)


#if you open a file it make sure already exist
f = open('new_file', 'w')
# print(f.readline())
# print(f.read())
# print(f.readline(4))
# print(f.read(4))

f2 = open('class_object.py', 'r')

for data in f2:
    print(data)
    f.write(data)
