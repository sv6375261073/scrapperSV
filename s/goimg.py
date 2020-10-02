"""
# Author Shivam Vishwakarma 
# sv6375261073@gmail.com
"""

from PIL import Image
import urllib
from bs4 import BeautifulSoup
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time,os


# In[7]:


total_urls=[]
titles=[]
# Saving all exteracted images 

def save_images(urls,titles,query):
    image=[]
    if not os.path.exists(query): # check existence of file 
        os.makedirs(query)
#     n=int(input(" Enter no of titles to download out of "+str(len(urls))+"  : ")) # n topic download 
    for title,urllist in zip(titles[:1],urls[:1]):
        if title !='Home':
            title=str(title['aria-label']) # naming folder based on topic on google 
        print('Downloading  : '+title+' under '+query)
        for i,url in enumerate(urllist):
            if not os.path.exists(query+'/'+title):
                os.makedirs(query+'/'+title)
            try:
                image=Image.open(urllib.request.urlopen(url['src'])) # opening url of image 
            except:
                try:
                    image=Image.open(urllib.request.urlopen(url['data-src']))
                except:
                    pass
            if len(np.array(image))>0:
                try:
                    image.save(query+'/'+title+'/'+url['alt']+str(i)+'.png') # saving image into topic folder 
                except:
                    pass
        print("Saved image : "+str(i))
        
                
# scrolling and going upto last image then scrapping all urls of images 
def images(browser):  # scroll upto end of page for any topic of image 
    found=1
    while(found):
        try:
            count=0
            while(count<6): # button show more results n page consist upto 6 scroll 
                try:
                    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
                    time.sleep(5)
                except:
                    pass
                count+=1
            time.sleep(3)
            browser.find_element_by_class_name('mye4qd').click() # clicking on show more results 
            time.sleep(5)
        except:
            found=0
    soup=BeautifulSoup(browser.page_source,'lxml')
    img_urls=[img for img in soup.find_all('img',class_='rg_i Q4LuWd')]
    return img_urls
def clean_garbage_files(query): # cleaning all which are not image from directory 
    root=query
    for folder in os.listdir(root):
        for image in os.listdir(root+'/'+folder):
            if os.stat(root+'/'+folder+'/'+image).st_size <=1:
                try:
                    os.remove(root+'/'+folder+'/'+image)
                except:
                    pass

# Accessing all urls available for given input 
def find(chromedriver_path,query='flower'):
    global titles  # taking title and total_urls as global so interuption cannot affect retrieved urls 
    global total_urls
    browser=webdriver.Chrome(chromedriver_path)  # open webdriver file available in device for chrome
    browser.get('https://www.google.com/')
#   browser.fullscreen_window()
    search=browser.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')#google input automation
    search.send_keys(query+' image')
    time.sleep(1)
    search.send_keys(Keys.ENTER)
    time.sleep(1)
    browser.find_element_by_class_name('Q2MMlc').click()  # clicking so more results for input query on google images
    time.sleep(1)
#   Accessing image home page base
    titles.append('Home') # for home url 
    total_urls.append(list(set(images(browser)))) # appending all topics available on google 
    soup=BeautifulSoup(browser.page_source,'lxml') # scrapping all urls on home page
    titles.extend([link for link in soup.find_all('a',class_='F9PbJd IJRrpb xKddTc')])
    browser.close()
#   Accessing images topic based 
    for url in titles[1:]:  # for retriving all topics url 
        browser=webdriver.Chrome('./chromedriver')
        browser.get('https://www.google.com'+url['href'])
#       browser.fullscreen_window()
        time.sleep(1)
        total_urls.append(list(set(images(browser))))
        browser.close()
    print("Categories found : "+str(len(total_urls)))
    browser.close()


# In[8]:


def google_image(chromedriver_path,query):
    """Required chromedriver downloaded in the local device
    1 param: chromedriver_path
    2 query: image name 
    """
#     query=input()
    try:
        find(chromedriver_path,query)
    except:
        pass
    save_images(total_urls,titles,query)
    clean_garbage_files(query)
#google_image('Ascending triangle')


# In[ ]:





# In[ ]:





# In[ ]:





# In[3]:


# query='flower'
# browser=webdriver.Chrome('./chromedriver')
# browser.get('https://www.google.com/')
# search=browser.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
# search.send_keys(query+' image')
# time.sleep(1)
# search.send_keys(Keys.ENTER)
# time.sleep(3)
# browser.find_element_by_class_name('Q2MMlc').click()
# time.sleep(3)
# soup=BeautifulSoup(browser.page_source,'lxml')
# titles=[link['href'] for link in soup.find_all('a',class_='F9PbJd IJRrpb xKddTc')]
# total_urls=[]
# for url in titles:
#     browser=webdriver.Chrome('./chromedriver')
#     browser.get('https://www.google.com'+url)
#     time.sleep(3)
#     total_urls.extend(images(browser))
#     browser.close()


# In[ ]:





# In[ ]:





# In[ ]:




