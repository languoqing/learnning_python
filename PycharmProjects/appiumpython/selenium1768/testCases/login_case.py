# -*- coding: utf-8 -*-
from appiumpython.selenium1768.pages.loginPage import LoginPage
import unittest
import os
from selenium import webdriver
import time
import HTMLTestRunner

class LoginTest(unittest.TestCase):

    url = "https://passport.1768.com/pass-info/oauth2/login.view?client_id=IN_000005&redirect_uri=http%3A%2F%2Fm.1768.com%2F%3Fact%3Dlogin%26st%3Dlogin_callback&response_type=code&platform=IOS&display=mobile&state=eyJzdGF0ZSI6ImVmNTA0NDA0OTc2ZDUxYWZjNTAxNTI0YTM5YzhlMDcyIiwiZnJvbSI6IiIsImFwcGtleSI6IiIsInNlcnZlcklkIjoiIiwibG9naW5Tb3VyY2UiOiIifQ%3D%3D&media_source=game_wap&isapp=1&back_url=http%3A%2F%2Fm.1768.com%2F%3Fact%3Dgame_shaizile%26abeam%3D0&otherLogin=QQ%7CWEIBO%7CWEIXIN%7CYIQIANBAO%7CHAOYISHENG&back_flag=1&mamc=1&gohome_url="
    @classmethod
    def setUpClass(cls):
        cls.webdriver_chrom = r"D:\selenium\chromedriver.exe"
        os.environ['webdriver-chrom'] = cls.webdriver_chrom
        cls.driver = webdriver.Chrome(cls.webdriver_chrom)
        cls.driver.set_window_size(375, 812)
        cls.pageObj = LoginPage(cls.driver)
        
    def test_url(self):
        self.pageObj.goPage(self.url)
        self.assertIn(self.driver.current_url,self.url,msg='aa')
    
    #测试登录
    def test_txzlogin(self):
        self.pageObj.goPage(self.url)
        #选中通行证
        self.pageObj.find_element(*self.pageObj.txz)
        #账号密码登录
        self.pageObj.send("languoqing10",*self.pageObj.txz_username)
        time.sleep(3)
        self.pageObj.send( "LGQ227770l",*self.pageObj.txz_password)
        self.pageObj.click(*self.pageObj.login_btn)
        
        #等待跳转页面
        time.sleep(5)
        self.assertIn("//m.1768.com",self.driver.current_url)
    
    def test_loginFalse(self):
        self.pageObj.goPage(self.url)
        # 选中通行证
        self.pageObj.find_element(*self.pageObj.txz)
        # 账号密码登录
        self.pageObj.send("languoqing10", *self.pageObj.txz_username)
        self.pageObj.send("LGQ227", *self.pageObj.txz_password)
        self.pageObj.click(*self.pageObj.login_btn)
        time.sleep(1)
        #判断提示浮层
        self.assertTrue(self.pageObj.find_element(*self.pageObj.login_false))
        
    #第三方登录 QQ
    def test_loginQQ(self):
        self.pageObj.goPage(self.url)
        #选中QQ点击
        self.pageObj.click(*self.pageObj.tencenqq)
        time.sleep(1)
        self.assertIn("qq.com",self.driver.current_url)
    @classmethod
    def tearDownClass(cls):
        cls.pageObj.quit()

if __name__ == '__main__':
    re = unittest.main()
    