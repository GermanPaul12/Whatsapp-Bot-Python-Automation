from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyperclip
from selenium.webdriver.common.keys import Keys
import sys
from config import CHROME_PROFILE_PATH

#wenn man kein Bild senden möchte einfach von "True" auf "False" ändern
image = False

with open('/Users/german/Documents/Coding/Python projects/My coding projects/Automation with Python/Whatsapp Bot/groups.txt', 'r', encoding='utf8') as f:
    groups = [group.strip() for group in f.readlines()]

with open('/Users/german/Documents/Coding/Python projects/My coding projects/Automation with Python/Whatsapp Bot/msg.txt', 'r', encoding='utf8') as f:
    msg = f.read()     

options = webdriver.ChromeOptions()
options.add_argument(CHROME_PROFILE_PATH)
#/Applications/chromedriver
#'/Users/german/Documents/Python projects/My coding projects/Learning Python/Own Projects/Web Scraping Tests/Whatsapp Bot/chromedriver'
browser = webdriver.Chrome(executable_path='/Applications/chromedriver', options=options)
browser.maximize_window()
browser.get('https://web.whatsapp.com')



time.sleep(15)

for group in groups:
    search_xpath = '//div[@contenteditable="true"][@data-tab="3"]'
    
    search_box = WebDriverWait(browser, 500).until(
        EC.presence_of_element_located((By.XPATH, search_xpath))
    )

    search_box.clear()

    time.sleep(2)

    pyperclip.copy(group)

    search_box.send_keys(Keys.COMMAND + 'v')

    time.sleep(2)

    group_title = WebDriverWait(browser, 500).until(
        EC.presence_of_element_located((By.XPATH, search_xpath))
    )
    group_xpath = f'//span[@title="{group}"]'
    group_title = browser.find_element(By.XPATH, group_xpath)
    #times gibt an wieviel mal die NAchricht verschickt werden soll
    times = 10
    group_title.click()

    time.sleep(1)
    for i in range(times):
        input_xpath = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p'
        input_box = browser.find_element(By.XPATH ,input_xpath)
    
        pyperclip.copy(msg)
        input_box.send_keys(Keys.COMMAND + 'v')
        input_box.send_keys(Keys.ENTER)

    time.sleep(1)

try: 
    if image == True:
        attachment_box = browser.find_element(By.XPATH, '//div[@title="Attach"] ')  
        attachment_box.click()
        time.sleep(1)   

        image_box = browser.find_element(By.XPATH, '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
        image_box.send_keys('C:/Users/Germa/OneDrive/Desktop/Coding/Übungsdateien/Python/Learning Python/Own Projects/Web Scraping Tests/Test.jpg')
        time.sleep(1)
        image_send = browser.find_element(By.XPATH, '//span[@data-icon="send"]')
        image_send.click()
except IndexError: 
    pass
browser.close()

