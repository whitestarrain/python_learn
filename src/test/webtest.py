# coding=utf-8
import socket


def handle_client(client_socket):
    "为一个客户端进行服务"
    recv_data = client_socket.recv(1024).decode("utf-8")
    request_header_lines = recv_data.splitlines()
    for line in request_header_lines:
        print(line)

    # 组织相应 头信息(header)
    response_headers = "HTTP/1.1 200 OK\r\n"  # 200表示找到这个资源
    response_headers += "\r\n"  # 用一个空的行与body进行隔开
    # 组织 内容(body)
    response_body = "hello world"

    response = response_headers + response_body
    client_socket.send(response.encode("utf-8"))
    client_socket.close()


def main():
    "作为程序的主控制入口"

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置当服务器先close 即服务器端4次挥手之后资源能够立即释放，这样就保证了，下次运行程序时 可以立即绑定7788端口
    """ 
    对于一个socket，可以设置很多不同的选项，对于那些一般用途的服务器，一个最让人感兴趣的socket选项是SO_REUSEADDR,通常地，
    在一个服务器进程终止后，操作系统会保留几分钟它的端口，
    从而防止其他进程（甚至包括本服务器自己的另外一个实例）在超市之前使用这个端口，
    如果你设置了SO_REUSEADDR的标记为true,操作系统就会在服务器socket被关闭或者服务器进程终止后马上释放该服务器的端口。
    这样做，可以使调试程序更简单。
    level:
    SOL_SOCKET:通用套接字选项.
    IPPROTO_IP:IP选项.
    IPPROTO_TCP:TCP选项.
    """
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("", 7788))
    server_socket.listen(128)
    while True:
        client_socket, client_addr = server_socket.accept()
        handle_client(client_socket)


if __name__ == "__main__":
    main()
