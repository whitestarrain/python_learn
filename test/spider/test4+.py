# 前面直接用的浏览器上的cookie和token。这里要自己生成token和cookie。否则只能暂时用
# 问题： cookie只有 BAIDUID是不行的，其他cookie的生成是个问题
# token会和cookie一起进行验证
# 现在已经查到大多数cookie需要重新访问其他资源获得
# 之后再进行完成

import requests
import re
import json
import execjs


class BaiduTranslation(object):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
    }
    html_response = requests.get("https://fanyi.baidu.com/",headers=headers)
    # token = re.search(r"token: '(\w+)'", requests.get("https://fanyi.baidu.com/",
    #                                                     headers=headers1).content.decode("utf-8")).group(1)

    url = "https://fanyi.baidu.com/v2transapi?from=zh&to=en"

    def get_sign(self, data):
        jsdata = ""
        with open("./test/spider/sign.js") as jsfile:
            jsdata = jsfile.read()
        sign = execjs.compile(jsdata).call("e", data)
        return sign

    # def get_token(self):
    #     headers = {
    #         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 "}
    #     response = requests.get("https://fanyi.baidu.com/", headers=headers)
    #     html = response.content.decode("utf-8")
    #     regex = r"token: '(\w+)'"
    #     ret = re.search(regex, html)
    #     return ret.group(1)

    def translate(self, data):
        token = re.search(r"token: '(\w+)'",self.__class__.html_response.content.decode("utf-8")).group(1)
        data = {
            "from": "zh",
            "to": "en",
            "query": data,
            "transtype": "translang",
            "simple_means_flag": 3,
            "sign": self.get_sign(data),
            "token":token,
            "domain": "common"
        }
        response = requests.post(
            self.__class__.url, data=data, headers=self.__class__.headers,cookies=self.__class__.html_response.cookies)

        result = json.loads(response.content.decode("utf-8"))
        return result["trans_result"]["data"][0]["dst"]


if __name__ == "__main__":
    b = BaiduTranslation()
    print(b.translate("数据测试"))
