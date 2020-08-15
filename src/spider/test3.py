import requests


class TiebaSpider:
    url_temp = "https://tieba.baidu.com/f?kw={}&ie=utf-8&pn={}"

    def __init__(self, name, page_num):
        self.name = name
        self.page_num = page_num

    def get_url_list(self):
        # url_list = list()
        # for i in range(self.page_num):
        #     url_list.append(self.__class__.url_temp.format(self.name, i))
        # return url_list

        # 使用推导式替代，推荐使用
        return [self.__class__.url_temp.format(self.name, i) for i in range(self.page_num)]

    def parse_url(self, url):
        rp = requests.get(url)
        return rp.content.decode("utf-8")

    def run(self):
        list = self.get_url_list()
        for url in list:
            html_con = self.parse_url(url)
            file_path = "./test/spider/tieba/{}-{}.html".format(
                self.name, list.index(url)+1)
            with open(file_path, "w", encoding="utf-8") as file:
                # 注意：打开文件是要指定编码，否则默认使用ascii
                file.write(html_con)
                print("写入--"+file_path)


if __name__ == "__main__":
    s = TiebaSpider("lol", 2)
    s.run()
