import time
from selenium import webdriver
from selenium.webdriver.common.by import By

proxy = ['5.44.42.115:10526']
url = 'https://2ip.ru/'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=%s' % proxy)

with webdriver.Chrome(options=chrome_options) as browser:
    browser.get(url)
    # print(browser.find_element(By.ID, 'd_clip_button').find_element(By.TAG_NAME, 'span').text)
    time.sleep(50)