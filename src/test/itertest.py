from typing import Iterable, Iterator


class classmate(object):
    def __init__(self):
        self.classmates = list()
        self.iterator = None

    def add(self, name):
        self.classmates.append(name)

    def __iter__(self):
        if self.iterator == None:
            self.iterator = classmate_iterator(self)
            return self.iterator
        else:
            return self.iterator


class classmate_iterator(object):
    """ 这个也可以写到上面类中，为了原理清晰些分开写了，一个对象可以迭代，不一定是迭代器，但迭代器一定可迭代(因为要实现__iter__方法) """

    def __init__(self, obj):
        self.obj = obj
        self.current = 0

    def __iter__(self):
        pass

    def __next__(self):
        if self.current < len(self.obj.classmates):
            r = self.obj.classmates[self.current]
            self.current += 1
        else:
            raise StopIteration
        return r


def main():
    classmate_ = classmate()
    classmate_.add("1111")
    classmate_.add("1211")
    classmate_.add("1311")
    classmate_.add("1211")
    for i in classmate_:
        print(i)


if __name__ == "__main__":
    main()
