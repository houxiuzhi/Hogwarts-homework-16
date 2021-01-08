import pytest

'''
可以用fixture来装饰一个方法来完成测试之前的初始化，也可以返回数据给测试函数
'''


# 里面不写参数，默认scope=“function”
@pytest.fixture()
def login():
    print("this is a login function")
    return ('henna', '123')


@pytest.fixture()
def operate():
    print("登录后的操作")


def test_case1(login, operate):
    print(login)
    print("case1需要登录")


def test_case2():
    print("case2不需要登录")


def test_case3(login):
    print(login)
    print("case3需要登录")
