import pytest
from .calculator import Calculator


class Test_calculator:
    expect = [-2, -1, 0, 99, -1, 0, 1, 100, 0, 1, 2, 101, 99, 100, 101, 200]

    def setup_class(self):
        self.cal = Calculator()

    def teardown_class(self):
        print("结束")

    # 自动生成测试用例
    @pytest.mark.parametrize("a", [-1, 0, 1, 100])
    @pytest.mark.parametrize("b", [-1, 0, 1, 100])
    # @pytest.mark.parametrize("result",expect)
    def test_add1(self, a, b):
        result = a + b
        assert result == self.cal.add(a, b)
        '''
        想要把实际结果放到一个列表里，和预期结果进行元素的一一对比，可是预期结果里取到的永远是一个
        # add1 = []
        # add1.append(self.cal.add(a,b))
        # for i in range(16):
        #     assert add1[i]== expect[i]
        #     i=i+1
        '''

    @pytest.mark.parametrize("a,b,expect",
                             [(-1, -1, -2), (-1, 0, -1), (-1, 1, 0), (-1, 100, 99), (0, -1, -1), (0, 0, 0),
                              (1.2, 1.2, 2.4), (100, 100, 200)])
    def test_add(self, a, b, expect):
        assert expect == self.cal.add(a, b)

    @pytest.mark.parametrize("a,b,expect",
                             [(-1, -1, 0), (-1, 1, -2), (-1, 0, -1), (-1, 100, -101), (0, -1, 1), (0, 0, 0),
                              (2.4, 1.2, 1.2), (100, 100, 0)])
    def test_sub(self, a, b, expect):
        assert expect == self.cal.sub(a, b)

    @pytest.mark.parametrize("a,b,expect",
                             [(-1, -1, 1), (-1, 0, 0), (-1, 1, -1), (-1, 100, -100), (0, -1, 0), (0, 0, 0),
                              (1.2, 1.2, 1.44), (0, 100, 0)])
    def test_mul(self, a, b, expect):
        assert expect == self.cal.mul(a, b)

    @pytest.mark.parametrize("a,b,expect",
                             [(-1, -1, 1), (-1, 1, -1), (0, -1, 0), (100, -1, -100), (100, 100, 1), (1.5, 0.5, 3),
                              (100, 100, 1)])
    def test_div(self, a, b, expect):
        assert expect == self.cal.div(a, b)
