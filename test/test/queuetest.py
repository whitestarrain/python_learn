import time
from threading import Thread
from queue import Queue

q = Queue(3)


def test1():
    global q
    i = 1
    while True:
        q.put(i)
        print("put", i)
        i += 1
        time.sleep(1)
    pass


def test2():
    global q
    while True:
        temp = q.get()
        print("get", temp)
        time.sleep(0.5)
    pass


def main():
    """ 可以换为Process看看，会发现无法共享全局数据，要把数据作为参数传入(args=q)，或者通过socket通信
    """
    p1 = Thread(target=test1)
    p2 = Thread(target=test2)
    p1.start()
    p2.start()
    pass


if __name__ == "__main__":
    main()
