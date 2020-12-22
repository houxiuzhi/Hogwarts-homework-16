import time
import pytest
import yaml
from selenium import webdriver


class TestAutoLoginQYWX():

    @pytest.fixture()
    def fixture(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        yield
        self.driver.quit()

    def test_get_cookies(self):
        opt = webdriver.ChromeOptions()
        opt.debugger_address = "127.0.0.1:9222"
        # driver为复用的那个
        driver = webdriver.Chrome(options=opt)
        # 已经登录进去的页面才有cookie
        driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # 获取cookie
        cookies = driver.get_cookies()
        # 把cookie放到yml文件里
        with open("cookiedata.yml", "w", encoding="utf-8") as f:
            yaml.dump(cookies, f)

    def test_login_by_ymlcookie(self, fixture):
        # 直接打开新浏览器
        self.driver.get("https://work.weixin.qq.com/")
        # 点击企业登录
        self.driver.find_element_by_xpath('//*[@id="indexTop"]/div[2]/aside/a[1]').click()
        # 从yml文件中去cookie
        with open("cookiedata.yml", encoding="utf-8") as f:
            ymlcookie = yaml.safe_load(f)
            for cookie in ymlcookie:
                self.driver.add_cookie(cookie)
        # 拿cookie进首页
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # 点击通讯录
        self.driver.find_element_by_id("menu_contacts").click()
        # self.driver.find_element_by_xpath("//*[@id="js_contacts47"]/div/div[2]/div/div[2]/div[3]/div[1]/a[1]").click()
        self.driver.find_element_by_link_text("添加成员").click()
        # 添加成员信息
        self.driver.find_element_by_id('username').send_keys("张三1")
        self.driver.find_element_by_id('memberAdd_english_name').send_keys('zhangsan1')
        self.driver.find_element_by_id('memberAdd_acctid').send_keys('00005')
        self.driver.find_element_by_id('memberAdd_phone').send_keys('13011112225')
        self.driver.find_element_by_link_text("保存").click()
        time.sleep(2)

        # 去找刚刚加的人的手机号
        iphone = self.driver.find_element_by_xpath('//*[@title="13011112225"]')
        # 断言如果匹配到了iPhone就说明添加成功了
        if iphone.text == '13011112225':
            pass
        else:
            raise Exception