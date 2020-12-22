import yaml
from selenium import webdriver
from selenium.webdriver.android.webdriver import WebDriver


class BasePage:

    def __init__(self, base_driver=None):
        # 注解，不是赋值操作。用作ide的类型提示
        base_driver: WebDriver
        if base_driver is None:
            self.driver = webdriver.Chrome()
            self.__cookie_login()
        else:
            self.driver = base_driver
        self.driver.implicitly_wait(3)

    def __get_cookie(self):
        opt = webdriver.ChromeOptions()
        opt.debugger_address = "127.0.0.1:9222"
        driver = webdriver.Chrome(opt)
        driver.get("https://work.weixin.qq.com/wework_admin/frame")
        cookies = driver.get_cookies()
        with open("../testcases/cookiedata.yml", "w", encoding="utf-8") as f:
            yaml.dump(cookies, f)

    def __cookie_login(self):
        self.driver.get("https://work.weixin.qq.com/")
        # 点击企业登录
        self.driver.find_element_by_xpath('//*[@id="indexTop"]/div[2]/aside/a[1]').click()
        # self.driver.get("https://work.weixin.qq.com/")
        with open("../testcases/cookiedata.yml", encoding="utf-8") as f:
            ymlcookie = yaml.safe_load(f)
            for cookie in ymlcookie:
                self.driver.add_cookie(cookie)
        # 拿cookie进首页
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")

    def find(self, by, value=None):
        if value is None:
            # 如果传入的是一个元祖，用元祖前面加*对元祖进行解包操作
            return self.driver.find_element(*by)
        else:
            # 如果是正常的传参就正常使用
            return self.driver.find_element(by=by, value=value)

    def finds(self, by, value=None):

        if value is None:
            # 如果传入的是一个元祖，用元祖前面加*对元祖进行解包操作
            return self.driver.find_elements(*by)
        else:
            # 如果是正常的传参就正常使用
            return self.driver.find_elements(by=by, value=value)

    def quit(self):
        # 退出二次封装
        self.driver.quit()
