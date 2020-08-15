def create_test(n):
    """ 生成器示例
    
    
    """
    i = 0
    while i < n:
        yield i
        i += 1


def main():
    # 生成器对象
    gen = create_test(10)
    for i in gen:
        print(i)


if __name__ == "__main__":
    main()
