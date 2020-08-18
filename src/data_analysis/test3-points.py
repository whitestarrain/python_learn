from matplotlib import pyplot as plt
import random


def test3():
    x = range(20)
    y = [random.randint(0, 20) for i in x]
    plt.figure(figsize=(16, 8))
    plt.grid()
    plt.xticks(x)
    plt.scatter(x, y, color="red",label="test3")
    plt.scatter(x,[random.randint(10,20) for i in x],label="test3+")
    plt.legend()
    plt.show()
    pass


if __name__ == "__main__":
    test3()
