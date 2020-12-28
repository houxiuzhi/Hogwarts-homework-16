from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from appauto.page.basepage import BasePage


class AddMemberPage(BasePage):
    def add_member(self):
        self.find_click(By.XPATH, '//*[@text="Add Manually"]')
        # self.driver.find_element(By.XPATH,'//*[@text="Add Manually"]').click()
        self.find_send_key(By.XPATH, '//*[contains(@text,"Name")]/..//*[@text="Required"]', "张三1")
        # self.driver.find_element(By.XPATH,'//*[contains(@text,"Name")]/..//*[@text="Required"]').send_keys("张三1")
        self.find_click(MobileBy.XPATH, '//*[contains(@text,"Gender")]/..//*[@text="Male"]')
        # self.driver.find_element(MobileBy.XPATH,'//*[contains(@text,"Gender")]/..//*[@text="Male"]').click()
        locator = (MobileBy.XPATH, '//*[@text="Female"]')
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()
        self.find_send_key(MobileBy.XPATH,
                           '//*[contains(@text,"Mobile")]/..//*[@text="Mobile No."]', "18900009999")
        # self.driver.find_element(MobileBy.XPATH,
        #                          '//*[contains(@text,"Mobile")]/..//*[@text="Mobile No."]').send_keys("18900009999")
        self.find_click(MobileBy.XPATH, '//*[@text="Save"]')
        # self.driver.find_element(MobileBy.XPATH,'//*[@text="Save"]').click()
        # return ContactPage(self.driver)
