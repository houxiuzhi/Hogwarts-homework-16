from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class TestRecordScript:
    def setup(self):
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
        caps['settings[waitForIdleTimeout]'] = 0
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(15)

    def teardown(self):
        self.driver.quit()

    def test_case1(self):
        self.driver.find_element(By.XPATH, "//*[@text='Workspace']").click()
        # 得改一下，改成那个滑动固定的
        self.driver.find_element(By.
                                 ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().'
                                                      'scrollable(true).instance(0)).'
                                                      'scrollIntoView(new UiSelector().'
                                                      'text("Attendance (Punch)").instance(0));').click()
        # 模拟器英文的，点击打开就挂掉，加了内存也不好使，打开后返回Punched这个不变的字符也是自己YY的
        self.driver.find_element(By.XPATH, "//*[@text='Punch']").click()
        self.driver.find_element(By.XPATH, '//*[contains(@text,"outsidePunch")]').click()
        WebDriverWait(self.driver, 10).until(lambda x: "Punched" in x.page_source())
        assert "Punched" in self.driver.page_source()
