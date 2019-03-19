#-*- coding:utf-8 -*-

from appium import webdriver

# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

class Driver:
    
    driver = None
    @staticmethod
    def init():
        '''初始化'''
        caps = {}
        caps["platformName"] = "ANDROID"
        caps["platformVersion"] = "8.1.0"
        caps["deviceName"] = "vivo Y85A"
        caps["app"] = "com.xueqiu.android"
        caps["noReset"] = True
        caps["udid"] = "7bff6865"
        caps["appActivity"] = ".view.WelcomeActivityAlias "
        Driver.driver = webdriver.Remote("http://172.21.12.105:4723/wd/hub", caps)
        Driver.driver.implicitly_wait(4)

    @staticmethod
    def get_dirver():
        return Driver.driver

   
        
    
    
    
        
        
        
