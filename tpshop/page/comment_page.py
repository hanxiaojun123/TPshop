from common.Base import Base,open_mobile
import time

class CommentPage(Base):#继承Base类
    """封装表现层"""
    my_loc = ("id", "com.tpshop.malls:id/mine_tv")  #定位我的
    car_loc = ("id","com.tpshop.malls:id/cart_tv")#定位购物车
    wait_shouhuo_loc = ("id", "com.tpshop.malls:id/wait_receive_ll]")  # 待收货的定位
    sure_shouhuo_local = ("xpath","//*[@text='确认收货']")#定位确认收货
    sure_loc = ("id","com.tpshop.malls:id/positiveButton")#确定按钮
    comment_loc = ("id","com.tpshop.malls:id/wait_comment_ll")#待评价按钮
    show_loc = ("id","com.tpshop.malls:id/order_show_btn")#评价晒单按钮
    send_comment_loc = ("id","com.tpshop.malls:id/comment_content_et")#评论输入框
    star_loc = ("id","com.tpshop.malls:id/star5_btn")#五颗星星的点击
    # star2_loc = ("class name", "android.widget.Button")[9]  # 第二排五颗星星的点击
    submit_loc = ("xpath","//*[@text='提交']")#提交按钮
    look_com_loc = ("xpath","//*[@text='查看评价']")#查看评价按钮
    all_loc = ("id","com.tpshop.malls:id/all_btn")#全部好评
    great_loc = ("id","	com.tpshop.malls:id/great_btn")#好的评论
    average_loc = ("id","com.tpshop.malls:id/average_btn")#中评
    bad_loc = ("id","com.tpshop.malls:id/bad_btn")#差评
    png_loc = ("id","com.tpshop.malls:id/pic_btn")#有图

    def click_my(self):
        """我的"""
        self.click(self.my_loc)
    def car(self):
        """定位购物车"""
        self.click(self.car_loc)
    def comment(self):
        """点击待评价"""
        self.click(self.comment_loc)
    def show(self):
        """点击评价晒单"""
        self.click(self.show_loc)
    def send_comment(self,text):
        """写评价"""
        self.send_keys(self.send_comment_loc,text)
    def click_stars(self):
        """点击每一行的第五颗星星"""
        elements = self.find_elements(self.star_loc)
        for i in elements:
            i.click()

    def submit(self):
        """点击提交"""
        self.click(self.submit_loc)

    def toast(self):
        self.get_toast("评论成功")

if __name__ == '__main__':
    driver = open_mobile()
    base = Base(driver)
    cp = CommentPage(driver)
    cp.click_my()
    cp.comment()
    cp.show()
    cp.click_stars()


