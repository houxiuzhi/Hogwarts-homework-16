from appium import webdriver
from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self, base_driver: WebDriver = None):
        if base_driver is None:
            caps = {}
            caps["platformName"] = "Android"
            caps["deviceName"] = "192.168.253.103:5555"
            # adb logcat |grep -i 'activitymanager'
            # 获取app包名、activity（关注START标签）
            caps["appPackage"] = "com.tencent.wework"
            caps["appActivity"] = ".launch.LaunchSplashActivity"
            caps["noReset"] = "true"
            # 跳过 uiautomator2 server的安装
            caps['skipServerInstallation'] = 'true'
            # 跳过设备初始化
            caps['skipDeviceInitialization'] = 'true'
            # 启动之前不停止app
            caps['dontStopAppOnReset'] = 'true'
            caps['unicodeKeyBoard'] = 'true'
            caps['resetKeyBoard'] = 'true'
            caps['settings[waitForIdleTimeout]'] = 0
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        else:
            self.driver = base_driver
        self.driver.implicitly_wait(15)

    def find_click(self, by, locator=None):
        self.driver.find_element(by=by, value=locator).click()

    def find_send_key(self, by, locator, key):
        self.driver.find_element(by=by, value=locator).send_keys(key)

    def scoll_find_click(self, text):
        self.driver.find_element(By.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().'
                                                         'scrollable(true).instance(0)).'
                                                         'scrollIntoView(new UiSelector().'
                                                         f'text("{text}").instance(0));').click()
        # 字符串前面加f,用{}扩起就变成了变量，f就是format

    def swip_find(self, by, locator):
        self.driver.implicitly_wait(1)
        # 找到所有元素
        eles = self.driver.find_elements(by, locator)
        # 不停滑动直到找到为止
        while len(eles) == 0:
            # 滑动
            self.driver.swipe(0, 800, 0, 400)
            self.driver.find_elements(by, locator)
        self.driver.implicitly_wait(5)
        return eles[0]

    def find_by_swipe_click(self, by, locator):
        self.swip_find(by, locator).click()
