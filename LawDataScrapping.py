#!/usr/bin/env python
# coding: utf-8

# In[67]:


from selenium import webdriver
import urllib,re  
from selenium.webdriver.support.select import Select
import time     
from bs4 import BeautifulSoup
import pandas as pd
import PyPDF2 as pdf
import lxml
sleep_time=1


# In[66]:


def pdf2text():
    pdfFileObj = open('Lawfile.pdf', 'rb')
    pdfReader = pdf.PdfFileReader(pdfFileObj)
    pagenum=pdfReader.numPages
    text=''
    for i in range(pagenum):
        pageObj = pdfReader.getPage(i)
        text+=' '+pageObj.extractText() 
    pdfFileObj.close()
    return text


# In[65]:


def Home(name='Administration'):
    # uploading chromedrive file 
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications" : 2}
    chrome_options.add_experimental_option("prefs",prefs)
    browser = webdriver.Chrome('./chromedriver',chrome_options=chrome_options)

    # openning URL in chromedriver 
    URL='https://caselaw.findlaw.com/summary/search'
    browser.get(URL)
    browser.maximize_window()

    # Preparing Home page scrapeable 
#     time.sleep(sleep_time)
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight / 4)')
    time.sleep(sleep_time)
    select=Select(browser.find_element_by_name('topic'))
    time.sleep(sleep_time)
    soup=BeautifulSoup(browser.page_source,'lxml')
    legal_name={i:[optiontag['value'],optiontag.text] for i,optiontag in enumerate(soup.find('select',attrs={'id':'topic'}).find_all('option')[1:])}
    print(legal_name)
    n=int(input('Select a LawName key in integer : '))
    select.select_by_value(legal_name[n][0])
    url=f'https://caselaw.findlaw.com/summary/search/?query=filters&dateFormat=yyyyMMdd&topic={legal_name[n][0]}&pgnum=1'
    browser.get(url)
    return browser


# In[64]:


def parse_data(raw_html):
    label=raw_html.find('i').text
    desc=raw_html.find('div',attrs={'class':'desc_subttl'}).text
    link=raw_html.find('a')['href']
    date=raw_html.find_all('td')[-2].text
    return [desc,link,date,label]

def scrape_text(browser,url):
    try:
        browser.window_handles[1]
    except Exception as e:
        browser.execute_script("window.open('');")
    browser.switch_to.window(browser.window_handles[1])
    browser.get(url)
    status=browser.find_element_by_class_name('caselawcontent').text
    time.sleep(sleep_time)
    tinybtn=browser.find_element_by_link_text('READ').click()
    time.sleep(sleep_time)
    text=''
    try:
        herebtn=browser.find_element_by_link_text('here')
        herebtn.click()
        browser.switch_to.window(browser.window_handles[2])
        url=browser.current_url
        file = urllib.request.urlopen(url)
        pdffile = open('Lawfile.pdf', 'wb')
        pdffile.write(file.read())
        text=pdf2text()
    except Exception as e:
        try:
            text=browser.find_element_by_class_name('caselawcontent').text
        except Exception as e:
            print(e)
#     browser.close()
    browser.switch_to.window(browser.window_handles[1])
    return text,status
statusLabel=['affirmed','held','remanded','vacated','denied','reversed','dismissed','vacated and remanded',
             'revived','revised','vocated and affirmed','reverse,remanded,affirmed','affirmed,reversed',
             'reaffirmed','reanded,reversed','rejected']

def findStatus(text):
    text=text.lower()
    text=re.sub("[\W]",' ',text)
    print(text)
    sLabels =[sl for sl in statusLabel if text.find(sl)>=0]
    if len(sLabels)>1:
        return ' and '.join([slr for slr in set(sl for l in sLabels for sl in l.split()) if slr in statusLabel])
    return sLabels[-1]

def ScrapeLinksAndSaveData(browser):
    global counter
    soup=BeautifulSoup(browser.page_source,'lxml')
    fileLinks=soup.find_all('tr')
    for i in range(1,len(fileLinks)):
        trlst=parse_data(fileLinks[i])
        text,status=scrape_text(browser,trlst[1])
        status=findStatus(status)
        trlst.extend([text,status])
        df.loc[counter]=trlst
        counter+=1
    if len(df)%10==0:
        df.to_csv('Law.csv')
        print('Check point created at dataframe length :  {}'.format(len(df)))
        


# In[68]:


df=pd.DataFrame(columns=['Description','Url','Date','Label','Text','Status'])
counter=0
browser=Home()
totalPages=int(browser.find_element_by_class_name('pagination').text.split('\n')[-2])
pages=1


# In[78]:



while pages!=totalPages:
    try:
        ScrapeLinksAndSaveData(browser)
    except Exception as e:
        print(e)
    browser.switch_to.window(browser.window_handles[0])
    nexturl=browser.current_url
    nexturl=nexturl.split('pgnum=')
    nexturl=nexturl[0]+'pgnum='+str(int(nexturl[1])+1)
    browser.get(nexturl)
    try:
        browser.execute_script('window.scrollTo(0, document.body.scrollHeight)/4')
    except Exception as e:
        pass
    pages+=1


# In[71]:


df.to_csv('Law.csv')


# In[72]:


df


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


# chrome_options = webdriver.ChromeOptions()
# prefs = {"profile.default_content_setting_values.notifications" : 2}
# chrome_options.add_experimental_option("prefs",prefs)
# browser = webdriver.Chrome('./chromedriver',chrome_options=chrome_options)

# URL='https://caselaw.findlaw.com/summary/search'

# browser.get(URL)
# browser.maximize_window()
# time.sleep(sleep_time)
# browser.execute_script('window.scrollTo(0, document.body.scrollHeight / 4)')
# time.sleep(sleep_time)
# select=Select(browser.find_element_by_name('topic'))
# time.sleep(sleep_time)
# select.select_by_value('cs_1')
# time.sleep(sleep_time)
# searchbtn=browser.find_element_by_class_name('primary')
# searchbtn.click()
# time.sleep(sleep_time)
# ttlbtn=browser.find_element_by_link_text('Lockett v. Bonson').click()
# time.sleep(sleep_time)
# tinybtn=browser.find_element_by_link_text('READ').click()
# time.sleep(sleep_time)
# herebtn=browser.find_element_by_link_text('here')
# herebtn.click()
# browser.switch_to.window(browser.window_handles[1])
# url=browser.current_url
# file = urllib.request.urlopen(url)
# pdffile = open('Lawfile.pdf', 'wb')
# pdffile.write(file.read())
# file.close()
# browser.quit()

