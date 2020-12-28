from selenium.webdriver.common.by import By

from appauto.page.basepage import BasePage


class MainPage(BasePage):

    def goto_contact_page(self):
        from appauto.page.contactpage import ContactPage
        self.find_click(By.XPATH, "//*[@class='android.widget.TextView' and @text='Contacts']")
        # self.driver.find_element(By.XPATH,"//*[@class='android.widget.TextView' and @text='Contacts']").click()
        return ContactPage(self.driver)
