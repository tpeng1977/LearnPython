from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

path_to_add = "d:\driver"
abs_path = os.path.abspath(path_to_add)
current_path = os.environ["PATH"]
new_path = current_path + ";" + abs_path
os.environ["PATH"] = new_path
options = webdriver.ChromeOptions()
options.binary_location = r'C:\Program Files (x86)\Tencent\QQBrowser\QQBrowser.exe'
driver = webdriver.Chrome(options=options)
driver.get('https://www.qq.com')
while True:
    time.sleep(2)