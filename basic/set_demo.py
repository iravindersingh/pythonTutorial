#set is the collection of unique element
#set dont follow any sequence
#set we dont have the indexing

s = {79,88,2,4,6,4,6,79,3}
print(s)

#this is how we add element in set
s.add(9)
print(s)

#remove element randomly
print(s.pop())

#remove element by element
s.remove(79)
print(s)

s1 = {1,2,3,4,5,6}

#give elements which not matched
print(s.difference(s1))

#union of 2 sets
print(s | s1)

#gives sets which exist in all sets
print(s & s1)

#gives element which not exist in second sets
print(s - s1)

#symatric diff which gives element which exist either sets but not in both
print(s ^ s1)

#remove all element
s.clear()
print(s)

