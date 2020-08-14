import socket


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(("", 10022))
    while True:
        data = input("请输入数据")
        s.sendto(data.encode("utf-8"), ("127.0.0.1", 10023))
        recvdata = s.recvfrom(1024)
        print(recvdata[0].decode("utf-8"))
        print("test")


def test():
    print("test data")

# test


if __name__ == "__main__":
    main()
    pass
