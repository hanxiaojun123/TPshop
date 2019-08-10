import time
import pytest
from page.pay_activity_page import Pay_page
from common.Base import Base,open_mobile
import allure
class TestPay:
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)  # 设置用例等级为CRITICAL
    @allure.step(title='使用货到付款购物')
    def setup(self):
        driver = open_mobile()
        self.base = Base(driver)
        self.pay = Pay_page(driver)
    def teardown(self):
        self.base.close()
    def test_pay_01(self):
        """限购一件商品"""
        allure.attach("点击商品促销", "进入商品促销")
        self.pay.click_activity()#点击商品促销
        time.sleep(2)
        self.base.swipe_up()#向上滑
        allure.attach("选择商品","选择的商品")
        self.pay.shop()#点击活动商品
        time.sleep(2)
        self.pay.click_pay()#点击立即购买
        time.sleep(2)
        allure.attach("确定数量和商品", "点击确定")
        self.pay.click_sure()#点击确定
        time.sleep(2)
        allure.attach("处理限购", "获取toast")
        self.pay.toast() #获取toast限购一件
        # self.pay.click_jifen()#点击积分
        # time.sleep(2)
        # self.pay.yu_e()#点击余额
        # time.sleep(2)
        # self.pay.submit()#点击提交
        # time.sleep(2)
        # self.pay.shuru("123456")#输入支付密码
        # allure.attach("货到付款")
        # self.pay.daofu()
        # time.sleep(2)
        # self.pay.sure_pay()
        # self.pay.check_order()#查看订单
        # time.sleep(2)

    def test_02(self):
        """购买活动商品"""
        allure.attach("点击商品促销", "进入商品促销")
        self.pay.click_activity()  # 点击商品促销
        time.sleep(2)
        # self.base.swipe_up()  # 向上滑
        self.pay.shop2()  # 点击活动商品
        time.sleep(2)
        self.pay.click_pay()  # 点击立即购买
        time.sleep(2)
        allure.attach("确定数量和商品", "点击确定")
        self.pay.click_sure()  # 点击确定
        time.sleep(2)
        # self.pay.click_jifen()#点击积分
        # time.sleep(2)
        # self.pay.yu_e()#点击余额
        # time.sleep(2)
        allure.attach("提交订单", "点击提交")
        self.pay.submit()  # 点击提交
        time.sleep(2)
        # self.pay.shuru("123456")#输入支付密码
        # time.sleep(3)
        # self.pay.sure_pay()
        # time.sleep(2)
        self.pay.daofu()
        time.sleep(2)
        allure.attach("显示的订单号", "购买后生成的订单号")
        order_loc = ("id", "com.tpshop.malls:id/pay_trade_no_tv")  # 生成订单号
        order = self.pay.find_element(order_loc, timeout=3).text  # 购买后弹出的订单号
        new_order = order.split(":")
        print(new_order[1])
        time.sleep(3)
        self.pay.check_order()  # 点击查看订单
        time.sleep(2)
        allure.attach("查看列表的订单号", "点击查看生成的第一个订单号")
        first_loc = ("id", "com.tpshop.malls:id/order_sn_tv")  # 生成的第一个订单号
        first_order = self.pay.find_elements(first_loc, timeout=3)[0].text  # 生成的第一个订单号
        print(first_order)
        time.sleep(3)
        if new_order[1] == first_order:
            print("True")
        else:
            print("False")






