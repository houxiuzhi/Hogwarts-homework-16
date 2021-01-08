import pytest
from test_frame.basepage import BasePage
from test_frame.page.main import MainPage


class TestSearch:
    def setup(self):
        self.start = MainPage()

    def test_case1(self):
        self.start.goto_market().search()




