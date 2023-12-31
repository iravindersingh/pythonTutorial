import time


def time_execution(fn):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = fn(*args, **kwargs)
        end = time.time()
        print(f" {fn.__name__} total time consume {(end-start)*1000}")
        return result
    return wrapper


@time_execution
def calculate_sqr(nums):
    result = []
    for i in nums:
        result.append(i*i)
    return result

@time_execution
def calculate_root(nums):
    result = []
    for i in nums:
        result.append(i*i*i)
    return result

a = [1,2,3,4,5,6,1,2,3,4,5,6,1,2,3,4,5,6,1,2,3,4,5,6,1,2,3,4,5,6]
sqr = calculate_sqr(a)
root = calculate_root(a)

print(sqr)
print(root)


#--------------------------------------##-----------------------------------------#


def getIntro(fn):
    def wrapper(*args, **kwargs):
        print("Hello")
        result = fn(*args, **kwargs)
        return result
    return wrapper

@getIntro
def getName():
    print("my name is wrath")

@getIntro
def getAge():
    print("my age is 22")

getAge()