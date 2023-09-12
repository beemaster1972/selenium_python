from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://parsinger.ru/selenium/2/2.html'
with webdriver.Firefox() as browser:
    browser.get(url)
    input_link = browser.find_element(By.LINK_TEXT, '16243162441624')
    input_link.click()
    result = browser.find_element(By.ID, 'result')
    print(result.text)
