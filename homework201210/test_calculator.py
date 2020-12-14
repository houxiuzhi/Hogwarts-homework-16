import pytest
from .calculator import Calculator
import yaml


class Test_calculator:

    @pytest.fixture()
    def fixture(self):
        self.cal = Calculator()
        yield
        print("结束")

    '''
    下面是setup_teardown
    '''

    # def setup_class(self):
    #     self.cal = Calculator()
    #
    # def teardown_class(self):
    #     print("结束")

    @pytest.mark.smoke
    @pytest.mark.sit
    @pytest.mark.parametrize("a,b,expect", yaml.safe_load(open("./data.yml"))["adddata"])
    def test_add(self, a, b, expect, fixture):
        assert expect == self.cal.add(a, b)

    @pytest.mark.sit
    @pytest.mark.parametrize("a,b,expect", yaml.safe_load(open("./data.yml"))["subdata"])
    def test_sub(self, a, b, expect, fixture):
        assert expect == self.cal.sub(a, b)

    @pytest.mark.uat
    @pytest.mark.parametrize("a,b,expect", yaml.safe_load(open("./data.yml"))["muldata"])
    def test_mul(self, a, b, expect, fixture):
        assert expect == self.cal.mul(a, b)

    @pytest.mark.smoke
    @pytest.mark.parametrize("a,b,expect", yaml.safe_load(open("./data.yml"))["divdata"],
                             ids=yaml.safe_load(open("./data.yml"))["myids"])
    def test_div(self, a, b, expect, fixture, fixtureconftest):
        assert expect == self.cal.div(a, b)

    # pytest.ini是否生效检查
    def check_ini(self):
        print("just for checking pytest.ini")
