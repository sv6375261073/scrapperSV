"""
# Author Shivam Vishwakarma 
# sv6375261073@gmail.com
"""

import requests
from PIL import Image
import urllib
from bs4 import BeautifulSoup
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time,os
import matplotlib.pyplot as plt


# In[5]:


def insta_profile(chromedriver_path,id_name):
    """
    Chromedriver must be downloaded into device 
    1 chromedriver_path
    2 instagram_profile id_name
    """
    query='https://www.instagram.com/'+id_name+'/'
    browser=webdriver.Chrome(chromedriver_path)
    browser.get(query)
    total_urls=[]
    print("Retrieving ..............")
    n_posts=int(browser.find_element_by_class_name('g47SY ').text)
    iteration=0
    while iteration<=n_posts//24+1:
        page=browser.page_source
        soup=BeautifulSoup(page,'lxml')
        tags=soup.find_all('img',class_='FFVAD')
        track=tags[-1]['src']
        if track not in total_urls:
            total_urls.extend(tags)
        try:
            browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(2)
            iteration+=1
        except:
            exit()
    print("Started downloading .........")
    total_urls=set(total_urls)
    for i,url in enumerate(total_urls):
        image=Image.open(urllib.request.urlopen(url['src']))
        try:
            caption=url['alt']
        except:
            caption='No caption'
        try:
            image.save(id_name+'/'+caption[:20]+str(i)+'.jpg')
        except:
            os.makedirs(id_name)
            image.save(id_name+'/'+caption[:20]+'.jpg')
#         print(i)
    return total_urls


# In[8]:


# if __name__=='__main__':
#     try:
#         urls=scrape_images()
#     except:
#         pass
#urls=scrape_images(id_name)


# # image uploder on instagram

# In[66]:


# from instabot import Bot 

# bot = Bot() 
# try:
#     bot.login(username = "+919530450649", password = "Shivam@271882Natural_beauty")
# except:
#     pass
# for img in os.listdir('instagram_images'):
#     image='instagram_images'+'/'+img
#     bot.upload_photo(image, caption ="How cute she is")





