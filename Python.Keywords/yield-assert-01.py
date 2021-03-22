# this script surveys concept of generator

# generator is an iterator which is created through being defined as
# generator function or by generator expression
# assert keyword raises assertion error if the expression is false

def generator(data):
    for i in data:
        yield i

print('1) generator function is a function that contains yield keyword')
data = [1, 2, 3, 4, 5]
gen1 = generator(data)
for x in gen1:
    print(x)

print('')
print('2) generator expression is similar to list comprehension')    
gen2 = (x for x in [1, 2, 3, 4, 5, 6, 7, 8, 9] if x < 6)
for x in gen2:
    print(x)

assert 1 == 1 # does nothing
assert 1 == 2 # raises assertion error