from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'http://parsinger.ru/selenium/7/7.html'
with webdriver.Firefox() as browser:
    browser.get(url)
    select_list = browser.find_elements(By.TAG_NAME, 'option')
    input_result = browser.find_element(By.ID, 'input_result')
    send_btn = browser.find_element(By.CLASS_NAME, 'btn')
    sum_select = sum([int(select.text) for i, select in enumerate(select_list)])
    input_result.send_keys(str(sum_select))
    send_btn.click()
    result = browser.find_element(By.ID, 'result')
    print(result.text)

