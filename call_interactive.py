# http://localhost:63342/LearnPython/testpage.html
# Import webdriver module and ActionChains class
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
# Create a driver object for Chrome browser
driver = webdriver.Chrome()

# Load the URL of the web page
driver.get("file:///C:/Users/Joyshop/PycharmProjects/LearnPython/testpage.html")
time.sleep(5)

# Find the element to hover over by its CSS_SELECTOR
element = driver.find_element(By.CSS_SELECTOR, "body > div.button")

# Create an ActionChains object and move the cursor to the element
action = ActionChains(driver)
action.move_to_element(element)

# Perform the action
action.perform()
#time.sleep(5)

# Find the element to hover over by its CSS_SELECTOR
element = driver.find_element(By.CSS_SELECTOR, "#menu > li:nth-child(2)")

# Create an ActionChains object and move the cursor to the element
action = ActionChains(driver)
action.move_to_element(element)
# Perform the action
action.perform()
time.sleep(20)



