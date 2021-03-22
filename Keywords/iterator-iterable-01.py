# this script surveys concept of iterator

from iteratorModule import *

print('1) iterator always returns itself when __iter__ is invoked')
data = [1, 2, 3, 4, 5]
iterator01 = iterator(data)
iterator02 = iter(iterator01)

while True:
    try:
        print(next(iterator01))
    except StopIteration:
        break

try: # try clause will not be executed because of the previous for-loop
    for num in iterator02:
        print(num)
except IndexError:
    print('iterable values exhausted already')

print(iterator01 is iterator02)

print('')
print('2) iterable returns a new iterator when __iter__ is invoked')
iterable01 = iterable([1, 2, 4, 5])
iterable02 = iter(iterable01)
iterable03 = iter(iterable01)

print(iterable02 is iterable03)
print(next(iterable01))