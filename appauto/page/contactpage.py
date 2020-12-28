from selenium.webdriver.common.by import By

from appauto.page.addmemberpage import AddMemberPage
from appauto.page.basepage import BasePage


class ContactPage(BasePage):
    def goto_addmemberpage(self):
        # android_uiautomator自带的滑动只能这个写不能改
        # self.driver.find_element(By.
        #                          ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().'
        #                                               'scrollable(true).instance(0)).'
        #                                               'scrollIntoView(new UiSelector().'
        #                                               'text("Add Member").instance(0));').click()
        self.scoll_find_click("Add Member")

        '''自己封装的用self.driver.swipe方法滑动,报下面错，明明只传了2个
        TypeError: scoll_find_click() takes 2 positional arguments but 3 were given'''
        # self.scoll_find_click(By.XPATH,'//*[@text = "Add Member"]')
        return AddMemberPage(self.driver)
