from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import wget
#Login to Instagram account
def log_in(user,passw, url, keyword):
    global driver
    driver = webdriver.Chrome(executable_path='./chromedriver')
    driver.get(url)
    sleep(3)
    username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
    password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

    username.clear()
    password.clear()
    username.send_keys(user)
    sleep(3)
    password.send_keys(passw)
    sleep(3)

    log_in = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
    sleep(2)
    skip = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Lúc khác')]"))).click()


    searchbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Tìm kiếm']")))
    searchbox.clear()
    searchbox.send_keys(keyword)
    sleep(5)
    #searchbox.send_keys(Keys.ENTER)
    #sleep(1)
    #searchbox.send_keys(Keys.ENTER)
    my_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/" + keyword[1:] + "/')]")))
    my_link.click()

    #Scroll down the page
    n_scrolls = 2
    for j in range(0, n_scrolls):
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        sleep(5)
    #target all the link elements on the page
    anchors = driver.find_elements_by_tag_name('a')
    anchors = [a.get_attribute('href') for a in anchors]
    #narrow down all links to image links only
    anchors = [a for a in anchors if str(a).startswith("https://www.instagram.com/p/")]
    print('Found ' + str(len(anchors)) + ' links to images')
    print(anchors[:5])

    images = []
    #follow each image link and extract only image at index=1
    for a in anchors:
        driver.get(a)
        sleep(5)
        img = driver.find_elements_by_tag_name('img')
        img = [i.get_attribute('src') for i in img]
        images.append(img[1])

    #Save images to computer
    path = os.getcwd()
    path = os.path.join(path, keyword[1:] + "s")
    os.mkdir(path)
    counter = 0
    for image in images:
        save_as = os.path.join(path, keyword[1:] + str(counter) + '.jpg')
        wget.download(image, save_as)
        counter += 1

if __name__ == '__main__':
    user = 'lauthaichuacay__'
    passw = 'huynguyen1801'
    url = 'https://www.instagram.com/'
    keyword = "#cat"
    log_in(user, passw, url, keyword)