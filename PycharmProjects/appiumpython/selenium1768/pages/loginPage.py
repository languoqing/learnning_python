# -*- coding: utf-8 -*-
from appiumpython.selenium1768.BasePage import Base
from selenium.webdriver.common.by import By



class LoginPage(Base):
    
    #登录元素
    txz = (By.XPATH,"/html/body/div[3]/div[1]/span[1]")
    wlt = (By.CLASS_NAME,"wlt current")
    txz_username = (By.ID,"unamePa")
    txz_password = (By.ID,"pwdPa")
    wlt_username = (By.ID,"loginName")
    wlt_password = (By.ID,"pwdWlt")
    login_btn = (By.ID,"id_login")
    #登录失败浮层
    login_false = (By.ID,"popupBox")

    #登录第三方元素
    sina = (By.CLASS_NAME, "sina")
    tencenqq = (By.CLASS_NAME, "qq")
    payiqb = (By.CLASS_NAME, "yiqb")
    pahys = (By.CLASS_NAME, "pahys")
    def __init__(self,driver):
        super(LoginPage,self).__init__(driver)
        
    def goPage(self,url):
        print('打开页面，url:{}'.format(url))
        self.goToPage(url)
     
     #登录操作
    def lgin(self,userloctor,pwdloctor,user,pwd):
        print("输入用户名，user:{}".format(user))
        self.send(userloctor,user)
        print("输入密码，pwd:{}".format(pwd))
        self.send(pwdloctor,pwd)
        print("开始登录")
        self.click(self.login_btn)
        
    #第三方登录
    def otherLogin(self,otherloginBtn):
        print("点击按钮 {}".format(otherloginBtn))
        self.click(otherloginBtn)
        
        

 