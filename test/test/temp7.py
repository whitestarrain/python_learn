import time
import threading



def function():
    print("执行function")
    time.sleep(3)


def main():
    i = 1
    # 创建5个线程，在1秒后同时i执行
    for i in range(5):
        t = threading.Thread(target=function)
        t.start()
        print(t.getName())
        e = threading.enumerate()
        print(e)
        # test tes22 1313

if __name__ == "__main__":
    main()

    