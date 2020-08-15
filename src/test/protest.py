import multiprocessing
import time
import os

def test1():
    while True:
        print("------test1-----")
        print(os.getpid())
        time.sleep(1)
def test2():
    while True:
        print("----test2----")
        print(os.getpid())
        time.sleep(1)

def __main__():
    p1 = multiprocessing.Process(target=test1)
    p2 = multiprocessing.Process(target=test2) 
    p1.start()
    p2.start()
    pass


if __name__=="__main__":
    __main__()