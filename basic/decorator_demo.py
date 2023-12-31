
import logging

def modifyDeco(fx):

    def inner_modify(*args,**kwargs):

        a = args[0]
        b = args[1]

        if a < b:
            a,b = b,a

        dev = fx(a,b)
        return dev
    return inner_modify


@modifyDeco
def div(a,b):
    print(a / b)


div(10,20)

