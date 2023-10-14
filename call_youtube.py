import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import os

path_to_add = "d:\driver"
abs_path = os.path.abspath(path_to_add)
current_path = os.environ["PATH"]
new_path = current_path + ";" + abs_path
os.environ["PATH"] = new_path
youtube_url='https://www.youtube.com/watch?v=KerQMk-c4qo'
driver = webdriver.Chrome()
driver.get(youtube_url)
time.sleep(10)
play_button=driver.find_element(By.XPATH, '//*[@id="movie_player"]/div[30]/div[2]/div[1]/button')
play_button.click()

driver.execute_script(
    "var theaterButton=document.getElementsByClassName('ytp-size-button')[0]; theaterButton.click();"
)

video_ended=False
while not video_ended:
    time.sleep(2)
    player_status = driver.execute_script("return document.getElementById('movie_player').getPlayerState()")
    if player_status == 0:
        video_ended=True
        print('video ended')

driver.quit()