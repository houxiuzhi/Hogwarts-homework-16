import time

from selenium.webdriver.common.by import By

from pageobject.page.basepage import BasePage


class ContactPage(BasePage):
    # _locator_goto_addmember_page = (By.CSS_SELECTOR, ".ww_operationBar .js_add_member")
    _locator_goto_addmember_page = (By.LINK_TEXT, "添加成员")
    _locator_plus = (By.CSS_SELECTOR, '.member_colLeft_top_addBtn')
    _locator_add_deparment = (By.CSS_SELECTOR, '.js_create_party')
    _locator_get_member_res = (By.XPATH, '//*[@title="13011112225"]')
    _locator_get_department_res = (By.CSS_SELECTOR, '.jstree-anchor')

    def goto_addmember_page(self):
        # 解决循环引用的问题
        from pageobject.page.addmemberpage import AddmemberPage
        self.find(self._locator_goto_addmember_page).click()
        # self.driver把这个页面的driver给AddmemberPage让操作连续起来
        return AddmemberPage(self.driver)

    def goto_adddepartment_page(self):
        # 解决循环引用的问题
        from pageobject.page.adddepartmentpage import AdddepartmentPage
        self.find(self._locator_plus).click()
        self.find(self._locator_add_deparment).click()
        return AdddepartmentPage(self.driver)

    def get_member_res(self):
        res = self.find(self._locator_get_member_res)
        return res

    def get_department_res(self):
        time.sleep(3)
        res = []
        for element in self.finds(self._locator_get_department_res):
            res.append(element)
        # '.jstree-anchor'得到的是机构的行.text才能获取到名字
        departname = [i.text for i in res]
        return departname
