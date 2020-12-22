from selenium.webdriver.common.by import By
from pageobject.page.basepage import BasePage


class AdddepartmentPage(BasePage):

    def add_department(self):
        from pageobject.page.contactpage import ContactPage
        self.find(By.XPATH, '//*[@id="__dialog__MNDialog__"]/div/div[2]/div/form/div[1]/input').send_keys("业务部")
        # 点击机构那个下拉框
        self.find(By.XPATH, "//*[@id='__dialog__MNDialog__']/div/div[2]/div/form/div[3]/a").click()
        '''选择下拉框的类容，这里直接用id定位不到，先定位到下拉框所在的大弹出框，再去通过ID定位到想选的机构,组合定位'''
        self.find(By.CSS_SELECTOR, ".qui_dialog_body.ww_dialog_body [id='1688853808016581_anchor']").click()
        self.find(By.XPATH, '//*[@id="__dialog__MNDialog__"]/div/div[3]/a[1]').click()
        return ContactPage(self.driver)
