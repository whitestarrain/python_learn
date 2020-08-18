from matplotlib import pyplot as plt
import random


def test4_1():
    x = range(20)
    y = [random.randint(0, 20) for i in x]
    plt.figure(figsize=(16, 8))
    plt.grid()
    plt.xticks(x)
    plt.bar(x, y,width=0.3,label="test4")
    plt.legend()
    plt.show()
def test4_2():
    x = range(20)
    y = [random.randint(0, 20) for i in x]
    plt.figure(figsize=(16, 8))
    plt.grid()
    plt.yticks(x)
    plt.barh(y, x,height=0.3)
    plt.legend()
    plt.show()


if __name__ == "__main__":
    test4_1()
