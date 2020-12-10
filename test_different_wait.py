from selenium import webdriver
import allure
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


def test_search_ceshiren():
    with allure.step("打开浏览器"):
        driver = webdriver.Chrome()
        driver.get("http://www.ceshiren.com")
        driver.maximize_window()
        # 加入隐式等待
        driver.implicitly_wait(5)

    with allure.step("点击测试答疑"):
        driver.find_element_by_link_text("测试答疑").click()
        # pass
        # 加入强制等待
        time.sleep(5)
        driver.find_element_by_link_text("关于“霍格沃兹答疑区”分类").click()
        # 加入显示等待
        # WebDriverWait(driver,10).until(
        #     expected_conditions.element_to_be_clickable("关于“霍格沃兹答疑区”分类")
        # )

    with allure.step("关闭浏览器"):
        driver.quit()
    # with allure.step("保存图片"):
    #     driver.save_screenshot("./result/b.png")
    #     allure.attach.file("./result/b.png",attachment_type=allure.attachment_type.PNG)
