from appium import webdriver
import time
desired_caps = {}

desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '8.1.0'
desired_caps['deviceName'] = 'vivo Y857'
desired_caps['appPackage'] = 'com.android.bbkcalculator'
desired_caps['appActivity'] = '.Calculator'

driver = webdriver.Remote('http://172.21.8.107:1111/wd/hub', desired_caps)

driver.find_element_by_id('digit1').click()

driver.find_element_by_id("digit5").click()

driver.find_element_by_id('mul').click()

driver.find_element_by_id("digit9").click()

driver.find_element_by_id("clear1").click()

driver.find_element_by_id("digit9").click()
#
# driver.find_element_by_name("5").click()
#
# driver.find_element_by_name("+").click()
#
# driver.find_element_by_name("6").click()

driver.find_element_by_id("equal").click()

time.sleep(5)

driver.quit()
