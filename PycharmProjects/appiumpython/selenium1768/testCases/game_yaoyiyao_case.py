#-*- coding:utf-8 -*-
import unittest
import os
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from appiumpython.selenium1768.pages import gameyaoyiyao

class YaoyiyaoGameTest(unittest.TestCase):

    game_url = "http://m.1768.com/?act=game_shaizile"
    
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
        
    def loginGame(self):
        self.pagObj.find_element(By.XPATH,'//*[@id="id_pawform"]/div[1]/input').send_keys("languoqing10")
        self.pagObj.find_element(By.ID,"txzpwd").send_keys("LGQ227770l")
        self.pagObj.find_element(By.CLASS_NAME,"btn-submit").click()
        
    def test_gamepage(self):
        self.pagObj.goGamePage(self.game_url)
        self.assertIn("摇一摇",self.pagObj.get_title())
        
    #测试为登录状态下点击跳登录
    def test_isgamelogin(self):
        self.pagObj.goGamePage(self.game_url)
        #清楚cookies
        self.pagObj.delete_cookies()
        #点击押注按钮
        self.pagObj.betClick()
        self.assertIn("passport",self.driver.current_url)
    
    #押注金额为0
    def test_wrongbet(self):
        self.pagObj.goGamePage(self.game_url)
        self.pagObj.delete_cookies()
        self.pagObj.betClick()
        time.sleep(1)
        #跳转登录
        if "passport" in self.driver.current_url:
            #d登录
            self.loginGame()
        self.pagObj.goGamePage("http://m.1768.com/?act=game_shaizile")
        time.sleep(2)
        self.pagObj.goGamePage("http://m.1768.com/?act=game_shaizile")
        time.sleep(3)
        #给押注金额置为 0
        self.pagObj.inputAmout("0")
        time.sleep(3)
        self.pagObj.betClick()
        dis = self.pagObj.find_element(*self.pagObj.up_box).get_attribute("style")
        self.assertFalse(dis)
        
        
        
    
        
if __name__ == '__main__':
    unittest.main()
        
    