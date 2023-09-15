from selenium import webdriver
import time
url = 'http://parsinger.ru/selenium/6/6.html'
with webdriver.Firefox() as browser:
    browser.install_addon('coords-0.9.6.xpi')
    browser.get(url)
    time.sleep(500)