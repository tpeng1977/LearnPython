# 导入 selenium库
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

path_to_add = "d:\driver"
abs_path = os.path.abspath(path_to_add)
current_path = os.environ["PATH"]
new_path = current_path + ";" + abs_path
os.environ["PATH"] = new_path
youtube_url = "https://www.youtube.com/watch?v=uqI4Pf6mTzQ"

driver = webdriver.Firefox()
driver.get("https://www.youtube.com/watch?v=uqI4Pf6mTzQ")

while True:
    driver.implicitly_wait(2)