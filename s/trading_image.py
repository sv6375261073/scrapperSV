"""
# Author Shivam Vishwakarma 
# sv6375261073@gmail.com

"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver   
import imageio
import requests,os
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.support.select import Select
import time     
from bs4 import BeautifulSoup
import lxml
from PIL import Image
import urllib
import numpy as np
sleep_time=2

def searchByinputBox(browser,sleep_time,name='RELIANCE'):
    search=browser.find_element_by_class_name('input-3lfOzLDc')
    search.send_keys(Keys.CONTROL + "a")
    search.send_keys(name) 
    search.send_keys(Keys.ENTER)

def search_name(browser,sleep_time,name='RELIANCE'):#search_class:'input-3lfOzLDc'
    try:
        browser.find_element_by_xpath('//*[@id="header-toolbar-symbol-search"]/div/input').click()
        search=WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, 'search-1t76YXcC')))
        browser.implicitly_wait(sleep_time)
        search.send_keys(Keys.CONTROL + "a") # select all text of input area to replace
        browser.implicitly_wait(sleep_time)
        search.send_keys(name) 
        search.send_keys(Keys.ENTER) # Enter to submit to search name of stock
    except:
        try:
            searchByinputBox(browser,sleep_time,name)
        except:
            browser.quit() 
#browser.implicitly_wait(sleep_time)

def period(browser,t='hour'):
    timet={'minute':8,'hour':16,'day':22,'week':23,'month':24}
    browser.implicitly_wait(sleep_time)
    element=WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="header-toolbar-intervals"]')))
    element.click()
    browser.implicitly_wait(sleep_time)
    browser.find_element_by_xpath('//*[@id="overlap-manager-root"]/div/span/div[1]/div/div/div/div[{}]/div/div[1]/div'.format(timet[t])).click()

def save_image(browser,name):
    if not os.path.exists('images'):
        os.makedirs('images')
    try:
        time.sleep(sleep_time)
        WebDriverWait(browser,20).until(EC.element_to_be_clickable((By.CLASS_NAME,'scrollRight-2SEqCpTf'))).click()
        time.sleep(sleep_time)
        browser.find_element_by_xpath('//*[@id="header-toolbar-screenshot"]/span').click()
        link=browser.find_element_by_xpath('//*[@id="overlap-manager-root"]/div/div/div[2]/div/div/div[1]/div[2]/div/div/div[2]/a')
        link.click()
        browser.switch_to.window(browser.window_handles[-1])
        url=browser.current_url
    except:
        browser.quit()
    print("image_url : ",url)
    image=Image.open(urllib.request.urlopen(url))
    image = Image.fromarray(np.array(image))
#     try:
    img_name='images/{}-{}.png'.format(name,len(os.listdir('images'))+1)
    image.save(img_name)
#     except:
#         image.save(img_name)
    browser.quit()
    return img_name    

        
def trade(chromedriver_path,name,t='month'):
    """
    Chromedriver must be downloaded into local device 
    1 chromedriver_path
    2 Stock symbol name ex:reliance,sbin,axisbank
    3: month,hour,week,minute
     
    """
    global sleep_time
    URL = 'https://tradingview.com/chart/'      
    browser = webdriver.Chrome(chromedriver_path) 
    browser.get(URL)
    #time.sleep(sleep_time)
    search_name(browser,sleep_time,name)
    period(browser,t='hour')
    img_name=save_image(browser,name)
    return img_name
