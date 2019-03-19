#-*- coding:utf-8 -*-
from pages.basepage import BasePage
from driver.appium_driver import Driver
from appium.webdriver.common.mobileby import By
from pages.searchpage import SearchPage


class MainPage(BasePage):
    #搜索框
    search_loc = (By.ID,"tv_search")
    @staticmethod
    def go_main_page():
        Driver.init()
        return MainPage()
    
    def go_search_page(self):
        self.find(*self.search_loc).click()
        return SearchPage()