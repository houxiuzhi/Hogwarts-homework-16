import yaml
from selenium.webdriver.common.by import By
from pageobject.page.addmemberpage import AddmemberPage
from pageobject.page.basepage import BasePage
from pageobject.page.contactpage import ContactPage
from selenium import webdriver


class MainPage(BasePage):
    # 设成私有变量，不用暴露
    _locator_goto_contact = (By.ID, "menu_contacts")
    _locator_goto_add_memberpage = (By.CSS_SELECTOR, '[node-type="addmember"]')

    # def setup(self):
    #     self.driver = webdriver.Chrome()
    #     self.driver.implicitly_wait(5)
    #
    def goto_contact(self):
        #     self.driver.get("https://work.weixin.qq.com/")
        #     with open("cookiedata.yml",encoding="utf-8") as f:
        #         ymlcookie = yaml.safe_load(f)
        #         for cookie in ymlcookie:
        #             self.driver.add_cookie(cookie)
        #     self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.find(self._locator_goto_contact).click()
        return ContactPage(self.driver)

    def goto_add_memberpage(self):
        # self.driver.get("https://work.weixin.qq.com/")
        # with open("cookiedata.yml",encoding="utf-8") as f:
        #     ymlcookie = yaml.safe_load(f)
        #     for cookie in ymlcookie:
        #         self.driver.add_cookie(cookie)
        self.find(self._locator_goto_add_memberpage).click()
        return AddmemberPage(self.driver)
