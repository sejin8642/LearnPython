# this script surveys try, except, raise, and finally keywords
# exceptions are objects

print()
try:
    print('x' + 1) # this will raise TypeError
    print('x + 1')
except TypeError: # this handles the raised error
    print('1) TypeError occured.')

print()
try:
    raise # this will raise RuntimeError. Other type of error can be raised when specified
except RuntimeError: # when no expression is specified, except handles all types of error
    print('2) RuntimeError was raised.')

print()
try:
    raise
except (TypeError, RuntimeError): # use parentheses to handle a variety of error types.
    print('3) TypeError or RuntimeError has been handled.')
finally: # finally statement will be executed no matter error is handled or not.
    print('3) finally statement executed.')

print()
try:
    print('4) no error occurs/') 
except (TypeError, RuntimeError):
    print('4) TypeError or RuntimeError has been handled.')
else:
    print('4) Else statement executed.')
finally:
    print('4) finally statement executed.')
# The else-clause itself is interesting. It runs when there is no exception 
# but before the finally-clause. That is its primary purpose. Without the else-clause,
# the only option to run additional code before finalization would be the 
# clumsy practice of adding the code to the try-clause. That is clumsy because it 
# risks raising exceptions in code that wasn't intended to be protected by the try-block.
# Another use-case for the else-clause is to perform actions that must occur when 
# no exception occurs and that do not occur when exceptions are handled. For example: