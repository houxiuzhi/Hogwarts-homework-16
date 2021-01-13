import yaml
from appium import webdriver
from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from test_frame.backlist import black_wrapper



class BasePage:
    Target = 'target'
    Action = 'action'
    Content = 'content'
    Find_and_click = 'find_and_click'
    Find_and_send_keys = 'find_and_send_keys'

    def __init__(self, base_driver: WebDriver = None):
        if base_driver is None:
            caps = {}
            caps["platformName"] = "Android"
            caps["deviceName"] = "192.168.253.103:5555"
            # adb logcat |grep -i 'activitymanager'
            # 获取app包名、activity（关注START标签）
            caps["appPackage"] = "com.xueqiu.android"
            caps["appActivity"] = ".view.WelcomeActivityAlias"
            caps["noReset"] = "true"
            caps["adbExecTimeout"] = 20000
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
        self.blacklist = [(By.XPATH, '//*[@resource-id = "com.xueqiu.android:id/iv_close"]')]

    @black_wrapper
    def find_click(self, by, locator=None):
            self.driver.find_element(by=by, value=locator).click()


    def finds(self,by,locator):
        #要记得返回啊，不返回别的地方调的时候就会没有none
        return self.driver.find_elements(by,locator)

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

    def get_toast_text(self):
        result = self.find(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        return result

    def get_data(self,ymlfile):
        with open(ymlfile,encoding='utf-8') as f:
            yamldata = yaml.safe_load(f)
            for step in yamldata:
                xpath_target = step.get(self.Target)
                action = step.get(self.Action)
                if action == self.Find_and_click:
                    self.find_click(By.XPATH,xpath_target)
                elif action == self.Find_and_send_keys:
                    content = step.get(self.Content)
                    self.find_send_key(By.XPATH,xpath_target,content)



