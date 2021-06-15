from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
def init_browser(url):
    global browser
    browser = webdriver.Chrome(executable_path = "./chromedriver")
    #url = 'https://www.facebook.com'
    browser.get(url)
    sleep(2)
    print('Initial browser')
    #Login
def login(username, password1):
    email = browser.find_element_by_id('email')
    email.send_keys(username)
    sleep(3)
    password = browser.find_element_by_id('pass')
    password.send_keys(password1)
    sleep(3)
    password.send_keys(Keys.ENTER)
    sleep(2)
    print('Login successful')
#crawl()
if __name__ == '__main__':
    url = 'https://www.facebook.com'
    init_browser(url)
    username = '0923689987'
    password1 = 'maiminhxa'
    login(username, password1)

    #browser.close()