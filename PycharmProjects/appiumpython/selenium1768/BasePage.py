# -*- coding: utf-8 -*-

class Base(object):
    """
    所有的page类继承该类
    """
    def __init__(self,driver):
        self.driver = driver
        
        
    def goToPage(self,url):
        return self.driver.get(url)
        
    def find_element(self,*loctor):
        """
        
        :param loctor eg find_element(By.ID,'foo'):
        :return: WebElement
        """
        return self.driver.find_element(*loctor)
    
    def click(self,*loctor):
        """
        
        :param loctor the loctor mast be clickabel:
        :return:
        """
        return self.find_element(*loctor).click()
    
    def send(self,message,*loctor):
        return self.find_element(*loctor).send_keys(message)
    
    def clearInput(self,inputloctor):
        return self.find_element(*inputloctor).clear()
    