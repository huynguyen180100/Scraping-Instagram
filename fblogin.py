from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
import wget

def log_in(user, passw, url):
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    global driver
    driver = webdriver.Chrome(executable_path = "./chromedriver", chrome_options=chrome_options)
    driver.get(url)
    sleep(2)
    print('Initial browser')
    #Login
    username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='email']")))
    password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='pass']")))
    username.clear()
    username.send_keys(user)
    sleep(2)
    password.clear()
    password.send_keys(passw)
    sleep(2)
    #target the button and click it
    button = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
    print('Login successful')
    #Click photo
    #https://www.facebook.com/congchualuumanh235/photos_all

    sleep(5)
    images = []
    for i in ['photos_all', 'photos_albums']:
        driver.get('https://www.facebook.com/congchualuumanh235/' + i +"/")
        sleep(5)
        for j in range(0,1):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(10)
        # target all the link elements on the page
        anchors = driver.find_elements_by_tag_name('a')
        anchors = [a.get_attribute('href') for a in anchors]
        # narrow down all links to image links only
        anchors = [a for a in anchors if str(a).startswith("https://www.facebook.com/photo")]
        #print(anchors)
        print('Found ' + str(len(anchors)) + ' links to images')
        for a in anchors:
            driver.get(a)  # navigate to link
            sleep(5)  # wait a bit
            img = driver.find_elements_by_tag_name("img")
            images.append(img[3].get_attribute("src"))  # may change in future to img[?]
            #for k in img:
                #print(k.get_attribute("src"))

    print('I scraped ' + str(len(images)) + ' images!')
    #print(images)
    #'''''
    #save img
    path = os.getcwd()
    path = os.path.join(path, "Crawl_Img")
    # create the directory
    os.mkdir(path)

    counter = 0
    for image in images:
        save_as = os.path.join(path, str(counter) + '.jpg')
        wget.download(image, save_as)
        counter += 1
    #'''''
if __name__ == '__main__':
    url = 'https://www.facebook.com'
    user = '0923689987'
    passw = 'maiminhxa'
    log_in(user, passw, url)
    #sleep(10)
   # driver.close()