import requests
import re
import json
import execjs


class BaiduTranslation(object):
    headers1 = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
    }
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36",
        "cookie":"REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BIDUPSID=CDCC58A804B9993641AD73AFB4E2C474; PSTM=1590133475; BAIDUID=CDCC58A804B99936A0747A06A0637C63:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; Hm_lvt_afd111fa62852d1f37001d1f980b6800=1596627072; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1596628292,1596636489,1596637207,1596671234; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1596679968; __yjsv5_shitong=1.0_7_a2219089f8c578da7105567bcdb1d3d58268_300_1596679969242_121.27.82.122_0fe8c182; yjs_js_security_passport=69e281327936de636c8fc2b0c420f56c4d0b96b7_1596679971_js"
    }
    token ="853820de666ae01e863337e02a8c7ef6"
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

    def parse_url(self, data):
        data = {
            "from": "zh",
            "to": "en",
            "query": data,
            "transtype": "translang",
            "simple_means_flag": 3,
            "sign": self.get_sign(data),
            "token": self.__class__.token,
            "domain": "common"
        }
        response = requests.post(
            self.__class__.url, data=data, headers=self.__class__.headers)
        result = json.loads(response.content.decode("utf-8"))
        return result["trans_result"]["data"][0]["dst"]


if __name__ == "__main__":
    b = BaiduTranslation()
    print(b.parse_url("测试数据"))
