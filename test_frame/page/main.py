from selenium.webdriver.common.by import By

from test_frame.basepage import BasePage
from test_frame.page.search import SearchPage


class MainPage(BasePage):

    def goto_market(self):
        self.find_click(By.XPATH,'//*[@resource-id="com.xueqiu.android:id/post_status"]')
        # self.find_click(By.XPATH,'//*[@resource-id = "com.xueqiu.android:id/iv_close"]')
        self.find_click(By.XPATH,'//*[@resource-id = "com.xueqiu.android:id/tab_name" and @text = "行情"] ')

        return SearchPage(self.driver)
