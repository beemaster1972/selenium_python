import time
from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Firefox() as browser:
    browser.get('https://parsinger.ru/selenium/1/1.html')
    input_forms = browser.find_elements(By.CLASS_NAME, 'form')
    button = browser.find_element(By.CLASS_NAME, 'btn')
    for i, form in enumerate(input_forms):
        form.send_keys('Text')
    button.click()
    time.sleep(20)
