# 自动执行fixture
import pytest

'''
如果每条用例都都需要初始化数据，则在装饰器里加一个autouse=’true'的参数，应用到所有测试方法中，只是没有办法返回值给测试用例
'''


@pytest.fixture(autouse="true")
def myfixture():
    print("初始化操作")


class TestAutoUse:
    def test_one(self):
        print("执行testone")
        # 断言
        assert 1 + 2 == 3

    def test_two(self):
        print("run testtwo")
        assert 1 == 1

    def test_three(self):
        print("run testthree")
        assert 1 + 1 == 2


'''
fixture传递参数，一般我们在测试过程中会将测试用到的数据以参数的形式传入到测试用例中，并为每条测试数据生成一个测试结果数据。
可以用fixture的参数化功能pytest.fixture(params=[1,2,3,4])，数据是个列表。
传入的数据需要用一个固定的request参数名来接收
'''


@pytest.fixture(params=[1, 2, 3, 4])
def data(request):
    return request.param


def test_not_5(data):
    print(f"测试数据，{data}")
    assert data != 5
