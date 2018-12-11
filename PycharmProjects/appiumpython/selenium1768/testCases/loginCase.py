# -*- coding: utf-8 -*-
from appiumpython.selenium1768.pages.loginPage import LoginPage
import unittest
import os
from selenium import webdriver

class LoginTest(unittest.TestCase):
    
    url = "https://passport.1768.com/pass-info/oauth2/login.view?client_id=IN_000005&redirect_uri=http%3A%2F%2Fm.1768.com%2F%3Fact%3Dlogin%26st%3Dlogin_callback&response_type=code&platform=WEB&display=mobile&state=eyJzdGF0ZSI6IjAzZWRlNmYwNTkwM2FkMTY4MjgyNjc0ZDliNjNiMWUxIiwiZnJvbSI6IiIsImFwcGtleSI6IiIsInNlcnZlcklkIjoiIiwibG9naW5Tb3VyY2UiOiIifQ%3D%3D&media_source=game_wap&isapp=1&back_url=http%3A%2F%2Fm.1768.com%2F%3Fact%3Dgame_shaizile%26abeam%3D0&otherLogin=QQ%7CWEIBO%7CWEIXIN%7CYIQIANBAO%7CHAOYISHENG&back_flag=1&mamc=1&gohome_url=&loginPage=1"
    def setUp(self):
        self.webdriver_chrom = r"D:\selenium\chromedriver.exe"
        os.environ['webdriver-chrom'] = self.webdriver_chrom
        self.driver = webdriver.Chrome(self.webdriver_chrom)
        
    def test_url(self):
        driver = self.driver
        loginObj = LoginPage(driver)
        loginObj.goPage(self.url)
        self.assertIn(driver.current_url,self.url,msg='aa')
        
    
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    re = unittest.main()
    