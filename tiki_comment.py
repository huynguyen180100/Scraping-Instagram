from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException
#from selenium.webdriver.common.keys import Keys
import os
import requests
def init_browser(url):
    global browser
    browser = webdriver.Chrome(executable_path= './chromedriver')
    browser.get(url)
    sleep(3)
    list_review = []
    x = 0
    while x<10:
        try:
            WebDriverWait(browser,5).until(EC.visibility_of_all_elements_located(By.CSS_SELECTOR, "div.style__StyledCustomerReviews-sc-103p4dk-0 jUzqeQ customer-reviews"))
        except:
            print('No comment for this product')
            break
        product_reviews = browser.find_elements_by_css_selector('[class="customer-reviews__inner"]')
            #Get product review
        for product in product_reviews:
            review = product.find_elements_by_css_selector('[class="review-comment__content"]').text
            if(review!="" or review.strip()):
                print(review, "\n")
                list_review.append(review)

        try:
            button_next = WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'class="btn"')))
            browser.execute_script("arguments[0].click();", button_next)
            print("Next page")
            sleep(2)
            x += 1
        except(TimeoutException, WebDriverException) as e:
            print('Load several page')
            break
    #browser.close()
    return list_review

if __name__ == '__main__':
    url = 'https://tiki.vn/apple-macbook-air-2020-m1-13-inchs-apple-m1-16gb-256gb-hang-chinh-hang-p88231354.html?src=ss-organic'
    sleep(5)
    init_browser(url)
    sleep(2)