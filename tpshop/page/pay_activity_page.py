from common.Base import Base,open_mobile
import time

class Pay_page(Base):#继承base类
    """封装表现层,制作定位器"""
    login_loc = ("id","	com.tpshop.malls:id/head_img")#登录按钮定位
    mobile_loc = ("id","com.tpshop.malls:id/mobile_et")#输入手机号的框框
    password_loc = ("id","com.tpshop.malls:id/pwd_et")#输入密码的框框
    sure_login_loc = ("id","com.tpshop.malls:id/login_tv")#点击登录
    activity_loc = ("xpath","//*[@text='商品促销']")#商品促销按钮定位
    shop_loc = ("xpath","//*[@text='palda']")#palda商品的定位(活动商品)限购
    shop2_loc = ("xpath","//*[@text='想胜多负少']")
    pay_loc = ("xpath","//*[@text='立即购买']")#立即购买的定位
    sure_loc = ("xpath","//*[@text='确定']")#确定按钮定位
    num_add_loc = ("class name","android.widget.Button")#添加数量+的按钮定位
    jifen_loc = ("id","	com.tpshop.malls:id/order_point_sth")#使用积分的定位
    balance_loc = ("id","com.tpshop.malls:id/order_balance_sth")#使用余额的定位
    submit_loc = ("id","com.tpshop.malls:id/submit_tv")#提交订单的按钮
    toast_loc = ("xpath","//*[contains[@text,'每人限购']")#有的商品限购一件
    daofu_loc = ("xpath", "//*[@text='货到付款']")  # 货到付款
    shuru_loc = ("id","com.tpshop.malls:id/pwd_et")#输入密码框的定位
    sure_pay_loc = ("id","com.tpshop.malls:id/sure_tv")#确定支付密码的定位
    order_num_loc = ("xpath","//*[@text='201908040846404743']")#订单号201908040846404743的定位
    my_loc = ("id","com.tpshop.malls:id/mine_ll]")#定位我的
    wait_shouhuo_loc = ("id","com.tpshop.malls:id/wait_receive_ll]")#待收货的定位
    receive_loc = ("id","com.tpshop.malls:id/status_receive_tv")#我的订单里的待收货的定位
    send_loc = ("id","com.tpshop.malls:id/status_send_tv")#我的订单里待发货的定位
    check_order_loc = ("id","com.tpshop.malls:id/check_order_tv")#查看订单
    first_loc = ("id","	com.tpshop.malls:id/order_sn_tv[0]")#生成的第一个订单号
    order_loc = ("id","	com.tpshop.malls:id/pay_trade_no_tv")#生成订单号
    def login(self):
        """点击登录"""
        self.click(self.login_loc)
    def mobile(self,text):
        """输入手机号"""
        self.send_keys(self.mobile_loc,text)
    def password(self,text):
        """输入密码"""
        self.send_keys(self.password_loc,text)
    def sure_login(self):
        """点击立即登录"""
        self.click(self.sure_login_loc)
    def click_activity(self):
        """点击商品促销类"""
        self.click(self.activity_loc)
    def shop(self):
        """点击活动商品"""
        self.click(self.shop_loc)
    def shop2(self):
        self.click(self.shop2_loc)
    # def click_rice(self):
    #     """定位大米"""
    #     self.click(self.rice_loc)
    def click_pay(self):
        """点击立即购买"""
        self.click(self.pay_loc)
    def click_sure(self):
        """点击确定"""
        self.click(self.sure_loc)
    def click_num_add(self):
        """添加数量的加号"""
        self.click(self.num_add_loc)
    def click_jifen(self):
        """点击积分"""
        self.click(self.jifen_loc)
    def yu_e(self):
        """使用余额"""
        self.click(self.balance_loc)
    def submit(self):
        """提交订单"""
        self.click(self.submit_loc)
    def shuru(self,text):
        """输入密码"""
        self.send_keys(self.shuru_loc,text)
    def sure_pay(self):
        """确认支付"""
        self.click(self.sure_pay_loc)
    def click_my(self):
        """我的"""
        self.click(self.my_loc)
    def wait_shouhuo(self):
        """待收货"""
        self.click(self.wait_shouhuo_loc)
    def receive(self):
        """我的订单的待收货"""
        self.click(self.receive_loc)
    def send(self):
        """我的订单里的待发货"""
        self.click(self.send_loc)
    def daofu(self):
        """货到付款"""
        self.click(self.daofu_loc)
    def check_order(self):
        """查看订单号"""
        self.click(self.check_order_loc)
    def first_order(self):
        """查看生成的第一个订单"""
        self.click(self.first_loc)
    def toast(self):
        self.get_toast("每人限购")

if __name__ == '__main__':

    driver = open_mobile()
    base = Base(driver)
    pay = Pay_page(driver)
    time.sleep(3)
    pay.click_activity()
    # pay.click_rice()
    time.sleep(2)
    base.swipe_up()
    pay.shop()
    time.sleep(3)
    pay.click_pay()
    time.sleep(2)
    pay.click_sure()
    time.sleep(2)
    pay.click_jifen()
    time.sleep(2)
    pay.yu_e()
    time.sleep(2)
    pay.submit()
    pay.shuru("123456")
    time.sleep(2)
    pay.sure_pay()
    time.sleep(2)
    # pay.click_my()
    # time.sleep(2)
    # pay.login()
    # time.sleep(3)
    # pay.mobile("12345678901")
    # time.sleep(3)
    # pay.password("123456")
    # time.sleep(3)
    # pay.sure_login()
