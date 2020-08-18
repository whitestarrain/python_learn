from matplotlib import pyplot as plt
import random

def test5():
    data = [random.randint(0,80) for i in range(100)]
    plt.figure(figsize=(16,8))
    plt.grid()
    plt.hist(data,20)
    plt.xticks(range(80)[::2])
    plt.show()

if __name__ =="__main__":
    test5()