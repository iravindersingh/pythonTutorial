def add(a,b):
    print(__name__)
    return a+b

# always excuting file name will as __main__
if __name__ == '__main__':
    print("checking call method")
    print(add(5, 10))

    def sub(a, b):
        return a-b