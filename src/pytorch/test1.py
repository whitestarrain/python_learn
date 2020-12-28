import torch
import numpy as np


def create1():
    # 没有初始化的5*3矩阵：
    x = torch.empty((5, 3))
    print(x)
    x = torch.rand(5, 3)
    print(x)
    x = torch.zeros(5, 3)
    print(x)
def create2():
    x = torch.tensor([3,3],dtype=torch.long)
    print(x)

    # 或者根据已有的tensor建立新的tensor。除非用户提供新的值，否则这些方法将重用输入张量的属性，例如dtype等：
    # 它的属性比如device和dtype是继承了调用者张量x的。
    x = x.new_ones(5, 3, dtype=torch.double)      # new_* methods take in sizes
    print(x)

    x = torch.randn_like(x, dtype=torch.float)    # 重载 dtype!
    print(x)                                      # 结果size一致

    # torch.Size本质上还是tuple，所以支持tuple的一切操作。
    print(x.size())

def yunsuan():
    # 一种运算有多种语法。在下面的示例中，我们将研究加法运算。 
    x = torch.ones(5, 3, dtype=torch.double)      # new_* methods take in sizes
    y = torch.rand(5, 3)

    # 形式1
    print(x + y)

    # 形式2
    print(torch.add(x, y))

    # 形式3
    result = torch.empty(5, 3)
    torch.add(x, y, out=result)
    print(result)

    # 形式4
    # adds x to y
    y.add_(x)
    # 任何一个in-place改变张量的操作后面都固定一个_。例如x.copy_(y)、x.t_()将更改x
    print(y)
def shape1():
    x = torch.randn(4, 4)
    y = x.view(16)
    z = x.view(-1, 8)  # the size -1 is inferred from other dimensions
    print(x.size(), y.size(), z.size())

    # 如果是仅包含一个元素的tensor，可以使用.item()来得到对应的python数值
    x = torch.randn(1)
    print(x)
    print(x.item())
def numpy1():
    # Torch张量和NumPy数组将共享它们的底层内存位置，因此当一个改变时,另外也会改变。
    a = torch.ones(5)
    print(a)
    b = a.numpy()
    print(b)
    a.add_(1)
    print(b)

    # numpy 转为 tensor
    a = np.ones(5)
    b = torch.from_numpy(a)
    np.add(a, 1, out=a) # a和b用的同一个内存区域
    print(a)
    print(b)

if __name__ == "__main__":
    numpy1()
