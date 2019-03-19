#-*- coding:utf-8 -*-
import unittest
from pages.mainpage import MainPage
from driver.appium_driver import Driver

class SearchPageTest(unittest.TestCase):
    
    main_page = None
    search_page = None
    
    
    
    def setUp(self):
        self.main_page = MainPage.go_main_page()
        self.search_page = self.main_page.go_search_page()
       
    def test_search(self):
        
        key = "pdd"
        re = self.search_page.get_search_result(key)
        print(re)
        
    def tearDown(self):
        Driver.get_dirver().close_app()
        