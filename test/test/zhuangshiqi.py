import time


def c_funciton(fun):
    print("装饰开始")

    def new_func(*args, **kwargs):
        start_time = time.time()
        print("-----new_function---",args)
        fun(*args, **kwargs)
        end_time = time.time()
        print("花费时间：%s" % (end_time - start_time))
    return new_func


@c_funciton
def test(a,*args,**kwargs):
    print("test执行")
    print(a)
    time.sleep(0.5)


if __name__ == "__main__":
    test(999)
