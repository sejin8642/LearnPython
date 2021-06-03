# this script surveys the concept of with statement

# The execution of the with statement with one “item” proceeds as follows: 
# 1) The context expression (the expression given in the with_item) is evaluated to obtain a context manager. 
# 2) The context manager’s __exit__() is loaded for later use. 
# 3) The context manager’s __enter__() method is invoked. 
# 4) If a target was included in the with statement, the return value from __enter__() is assigned to it. 
# 5) The suite is executed. 
# 6) The context manager’s __exit__() method is invoked. If an exception caused the suite to be exited, its type, value, and traceback are passed as arguments to __exit__(). Otherwise, three None arguments are supplied. If the suite was exited due to an exception, and the return value from the __exit__() method was false, the exception is reraised. If the return value was true, the exception is suppressed, and execution continues with the statement following the with statement. If the suite was exited for any reason other than an exception, the return value from __exit__() is ignored, and execution proceeds at the normal location for the kind of exit that was taken.

from contextModule import *

with contextManager(): # contextManager.__enter__() does not return for assignment
    print('with suite!!')
    raise NameError
    
with contextManagerAs() as cma: # see the attributes of cma to study what they are
    print('with-as suite')
    raise NameError
    
print(cma.eType)
print(cma.eValue)
print(cma.traceback)