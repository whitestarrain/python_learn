import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("", 10022))
while True:
    data = s.recvfrom(1024)
    print(data[0].decode("utf-8"))
    if data[0].decode("utf-8") == "exit":
        break
s.close()
