from selenium import webdriver
from selenium.webdriver.common.by import By

options_firefox = webdriver.FirefoxOptions()
options_firefox.add_argument('--headless')

with webdriver.Chrome(options=options_firefox) as browser:
    url = 'https://yandex.ru/'
    browser.get(url)
    a = browser.find_element(By.TAG_NAME, 'a')
    print(a.get_attribute('href'))