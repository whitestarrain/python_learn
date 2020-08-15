from selenium import webdriver
import time

def main():
    try:
        driver = webdriver.PhantomJS(r"D:\learn\phantomjs-2.1.1-windows\bin\phantomjs.exe")
        driver.get("https://www.baidu.com")
        cookies = driver.get_cookies()
        print({i["name"]:i["value"] for i in cookies})
        time.sleep(0.5)
    except Exception as identifier:
        print(identifier)
    finally:
        driver.quit()


if __name__ =="__main__":
    main()