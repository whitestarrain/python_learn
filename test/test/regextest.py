#coding=utf-8
import re

str = "<html>1111</html>"

result = re.match(r"<([a-zA-Z]+)>.*<\/\1>", str)

if result:
    print(result.group())
    


