import socket

url = "i.ibb.co"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((url,80))

send_data = """GET https://i.ibb.co/80LV7xT/dao.png HTTP/1.1
Host: i.ibb.co
Connection: keep-alive
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9,ja;q=0.8


"""

print(send_data)

s.send(send_data.encode("utf-8"))

html = ""

data = s.recv(65535)
print(data.decode("utf-8"))

print(html)

s.close()
