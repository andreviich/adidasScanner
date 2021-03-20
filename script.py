from selenium import webdriver
from selenium.webdriver import ActionChains
import requests
import time
import os
from selenium.webdriver.common.by import By
import selenium
from threading import Thread
def initChrome():
    comm = os.system('chrome --remote-debugging-port=3050  --user-data-dir="c:\selenium\didasProfile" "https://www.adidas.ru/streetball"') 
th1 = Thread(target=initChrome)
th1.start()
chromedriver = 'chromedriver'
options = webdriver.ChromeOptions()
options.add_experimental_option("debuggerAddress", "127.0.0.1:3050")
browser = webdriver.Chrome(executable_path=chromedriver, options=options)

while True:
    time.sleep(2)
    cross = browser.find_elements_by_css_selector('.gl-price-item')

    for i in cross:
        priceString = i.text
        try:
            price = int(''.join([p for p in priceString if p.isdigit()]))
            print(price)
            if price < 10000:
                card  = i.find_element(By.XPATH, '..').find_element(By.XPATH, '..').find_element(By.XPATH, '..').get_attribute('href')
                print(card)
                print('Ого! Вот оно!')
        except Exception as e:
            print(e)
            
    # print(cross)
    time.sleep(2)
    browser.refresh()
