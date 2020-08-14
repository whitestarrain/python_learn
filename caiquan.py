
import random
import test

a = int(input("请输入石头（1），剪刀（2），布（3）"))

b = random.randint(1, 3)

print("电脑出的是",b)

if ((abs(a-b) == 1 and a-b < 0)
    or a-b==2):
    print('你赢了')
elif a == b:
    print('平局')
else:
    print('你输了')

test.jiu_jiu()
