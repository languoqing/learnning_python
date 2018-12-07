import uiautomator2 as u2
import time
import random

d = u2.connect_usb('7bff6865')
d.app_start('com.pingan.idle.redmahjong')
#d.unlock()
print(d.healthcheck())
print(d.current_app())
print(d.current_app().get('package'))
time.sleep(5)
d.click(0.669, 0.725)
# count = 0
# flag = True
# while(flag):
#     a = round(random.uniform(0,1),3)
#     b = round(random.uniform(0,1),3)
#     d.click(a,b)
#     if d.current_app().get('package') != 'com.pingan.idle.redmahjong':
#         flag = False
#     count += 1
#     if count > 10000:
#         flag = False
# print(d.current_app().get('package'))
# print(count)
# print('==========退出============')
xml = d.dump_hierarchy()
print(xml)

