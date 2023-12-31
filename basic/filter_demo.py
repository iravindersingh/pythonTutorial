# The filter() method filters the given sequence
# with the help of a function that tests each element
# in the sequence to be true or not.
from functools import reduce

lst = [1,2,3,4,5,6,7,8]

def check_greater_than_5(num):
    return num > 5

a = list(filter(check_greater_than_5, lst))
print(a)


lst = [1,2,3,45,67,82,3,4,56,78,96]

evens =list(filter( lambda x:x%2==0,lst))
print(evens)

double_even = list(map(lambda x : x+x,evens))
print(double_even)


sum = reduce(lambda x,y : x +y, double_even)
print(sum)