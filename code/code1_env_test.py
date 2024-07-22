'''
Open Bing and search Python3 (Edge)
打开必应并搜索“Python3”（Edge浏览器）
'''

# 导入time
import time
# 导入Selenium
from selenium import webdriver
# 导入Selenium的元素查找方法By
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
# 设置浏览器驱动路径（根据自己的配置）
driver_path = Service(r'C:/Program Files (x86)/Microsoft/Edge/Application/msedgedriver.exe')
# 设置页面路径
url = 'https://cn.bing.com/?mkt=zh-cn'
# 生成浏览器对象
driver = webdriver.Edge(service=driver_path)
#                  ^^^^ 注意：这里根据自己的浏览器决定
# 打开页面
driver.get(url)
# 等待1秒
time.sleep(1)
# 获取输入框
inputElement = driver.find_element(By.ID, 'sb_form_q')
# 获取搜索按钮
searchButton = driver.find_element(By.ID, 'sb_form_go')
# 输入框输入Python3
inputElement.send_keys("Python3")
# 等待1秒
time.sleep(1)
# 搜索
searchButton.submit()
# 等待5秒
time.sleep(5)
