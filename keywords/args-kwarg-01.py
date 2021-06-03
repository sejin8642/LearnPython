# this script surveys concept of *args

def mulArgs(arg1, arg2, arg3):
    return arg1, arg2, arg3

def varArgs(*args):
    return args

def varKwargs(**kwargs):
    return kwargs

n1, n2, n3 = mulArgs(1, 2, 3)
nums = mulArgs(1, 2, 3)
print(type(n1))
print(type(nums))

print('')
tupleN = varArgs(1, 2, 3, 4) # this will return an iterable
print(type(tupleN)) # the iterable type is tuple

print('')
fruits = varKwargs(apple=14, orange=11, pear=5, peach=22, grape=33)
for fruit in fruits:
    print(fruit)

print('')
print(type(fruits)) # the iterable type is dict
fruitIter = iter(fruits) # this iterator only returns keyword when __next__ is invoked
print(type(fruitIter))

print('')
fruitItems = fruits.items() # this returns iterable
print(type(fruitItems))
itemsIter = iter(fruitItems) # this iterator returns both keyword and value
print(type(itemsIter))
for fruit, number in fruitItems:
    print(fruit, number)

def varArgs2(arg1, *args1, arg2, arg3):
    return arg1, args1, arg2, arg3

print('')
firstN, tupleN, secondN, thirdN = varArgs2(1, 2, 3, 4, 5, 6, arg2=7, arg3=8)
print(firstN, tupleN, secondN, thirdN)
