from appium import webdriver
import os
import time
apk_path = os.path.abspath(os.path.dirname(__file__))
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '8.1.0'
desired_caps['deviceName'] = 'vivo Y85A'
desired_caps['app'] = '{}\\app\\RedMahjong-122test.apk'.format(apk_path)#'com.pingan.idle.redmahjong"  #加包路径会自动安装包
desired_caps['appActivity'] = 'com.pingan.idle.redmahjong.AppActivity'

#初始化driver对象，参数：appium server地址，连接客户端信息
driver = webdriver.Remote(command_executor = 'http://172.21.12.105:1111/wd/hub',
                          desired_capabilities = desired_caps
                          )


#开始进行元素操作
driver.find_element_by_id()



