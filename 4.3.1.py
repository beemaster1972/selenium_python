import time
from selenium import webdriver

user_profile = '/home/beemaster/.mozilla/firefox/aa13cj0p.default-esr'
options_firefox = webdriver.FirefoxOptions()
options_firefox.add_argument(user_profile)
with webdriver.Chrome(options=options_firefox) as browser:
    url = 'https://yandex.ru/'
    browser.get(url)
    time.sleep(10)
