#-*- coding:utf-8 -*-
from pages.basepage import BasePage
from driver.appium_driver import Driver
from appium.webdriver.common.mobileby import By


class SearchPage(BasePage):
    #搜索输入框
    searche_input = (By.ID,"search_input_text")
    searche_result = (By.ID, "stockName")
    def get_search_result(self,search_key):
        self.find(*self.searche_input).send_keys(search_key)
        result = Driver.get_dirver().find_elements(*self.searche_result)
        print("++++++++++{}++++++++++++".format(result))
        return result
        