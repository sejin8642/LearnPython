# this module contains decorators to survey the concept

# In Python, functions are first-class objects. This means that functions can be passed around and used as arguments, just like any other object (string, int, float, list, and so on). See the following code.
import functools

def myDecorator(func):
    @functools.wraps(func) # this decorator preserves identity of the wrapped function 
    def wrapper(*args, **kwargs):
        print('start!')
        returnValue = func(*args, **kwargs)
        print('finished!')
        return returnValue
    return wrapper

def repeatDec(nums): # this decorator takes an input
    def myDecorator(func):
        @functools.wraps(func) # this decorator preserves identity of the wrapped function 
        def wrapper(*args, **kwargs):
            print('start!')
            for _ in range(nums):
                returnValue = func(*args, **kwargs)
            print('finished!')
            if returnValue == None:
                return nums
            else:
                return returnValue
        return wrapper
    return myDecorator