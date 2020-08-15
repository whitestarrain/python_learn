import socket


def main():
    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ss.bind(("", 50020))

    # 简单可以简单理解成同一时刻并发数，其实并不是
    ss.listen(128)

    client_socket, addr = ss.accept()
    print(client_socket)
    print(addr)
    recevata = client_socket.recv(1024)
    print(recevata)
    client_socket.send("data".encode("utf-8"))
    pass


#  test test test
if __name__ == "__main__":
    main()
