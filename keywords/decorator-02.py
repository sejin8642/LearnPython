# this script surveys concept of decorator

from decoratorModule import *
    
@repeatDec(4)
def wrappee1():
    print('this is wrappee1 function printing.')
    
print(wrappee1())
print()

