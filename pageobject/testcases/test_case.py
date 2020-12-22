from selenium import webdriver
from pageobject.page.mainpage import MainPage
import pytest


class TestAddMember:

    def setup(self):
        self.main = MainPage()

    def test_addmember_by_main(self):
        # 需要先实例化MainPage，业务逻辑：从首页点击增加成员，输入成员信息，保存，获取成员信息进行断言
        res = self.main.goto_add_memberpage().addmember().get_member_res()
        assert res.text == '13011112225'

    def test_addmember_by_contact(self):
        # 从首页点击通讯录，点添加成员，输入成员信息，保存，获取结果进行断言
        res = self.main.goto_contact().goto_addmember_page().addmember().get_member_res()
        assert res.text == '13011112225'

    def test_adddepartmemt_by_contact(self):
        # 从首页点击通讯录，点击新增机构，输入机构信息，保存，获取结果进行断言
        res = self.main.goto_contact().goto_adddepartment_page().add_department().get_department_res()
        assert "业务部" in res
