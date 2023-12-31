#to make iterator of an class req iter and next method

class TopTen:

    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):

        if self.num <= 10:
            val =  self.num
            self.num += 1
        else:
            raise StopIteration
        return val

top_ten = TopTen()

# print(top_ten)

for i in top_ten:
    print(i)