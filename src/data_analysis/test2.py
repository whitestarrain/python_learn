from matplotlib import pyplot as plt
import random
from matplotlib import font_manager


def test2():
    my_font = font_manager.FontProperties(fname="C:/Windows/Fonts/msyhl.ttc")
    plt.figure(figsize=(16, 8))
    x = range(0, 120)
    _x = x[::10]
    _x1 = ["{}分".format(i) for i in _x if i <= 60]
    _x2 = ["%d时%.2d分" % (i/60, i % 60) for i in _x if i > 60]
    _x = _x1+_x2
    y = [random.randint(20, 35) for i in range(120)]

    # 数字和字符串一一对应
    plt.xticks(x[::10], _x,fontproperties=my_font)
    plt.plot(x, y)
    plt.grid()
    plt.show()

if __name__=="__main__":
    test2()