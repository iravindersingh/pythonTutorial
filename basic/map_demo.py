# map() function returns a map object(which is an iterator) of the results after
# applying the given function to each item of a given iterable (list, tuple etc.) Syntax :
#
# map(fun, iter)


a = [1,23,45,6,7,89]

def abc(a):
    return a*a

print(list(map(abc, a)))

print(list(map(lambda x:x*x, a)))


