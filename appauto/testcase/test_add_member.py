from appauto.page.basepage import BasePage
from appauto.page.mainpage import MainPage


class TestAddMember:
    def setup(self):
        self.main = MainPage()

    def test_add_member(self):
        # 从首页点击通讯录，点击新增人员，输入人员信息，保存
        self.main.goto_contact_page().goto_addmemberpage().add_member()
