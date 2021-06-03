# this script surveys nonlocal and global keywords

# to study the concept of local and nonlocal variables
def outside():
    msg = "Outside!"
    def inside():
        msg = "Inside!"
        print(msg)
    inside()
    print(msg)

outside()

print()
def outside2():
    msg = "Outside!"
    def inside():
        nonlocal msg
        msg = "Inside!"
        print(msg)
    inside()
    print(msg)

outside2()

print()
x = "Outside!"
def outside3():
    global x
    print(x)
    
outside3()

print()
f = lambda x: x*x*x
print(f(2))