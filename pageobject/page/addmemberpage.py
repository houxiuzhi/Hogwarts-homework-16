from selenium.webdriver.common.by import By

from pageobject.page.basepage import BasePage
from pageobject.page.contactpage import ContactPage


class AddmemberPage(BasePage):
    _locator_username = (By.ID, 'username')
    _locator_english_name = (By.ID, 'memberAdd_english_name')
    _locator_memberAdd_acctid = (By.ID, 'memberAdd_acctid')
    _locator_memberAdd_phone = (By.ID, 'memberAdd_phone')
    _locator_baocun = (By.LINK_TEXT, "保存")

    def addmember(self):
        self.find(self._locator_username).send_keys("张三1")
        self.find(self._locator_english_name).send_keys('zhangsan1')
        self.find(self._locator_memberAdd_acctid).send_keys('00005')
        self.find(self._locator_memberAdd_phone).send_keys('13011112225')
        self.find(self._locator_baocun).click()
        return ContactPage(self.driver)
