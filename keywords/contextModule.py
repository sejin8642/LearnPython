# this script surveys concept of context manager

# A context manager is an object that defines the runtime context to be established when executing a with statement. The context manager handles the entry into, and the exit from, the desired runtime context for the execution of the block of code. Simple implementations are shown below

class contextManager():
    def __init__(self):
        pass

    def __enter__(self):
        print('enter method is invoked first!!')
    
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type == None:
            print('No exception raised.')
        else:
            print('the following error was raised:')
            print(exc_type)
        return True # raised exception is always suppressed
    
class contextManagerAs():
    def __init__(self):
        self.eType = None
        self.eValue = None
        self.traceback = None

    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.eType = exc_type
        self.eValue = exc_value
        self.traceback = traceback
        return True # raised exception is always suppressed