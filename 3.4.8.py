from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'http://parsinger.ru/selenium/4/4.html'
with webdriver.Firefox() as browser:
    browser.get(url)
    chk_boxes = browser.find_elements(By.CLASS_NAME, 'check')
    send_btn = browser.find_element(By.CLASS_NAME, 'btn')
    for i, chk in enumerate(chk_boxes):
        chk.click()
    send_btn.click()
    result = browser.find_element(By.ID, 'result')
    print(result.text)

