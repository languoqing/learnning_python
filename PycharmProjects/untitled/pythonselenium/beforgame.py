from selenium import webdriver
import os
import time

#webdriver 添加到执行
webdriver_chrom = "D:\selenium\chromedriver_win32\chromedriver.exe"
os.environ['webdriver-chrom'] = webdriver_chrom
#获取webdriver 对象
def getChromObj():
    return webdriver.Chrome(webdriver_chrom)