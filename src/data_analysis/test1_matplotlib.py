from matplotlib import pyplot as plt

plt.figure(figsize=(16, 8))
x = range(0, 24, 2)
y = [15, 13, 16, 13, 11, 1, 16, 12, 16, 19, 4, 7]
# 点为x与y交线

plt.plot(x, y,label="test")
plt.xticks(range(0, 24))
plt.grid()
plt.legend()
plt.show()
