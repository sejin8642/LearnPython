# this script surveys concept of decorator

from decoratorModule import *

def wrappee1():
    print('this is wrappee1 function printing.')

wrappee1 = myDecorator(wrappee1)
print(wrappee1())
print()

# the following implementation is equivalent to the above. Here myDecorator is a decorator: Decorators wrap a function, modifying its behavior.
@myDecorator
def wrappee2(x, y, z):
    returnX = lambda ox: ox
    returnX = returnX(x)
    while x < 5:
        print('this is wrappee2 function printing.')
        x += 1
    return returnX

print(wrappee2(2, 2, 3))
print()

@myDecorator
@myDecorator
def wrappee3():
    print('this is wrappee3 function printing.')
    
wrappee3()
print()