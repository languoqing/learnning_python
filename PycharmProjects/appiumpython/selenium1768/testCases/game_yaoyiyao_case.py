#-*- coding:utf-8 -*-
import unittest
import os
import time
from selenium import webdriver
from appiumpython.selenium1768.pages import gameyaoyiyao

class YaoyiyaoGameTest(unittest.TestCase):

    game_url = "http://m.1768.com/?act=game_shaizile&abeam=0"
    
    @classmethod
    def setUpClass(cls):
        cls.webdriver_chrom = r"D:\selenium\chromedriver.exe"
        os.environ['webdriver-chrom'] = cls.webdriver_chrom
        cls.driver = webdriver.Chrome(cls.webdriver_chrom)
        cls.pagObj = gameyaoyiyao.GameYaoYiYao(cls.driver)
        cls.driver.set_window_size(375, 812)

    @classmethod
    def tearDownClass(cls):
        cls.pagObj.quit()
        
    def test_gamepage(self):
        self.pagObj.goGamePage(self.game_url)
        self.assertIn("摇一摇",self.pagObj.get_title())
        
    #测试为登录状态下点击跳登录
    def test_isgamelogin(self):
        self.pagObj.goGamePage(self.game_url)
        #获取页面cookie值,有则删除
        has_cookie = self.pagObj.get_cookies()
        if has_cookie:
            self.pagObj.delete_cookies()
        #点击押注按钮
        self.pagObj.betClick()
        self.assertIn("passport",self.driver.current_url)
        
        
    
        
if __name__ == '__main__':
    unittest.main()
        
    