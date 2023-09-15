from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'http://parsinger.ru/selenium/6/6.html'
with webdriver.Firefox() as browser:
    browser.get(url)
    equation = browser.find_element(By.ID, 'text_box')
    target = str(eval(equation.text))
    select_list = browser.find_elements(By.TAG_NAME, 'option')
    selected = list(filter(lambda x: x.text == target, select_list))[0]
    selected.click()
    send_btn = browser.find_element(By.CLASS_NAME, 'btn')
    send_btn.click()
    result = browser.find_element(By.ID, 'result')
    print(result.text)

