from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from time import sleep

source='ENGLISH'

text="Pritam's real name is Jhaatu"

dest='HINDI'

d={'ENGLISH':0,'HINDI':1}

ind_source=d[source]

ind_dest=d[dest]

options = Options()
options.add_argument("--disable-notifications")
options.add_argument("--disable-extensions")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
options.add_argument("--incognito") 
options.add_argument("--headless") 

driver = webdriver.Chrome(options=options)

driver.maximize_window()

driver.get('https://translate.google.co.in/')
sleep(1)

xpath1='//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[1]/c-wiz/div[1]/c-wiz/div[2]/button/div[3]'
drop_down_source=WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH,xpath1)))
drop_down_source.click()
sleep(1)

xpath_source=['//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[1]/c-wiz/div[2]/c-wiz/div[1]/div/div[3]/div/div[3]/span[58]/div[1]','//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[1]/c-wiz/div[2]/c-wiz/div[1]/div/div[3]/div/div[3]/span[84]/div[1]']
lang_source=WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH,xpath_source[ind_source])))
lang_source.click()
sleep(1)

xpath2='//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[1]/c-wiz/div[1]/c-wiz/div[5]/button/div[3]'
drop_down_dest=WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH,xpath2)))
drop_down_dest.click()
sleep(1)

xpath_dest=['//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[1]/c-wiz/div[2]/c-wiz/div[2]/div/div[3]/div/div[2]/span[58]/div[1]','//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[1]/c-wiz/div[2]/c-wiz/div[2]/div/div[3]/div/div[2]/span[84]/div[1]']
lang_dest=WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH,xpath_dest[ind_dest])))
lang_dest.click()
sleep(1)

xpath_text='//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/div/c-wiz/span/span/div/textarea'
textbox=WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH,xpath_text)))
textbox.send_keys(text)
sleep(1)

xpath_translated_text='//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz/div/div[6]/div/div[1]/span[1]/span/span'
translated_text=WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH,xpath_translated_text)))
print(translated_text.text)
sleep(1)

driver.quit()