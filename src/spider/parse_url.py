import requests
from retrying import retry


@retry(stop_max_attempt_number=5)  # 通过装饰器会遇到错误后重新执行，尝试五次
def _parse_url(url,method, headers, data, cookies, timeout):
    print("*"*20)
    if method=="get":
        resopnse = requests.get(url, headers=headers,
                                data=data, cookies=cookies, timeout=timeout)
    elif method == "post":
        resopnse = requests.post(url, headers=headers,
                                data=data, cookies=cookies, timeout=timeout)
    assert resopnse.status_code == 200  # 状态码不为200就报错重试
    return resopnse.content.decode("utf-8")


def parse_url(url,method="get", headers=None, data=None, cookies=None, timeout=10):
    try:
        # 重试多少次后依旧不行,就会抛出异常，在此处接住
        html_str = _parse_url(url,method, headers, data, cookies,timeout)
    except:
        html_str = None
    return html_str


if __name__ == "__main__":
    data = parse_url("https://www.baidu.com")
    print(data)
    pass
