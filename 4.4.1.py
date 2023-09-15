from selenium import webdriver
from selenium.webdriver.common.by import By

proxy = []
options_firefox = webdriver.FirefoxOptions()
options_firefox.add_argument('--headless')
url = 'https://2ip.ru/'
proxy_url = 'https://proxy-store.com/ru/free-proxy'
with webdriver.Firefox(options=options_firefox) as browser:
    browser.get(proxy_url)
    # browser.find_element(By.CLASS_NAME, "btn").click()
    proxy_list = browser.find_elements(By.CLASS_NAME, 'green-card__item-text')
    proxy = [prx.text.splitlines() for prx in proxy_list]
proxy_list = [proxy_addr for lst in proxy for proxy_addr in lst if proxy_addr]
print(proxy)
for proxy_addr in proxy_list:
    try:
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.add_argument('--headless')
        firefox_options.add_argument(f'--proxy-server {proxy_addr}')

        with webdriver.Firefox(options=firefox_options) as browser:
            browser.get(url)
            print(browser.find_element(By.ID, 'd_clip_button').find_element(By.TAG_NAME, 'span').text, proxy_addr)
            browser.set_page_load_timeout(5)
    except Exception as _ex:
        print(f"Превышен timeout ожидания для - {proxy_addr}")
        continue
