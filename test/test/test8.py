import threading
import time

num = 0

mutex = threading.Lock()

def test1():
    global num
    i = 0
    while i < 100000:
        # 这样能保证最终没问题而已
        mutex.acquire()
        num += 1
        i += 1
        mutex.release()
    print(num)


def test2():
    global num
    i = 0
    while i < 100000:
        mutex.acquire()
        num += 1
        i += 1
        mutex.release()
    print(num)


def main():
    t1 = threading.Thread(target=test1)

    t2 = threading.Thread(target=test2)
    t0.start()
    t2.start()
    time.sleep(2)
    print(num)


if __name__ == "__main__":
    main()
