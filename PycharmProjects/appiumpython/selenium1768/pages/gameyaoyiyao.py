# -*- coding: utf-8 -*-
from appiumpython.selenium1768.BasePage import Base
from selenium.webdriver.common.by import By


class GameYaoYiYao(Base):
    
    #页面元素
    paihb_btn = (By.ID,"inpage")
    addamount_btn = (By.XPATH,"/html/body/div[3]/div[7]/div/div[1]/span[2]")
    cutamount_btn = (By.XPATH,"/html/body/div[3]/div[7]/div/div[1]/span[1]")
    yz_input = (By.XPATH,r"//*[@id='ipt_yazhu']")
    maxamount_btn = (By.ID,"maxBet")
    cz_btn = (By.XPATH,"/html/body/div[3]/div[7]/div/div[2]/span[2]")
    bet_btn = (By.ID,"start")
    #余额区域
    yue_loctor = (By.ID,"YconRemaining")
    
    def __init__(self):
        super(GameYaoYiYao,self).__init__()
        
    def goGamePage(self,url):
        self.goToPage(url)
    
    def showPahangbang(self):
        self.click(self.paihb_btn)
        
    def showYue(self):
        self.click(self.yue_loctor)
        
    def addAmoount(self):
        self.click(self.addamount_btn)
    
    def cutamout(self):
        self.click(self.cutamount_btn)
        
    def inputAmout(self,value):
        #先清除再发送
        self.clearInput()
        self.send(self.yz_input,value)
        
    def betClick(self):
        #获取这个btn的class属性值
        btn_at = self.find_element(self.yz_input).get_attribute('class')
        #判断可点击
        print("此时押注 按钮class属性为：{}".format(btn_at))
        if btn_at == "start btn_active":
            self.click(self.bet_btn)
        