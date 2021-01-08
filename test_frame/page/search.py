from selenium.webdriver.common.by import By

from test_frame.basepage import BasePage


class SearchPage(BasePage):

    def search(self):
        self.find_click(By.XPATH,'//*[@resource-id = "com.xueqiu.android:id/action_search"]')
        self.find_send_key(By.XPATH,'//*[@resource-id = "com.xueqiu.android:id/search_input_text"]','ali')


