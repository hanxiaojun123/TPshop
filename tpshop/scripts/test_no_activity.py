import time
from common.Base import Base,open_mobile
from page.no_activity_page import Pay_no_activity
import pytest
import allure
class TestNo:
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)  # 设置用例等级为CRITICAL
    @allure.step(title='购买没有活动的商品')
    def setup(self):
        driver = open_mobile()
        self.base = Base(driver)
        self.pay = Pay_no_activity(driver)
    def teardown(self):
        self.base.close()
    def test_01(self):
        """没有活动的商品"""
        self.base.swipe_up()  # 向上滑
        allure.attach("选择商品","点击商品")
        self.pay.click_good() #点击商品
        time.sleep(2)
        allure.attach("购买","点击立即购买")
        self.pay.click_pay()  # 点击立即购买
        time.sleep(2)
        allure.attach("确定数量和商品", "点击确定")
        self.pay.click_sure()  # 点击确定
        time.sleep(2)
        allure.attach("提交", "点击立即提交")
        self.pay.submit()#点击提交
        time.sleep(2)
        self.pay.daofu()
        time.sleep(2)
        allure.attach("显示的订单号","购买后生成的订单号")
        order_loc = ("id", "com.tpshop.malls:id/pay_trade_no_tv")  # 生成订单号
        order = self.pay.find_element(order_loc,timeout=3).text#购买后弹出的订单号
        new_order = order.split(":")
        print(new_order[1])
        time.sleep(3)
        self.pay.check_order()  # 点击查看订单
        time.sleep(2)
        allure.attach("查看列表的订单号", "点击查看生成的第一个订单号")
        first_loc = ("id", "com.tpshop.malls:id/order_sn_tv")  # 生成的第一个订单号
        first_order = self.pay.find_elements(first_loc,timeout=3)[0].text#生成的第一个订单号
        print(first_order)
        time.sleep(3)
        if new_order[1] == first_order:
            print("True")
        else:
            print("False")

