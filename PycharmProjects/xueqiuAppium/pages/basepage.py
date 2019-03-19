#-*- coding:utf-8 -*-
from driver.appium_driver import Driver
from appium.webdriver.webelement import WebElement


class BasePage:
    
    
    def find(*loc):
        return Driver.get_dirver().find_element(*loc)