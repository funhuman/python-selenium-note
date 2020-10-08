'''
Open Bing and search Python3
'''

# import
from selenium import webdriver
# 设置浏览器驱动路径
driver_path = r'C:/Program Files (x86)/Microsoft/Edge/Application/msedgedriver.exe'
# 设置页面路径
url = 'https://cn.bing.com/?mkt=zh-cn'
# 生成浏览器对象
driver = webdriver.Edge(driver_path)
#                  ^^^^ 注意：这里根据浏览器决定
# 打开页面
driver.get(url)
# 获取输入框
inputElement = driver.find_element_by_id('sb_form_q')
# 获取搜索按钮
searchButton = driver.find_element_by_id('sb_form_go')
# 输入框输入"Python"
inputElement.send_keys("Python3")
# 搜索
searchButton.click()
