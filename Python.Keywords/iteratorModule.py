# this script surveys concept of iterator

# an iterable is an object which contains __iter__() method. When __iter__()
# is invoked, the iterable returns an iterator.
# an iterator is an iterable which implements the iterator protocol, which contains 
# __next__() method. Simple implementations of both are shown below

class iterator():
    def __init__(self, data):
        self.__data__ = data
        self.__base__ = -1
        self.__sentinel__ = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        self.__base__ += 1
        if self.__base__ == self.__sentinel__:
            raise StopIteration
        else:
            return self.__data__[self.__base__]

class iterable():
    def __init__(self, data):
        self.__data__ = data

    def __iter__(self):
        return iterator(self.__data__)