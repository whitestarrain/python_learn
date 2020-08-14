import socket
def main();
    tcp_socket = soket.socket(socket.AF_INET,socket.SOCK_STREAM)

    addr = ("127.0.0.1",10023)

    tcp_socket.connect(addr)
    
    tcp_socket.send("testdata".encode("utf-8"))

    revedata = tcp_socket.recv(1023)

    print(revedata.decode("utf-8")


if __name__ = "__main__" :
    main()
