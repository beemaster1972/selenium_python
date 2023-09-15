import time

from selenium import webdriver
from selenium.webdriver.common.by import By

options_firefox = webdriver.FirefoxOptions()
options_firefox.add_argument('--headless')
url = 'https://2ip.ru/'
proxy_url = 'https://proxy-store.com/ru/free-proxy'
with webdriver.Firefox(options=options_firefox) as browser:
    browser.get(proxy_url)
    # browser.find_element(By.CLASS_NAME, "btn").click()
    proxy = [prx.text.splitlines()[0] for prx in browser.find_elements(By.CLASS_NAME, 'table__row')][1:]
firefox_options = webdriver.FirefoxOptions()
print(f'-proxy-server {proxy[0]}')
firefox_options.add_argument(f'--proxy-server={proxy[0]}')

with webdriver.Firefox(options=firefox_options) as browser:
    browser.get(url)
    print(browser.find_element(By.ID, 'd_clip_button').find_element(By.TAG_NAME, 'span').text)
    time.sleep(2)
