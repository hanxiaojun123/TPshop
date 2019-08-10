from selenium.webdriver.support.wait import WebDriverWait
from appium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction
import time


def open_mobile():
    """打开手机"""
    desired_caps = {}
    # 2.1.启动的系统名称 Android
    desired_caps['platformName'] = "Android"
    # 2.2.启动的设备名称 5.1.1
    desired_caps['platformVersion'] = "5.1.1"
    # 2.3.启动的设备名称 device
    desired_caps['deviceName'] = "127.0.0.1:21503"
    # 2.4.启动的APP包名 APPpackage
    desired_caps['appPackage'] = "com.tpshop.malls"
    # 2.5.启动的APP启动名 appactivity
    desired_caps['appActivity'] = ".SPMainActivity"
    # 添加一个新参数
    desired_caps["automationName"] = "Uiautomator2"
    # 2.6启动unicode输入法,设置为True可以输入中文，默认为false
    desired_caps['unicodeKeyboard'] = True
    # 2.7在设定了UnicodeKeyboard 关键字运行Unicode测试结束后，将键盘重置为其原始状态
    # 如果单独使用，将会被忽略，默认值 false
    desired_caps['resetKeyboard'] = True
    # 2.8 不重置应用
    desired_caps["noReset"] = True
    # 3.启动手机
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    return driver

class Base:

    def __init__(self, driver):
        self.driver = driver
    def find_element(self,locator,timeout = 10):
        """定位一个元素"""
        try:
            element = WebDriverWait(self.driver,timeout).until(EC.presence_of_element_located(locator))
        except:
            return False
        else:
            return element

    def find_elements(self,locator,timeout = 10):
        """
        定位一组元素
        :param locator:
        :param timeout:
        :return:
        """
        elements = WebDriverWait(self.driver,timeout).until(EC.presence_of_all_elements_located(locator))
        return elements

    def click(self, locator, timeout=10):
        """点击元素"""
        try:
            element = self.find_element(locator,timeout)
            element.click()
        except:
            return False

    def send_keys(self, locator, text, timeout=10):
        """输入"""
        try:
            element = self.find_element(locator)
            element.clear()
            element.send_keys(text)
        except:
            return False
        else:
            return element

    def close(self):
        """关闭手机"""
        self.driver.quit()

    def is_text_in_element(self, locator, text, timeout=10):
        """判断文本是否存在元素中,存在返回True,不存在返回False"""
        try:
            result = WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element(locator, text))
            return result
        except:
            return False

    def swipe_up(self):
        """向上滑动"""
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        self.driver.swipe(width * 0.2, height * 0.8, width * 0.2, height * 0.2, duration=5000)

    def swipe_down(self):
        """向下滑动"""
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        self.driver.swipe(width * 0.2, height * 0.1, width * 0.2, height * 0.9,duration=5000)

    def swipe_left(self):
        """向左滑动"""
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        self.driver.swipe(width * 0.2, height * 0.1, width * 0.8, height * 0.1,duration=5000)

    def swipe_right(self):
        """向右滑动"""
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        self.driver.swipe(width * 0.8, height * 0.1, width *0.2, height * 0.1,duration=5000)

    # def get_toast(self, locator, timeout=10):
    #     """获取toast文本"""
    #     element = WebDriverWait(self.driver, timeout, 0.1).until(EC.presence_of_element_located(locator))
    #     return element.text
    def get_toast(self,text: str):
        """
        获取toast文本内容
        :param text:
        :return:
        """
        try:
            message_loc = ("xpath",f"//*[contains(@text,'{text}')]")
            element = WebDriverWait(self.driver,10,0.1).until(EC.presence_of_element_located(message_loc))
            message = element.text
            return message
        except TimeoutError:
            print("没有toast标签")

if __name__ == '__main__':
    driver = open_mobile()
    base = Base(driver)
    open_mobile()
    time.sleep(3)
    base.swipe_up()
    time.sleep(3)
    base.close()