import requests
import requests

headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 "}

response = requests.get("http://www.baidu.com",headers=headers)

response.encoding= "utf-8"

print(response.content.decode("utf-8"))

""" i = requests.get("http://p.xiaomingming.org/FileUpload/201762221155776184.jpg")

with open("a.jpg","wb") as image:
    image.write(i.content)
    pass """

