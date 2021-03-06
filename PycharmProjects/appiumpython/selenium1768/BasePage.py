# -*- coding: utf-8 -*-

class Base(object):
    """
    所有的page类继承该类，封装所有的公共方法
    """
    def __init__(self,driver):
        self.driver = driver
        #self.driver.set_window_size(375,812)
        
        
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
    
    def clearInput(self,*inputloctor):
        return self.find_element(*inputloctor).clear()
    
    def quit(self):
        return self.driver.quit()
    
    def get_title(self):
        return self.driver.title
    
    def get_cookie(self,name):
        return self.driver.get_cookie(name)
    
    def get_cookies(self):
        return self.driver.get_cookies()
    
    def delete_cookies(self):
        return self.driver.delete_all_cookies()