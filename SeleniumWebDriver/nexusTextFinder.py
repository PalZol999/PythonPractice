from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

bro = webdriver.Firefox()
bro.get('https://nexus.hexagon.com/')
time.sleep(4)


elem=bro.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div/div[2]/div/div/button[1]")
time.sleep(1)
elem.click()

elemNew=bro.find_element(By.XPATH, "/html/body/div[1]/div/div/header/div/div/div/nav/ul/li[4]/a")
time.sleep(1)
elemNew.click()


wait = WebDriverWait(bro, 10)
elemText = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/div/main/div/div/footer/div[2]/div/article[1]/h3")))

print(elemText.text)

time.sleep(2)
bro.quit()