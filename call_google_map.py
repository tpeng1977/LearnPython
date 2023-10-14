"""
searchbox   //*[@id="searchboxinput"]
searchbutton  //*[@id="searchbox-searchbutton"]
direction  //*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]/div[1]/button/span/span
frominput //*[@id="sb_ifc50"]/input
from_search_button  //*[@id="directions-searchbox-0"]/button[1]
hours //*[@id="section-directions-trip-1"]/div[1]/div/div[1]/div[1]
distance //*[@id="section-directions-trip-1"]/div[1]/div/div[1]/div[2]/div
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import os

path_to_add = "d:\driver"
abs_path = os.path.abspath(path_to_add)
current_path = os.environ["PATH"]
new_path = current_path + ";" + abs_path
os.environ["PATH"] = new_path

google_map_url = "https://www.google.com/maps/@49.416591,6.1517344,6z?entry=ttu"
driver = webdriver.Chrome()
driver.get(google_map_url)


def search_place():
    place = driver.find_element(By.XPATH, '//*[@id="searchboxinput"]')
    place.send_keys('伯明翰')
    submit = driver.find_element(By.XPATH, '//*[@id="searchbox-searchbutton"]')
    submit.click()


def direction():
    direct = driver.find_element(By.XPATH,
                                 '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]/div[1]/button/span/span')
    direct.click()


def start_point():
    place = driver.find_element(By.XPATH, '//*[@id="sb_ifc50"]/input')
    place.send_keys('London')
    submit = driver.find_element(By.XPATH, '//*[@id="directions-searchbox-0"]/button[1]')
    submit.click()


def print_info():
    distance = driver.find_element(By.XPATH, '//*[@id="section-directions-trip-1"]/div[1]/div/div[1]/div[2]/div')
    print('distance', distance.text)
    time_via_car = driver.find_element(By.XPATH, '//*[@id="section-directions-trip-1"]/div[1]/div/div[1]/div[1]')
    print('time', time_via_car.text)


if __name__ == "__main__":
    time.sleep(10)
    search_place()
    time.sleep(10)
    direction()
    time.sleep(10)
    start_point()
    time.sleep(10)
    print_info()
    time.sleep(5)
