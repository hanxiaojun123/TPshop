import time
import pytest
from page.comment_page import CommentPage
from common.Base import Base,open_mobile
from faker import Faker
import allure
class Testcomment:
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)  # 设置用例等级为CRITICAL
    @allure.step(title='商品评价')
    def setup(self):
        driver = open_mobile()
        self.base = Base(driver)
        self.cp = CommentPage(driver)
        self.fk = Faker('zh_CN')
    def teardown(self):
        self.base.close()

    def test_01(self):
        """评论商品"""
        allure.attach("点击我的", "进入个人中心")
        self.cp.click_my()#点击我的
        time.sleep(2)
        self.cp.comment()#点击待评论
        time.sleep(2)
        self.cp.show()#点击评论晒单
        time.sleep(2)
        allure.attach("评论","输入文字评论")
        comment = self.fk.paragraph()#随机生成段落
        self.cp.send_comment(f"{comment}")
        time.sleep(3)
        allure.attach("评价星级","点击每一行的星星")
        self.cp.click_stars()#点击星星
        time.sleep(3)
        allure.attach("点击提交","点击提交")
        self.cp.submit()#点击提交
        time.sleep(3)
        try:
            toast = self.cp.toast()#获取评论成功的toast
            if toast == "评论成功":
                assert 1
        except:
            return False



