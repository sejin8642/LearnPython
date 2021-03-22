# this script surveys concept of container

# Containers are any object that holds an arbitrary number of other objects. 
# Generally, containers provide a way to access the contained objects 
# and to iterate over them.

listContainer1 = [1, 2, 3, 4] # list comprehension to create a list contrainer
listContainer2 = [3, 4, 5, 6]
setContainer1 = set(listContainer1) # set comprehension to create a set container from the list
setContainer2 = set(listContainer2)
setUnion = setContainer1 | setContainer2 
print()
print(setUnion)

print()
tupleContainer = (1, 'red', 2) # tuple comprehension to create a tuple contrainer
print(tupleContainer)

print()
dictContainer = {1:'first', 2:'second'} # dict comprehension to create a dict contrainer
print(dictContainer)