#A Generator in Python is a function that returns an iterator using the Yield keyword.

def top_ten():
    n = 1;
    while(n <= 10):
        yield n*n
        n += 1
# print(top_ten())

value = top_ten()

for i in value:
    print(i)