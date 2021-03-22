# this script surveys concept of __call__ method of class

class calleeClass():
    def __init__(self, name):
        self.name = name
        
    def __call__(self, rn): # this allows class to act as function when called
        for _ in range(rn):
            print(self.name + '!')

classA = calleeClass('Sejin')
classA(3)
print()

class decoratorClass():
    def __init__(self, func):
        self.func = func
        
    def __call__(self, rn):
        for _ in range(rn):
            self.func()

@decoratorClass
def shout():
    print('hey!!!')
    
shout(3)