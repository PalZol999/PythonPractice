from selenium import webdriver
from selenium.webdriver.common.by import By
import time

bro = webdriver.Firefox()
bro.get('https://nexus.hexagon.com/')
time.sleep(4)

elem=bro.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div/div[2]/div/div/button[1]")
elem.click()

elemSign=bro.find_element(By.XPATH, "/html/body/div[1]/div/div/header/div/div/ul/li[3]/a")
time.sleep(1)
elemSign.click()

elemWrite=bro.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div/div[2]/form/fieldset/div/div[1]/div/div/input")
time.sleep(2)
elemWrite.send_keys('Pierre')

time.sleep(3)
bro.quit()