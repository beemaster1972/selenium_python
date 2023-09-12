from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://parsinger.ru/selenium/3/3.html'
with webdriver.Firefox() as browser:
    browser.get(url)
    tags = browser.find_elements(By.XPATH, '//p')
    nums = [int(tag.text) for i, tag in enumerate(tags)]
    print(sum(nums))
