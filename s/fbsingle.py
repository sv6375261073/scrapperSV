"""
# Author Shivam Vishwakarma 
# sv6375261073@gmail.com
"""

import requests 
from bs4 import BeautifulSoup 
import pandas as pd
import re


# In[2]:


def fb_post(URL):
    r = requests.get(URL) 
    soup = BeautifulSoup(r.content, 'html.parser')
    meta=soup.find_all('meta')
    if len(meta)<8:
        raise Exception('Something Went Wrong !!')
    else:
        for i,j in enumerate(meta):
            if i==6 and str(j).find("og:description"):
                desc=str(j).split('"')[1].replace('\n','').replace('  ',' ')
            elif i==7 and str(j).find("og:image"):
                image=str(j).split('"')[1]
                image=str(image).replace('amp;','')
            elif i==8 and str(j).find("og:url"):
                url=str(j).split('"')[1]
                url=str(url).replace('amp;','')
    return desc,image,url


# In[4]:


# url=input()#'http://www.facebook.com/story.php?story_fbid=3224814467564560&id=1389683114411047&scmts=scwspsdd&extid=mDJbnuN6JNvWLD6J'
# desc,image,url=fb_scrape(url)


# In[5]:


# print(desc)
# print(image)
# print(url)


# In[ ]:


# from selenium import webdriver 
# from time import sleep 
# from webdriver_manager.chrome import ChromeDriverManager 
# from selenium.webdriver.chrome.options import Options 

# usr=input('Enter Email Id:') 
# pwd=input('Enter Password:') 

# driver = webdriver.Chrome(ChromeDriverManager().install()) 
# driver.get('https://www.facebook.com/') 
# print ("Opened facebook") 
# sleep(1) 

# username_box = driver.find_element_by_id('email') 
# username_box.send_keys(usr) 
# print ("Email Id entered") 
# sleep(1) 

# password_box = driver.find_element_by_id('pass') 
# password_box.send_keys(pwd) 
# print ("Password entered") 

# login_box = driver.find_element_by_id('loginbutton') 
# login_box.click() 

# print ("Done") 
# input('Press anything to quit') 
# driver.quit() 
# print("Finished") 

