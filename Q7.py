def add(a,b,c="sum of numbers"):
    print(c)
    return a+b
def catch(add,*args,**kwargs):
    for val in args:
        print(val)
    for key,value in kwargs.items():
        print(key,"=",value)
    print(add(*args))

catch(add,1,2,c="this is sum")