import time

import pytest
import yaml
from selenium import webdriver


class TestQiyeweixin():
    @pytest.fixture()
    def fixture(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        yield
        self.driver.quit()

    @pytest.mark.skip
    def test_clicklogin(self, fixture):
        self.driver.get("https://work.weixin.qq.com/")
        self.driver.maximize_window()
        self.driver.find_element_by_css_selector('.index_top_operation_loginBtn').click()
        time.sleep(2)

    @pytest.mark.skip
    def test_remotechrome(self):
        '''
        复用浏览器,先在gitbash执行chrome --remote-debugging-port=9222
        打开浏览器，下面get百度时就不会在重新打开一个新页面了
        '''
        opt = webdriver.ChromeOptions()
        opt.debugger_address = "127.0.0.1:9222"
        driver = webdriver.Chrome(options=opt)
        driver.implicitly_wait(5)
        driver.get("https://work.weixin.qq.com/wework_admin/frame")
        driver.find_element_by_id('menu_contacts').click()
        print(driver.get_cookies())

    @pytest.mark.skip
    def test_cookie_login(self, fixture):
        # driver = webdriver.Chrome()
        # driver.implicitly_wait(5)
        self.driver.get("https://work.weixin.qq.com/")
        self.driver.maximize_window()
        self.driver.find_element_by_css_selector('.index_top_operation_loginBtn').click()
        cookies = [
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688853804057409'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970325138203272'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688853804057409'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': 'RwxaN52Rm1Ddd-TfsTe0j3fSFp2FCSmdlOo_HlzKJYCWLTlJeekf0S9R4Fv5QDMz'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a4768103'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': 'NVeYLxkCp4ayiiKr_j0nfxysiZv1qET3fTDh_7OTN0EyOJQL1Fy8pDJtlLof1n9jj5IEcLU-ZGNJo03FpViGv8CS0dLrB0tTJCqYdo3-yZaUp5lN393-U6opuDPk3qf2Ny_TmanYdL-8q-6PyKPBil383z4PBeOUC2RHXmBn0NllTg6XhLxg0wE7WZp7vxYdbZb4Rf_jxSNfyadjRmS0lRLZVL40M_f1j36f9dFWd5XZWsfVGh21X5YpFXi8hAn4UXyJbTKIeXatUYir3HiVeg'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d',
             'path': '/', 'secure': False, 'value': '1608261020'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
             'value': '0403819'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1608286735, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': False, 'value': 'jrpbm3'},
            {'domain': '.qq.com', 'expiry': 1608347677, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
             'value': 'GA1.2.2016375470.1608255214'},
            {'domain': '.qq.com', 'expiry': 1609986185, 'httpOnly': False, 'name': 'ptui_loginuin', 'path': '/',
             'secure': False, 'value': '625470150'},
            {'domain': '.qq.com', 'expiry': 1671333277, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
             'value': 'GA1.2.1628752043.1608255214'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1629358622, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': False, 'value': '0'},
            {'domain': '.qq.com', 'expiry': 2147483649, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False,
             'value': 'IV4dvoSCQe'},
            {'domain': '.qq.com', 'expiry': 2147483651, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False,
             'value': 'd1109a39cf19810f1029844e1229e9d442aa8d3ab84de1ae900a58abf1f2d69b'},
            {'domain': '.qq.com', 'expiry': 1910229821, 'httpOnly': False, 'name': 'pac_uid', 'path': '/',
             'secure': False, 'value': '0_5f0fc839e7d0b'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1610853600, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'}, {'domain': '.work.weixin.qq.com', 'expiry': 1639797019, 'httpOnly': False,
                             'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False,
                             'value': '1608255202,1608260807'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
             'value': 'direct'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
             'secure': False, 'value': '4307012932'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/',
             'secure': False, 'value': '7869305856'}]
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.find_element_by_id('menu_contacts').click()

    def test_get_cookies_toyml(self):
        opt = webdriver.ChromeOptions()
        opt.debugger_address = "127.0.0.1:9222"
        driver = webdriver.Chrome(options=opt)
        driver.implicitly_wait(5)
        driver.get("https://work.weixin.qq.com/wework_admin/frame")
        cookies = driver.get_cookies()
        print(cookies)
        with open("cookiedata.yml", "w", encoding="UTF-8") as f:
            yaml.dump(cookies, f)

    # 使用序列化cookie的方式登录
    def test_loginbycookies(self, fixture):
        self.driver.get("https://work.weixin.qq.com/")
        self.driver.maximize_window()
        self.driver.find_element_by_css_selector('.index_top_operation_loginBtn').click()
        with open("cookiedata.yml", encoding="UTF-8") as f:
            cookies = yaml.safe_load(f)
            for cookie in cookies:
                self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.find_element_by_id('menu_contacts').click()
