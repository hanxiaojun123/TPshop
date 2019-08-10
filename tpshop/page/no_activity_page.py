from common.Base import Base,open_mobile
import time

class Pay_no_activity(Base):#继承base类
    login_loc = ("id", "com.tpshop.malls:id/head_img")  # 登录按钮定位
    mobile_loc = ("id", "com.tpshop.malls:id/mobile_et")  # 输入手机号的框框
    password_loc = ("id", "com.tpshop.malls:id/pwd_et")  # 输入密码的框框
    sure_login_loc = ("id", "com.tpshop.malls:id/login_tv")  # 点击登录
    pay_loc = ("xpath", "//*[@text='立即购买']")  # 立即购买的定位
    sure_loc = ("xpath", "//*[@text='确定']")  # 确定按钮定位
    num_add_loc = ("class name", "android.widget.Button")  # 添加数量+的按钮定位
    jifen_loc = ("id", "com.tpshop.malls:id/order_point_sth")  # 使用积分的定位
    balance_loc = ("id", "com.tpshop.malls:id/order_balance_sth")  # 使用余额的定位
    submit_loc = ("id", "com.tpshop.malls:id/submit_tv")  # 提交订单的按钮
    shuru_loc = ("id", "com.tpshop.malls:id/pwd_et")  # 输入密码框的定位
    sure_pay_loc = ("id", "com.tpshop.malls:id/sure_tv")  # 确定支付密码的定位
    my_loc = ("id", "com.tpshop.malls:id/mine_ll]")  # 定位我的
    wait_shouhuo_loc = ("id", "com.tpshop.malls:id/wait_receive_ll]")  # 待收货的定位
    receive_loc = ("id", "com.tpshop.malls:id/status_receive_tv")  # 我的订单里的待收货的定位
    send_loc = ("id", "com.tpshop.malls:id/status_send_tv")  # 我的订单里待发货的定位
    good_loc = ("xpath","//*[@text='航测试手机']")#不参与活动的商品
    daofu_loc = ("xpath", "//*[@text='货到付款']")  # 货到付款
    check_order_loc = ("id", "com.tpshop.malls:id/check_order_tv")  # 查看订单
    def click_good(self):
        """点击不参与活动的商品"""
        self.click(self.good_loc)
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

if __name__ == '__main__':
    driver = open_mobile()
    no_act = Pay_no_activity(driver)
    time.sleep(2)
    base = Base(driver)
    base.swipe_up()#向上滑
    no_act.click_good()
    time.sleep(2)
    no_act.click_pay()#点击立即购买
    time.sleep(2)
    no_act.click_sure()#点击确定
    time.sleep(2)
    no_act.click_jifen()
    time.sleep(2)
    no_act.yu_e()
    time.sleep(2)
    no_act.submit()
    no_act.shuru("123456")
    time.sleep(2)
    no_act.sure_pay()
    time.sleep(2)

