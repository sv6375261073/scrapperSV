"""
# Author Shivam Vishwakarma 
# sv6375261073@gmail.com
"""

import requests 
from bs4 import BeautifulSoup 
import pandas as pd
import re

# finding url in page
def url_fetch(table):
    links=set()
    for txt in table:
        content=re.findall('https.*',str(txt))
        content=content[0].split("title")[0].replace("\"","").strip()
        links.add(str(content))
    return links
# retrieving url from page
def retrieve_url():
    counter=1
    total_links=[]
    while counter !=249:
        print("Trying to access data of page "+str(counter))
        URL = "https://www.altnews.in/page/"+str(counter)+"/"
        r = requests.get(URL) 
        soup = BeautifulSoup(r.content, 'html.parser') 
        table = soup.find_all('a',attrs={'href'},class_='herald-read-more')
        total_links.append(url_fetch(table))
        counter+=1
    print("Total links found : {} ".format(len(total_links)))
    return total_links


def txt_reterive(text):
    if re.findall('“.*',text) !=-1:
        text=' '.join([t.split('”')[0] for t in re.findall('“.*',text)])
        return text
    else:
        return ''
# synchronize data 
def altnews():
    df=pd.DataFrame(columns=['title','link','date','text','category'])
    count=0
    urls=retrieve_url()
    urls=[url for url_set in urls for url in url_set]
    for url in urls:
        url=str(url).replace('\n','')
        r = requests.get(url) 
        soup = BeautifulSoup(r.content, 'html.parser')
        all_text =soup.find_all('p')
        date=soup.find("span",class_="updated")
        date=date.text
        title=soup.find('h1',class_="entry-title h1")
        title=title.text
        for txt in all_text:
            txt=txt_reterive(txt.text)
            if len(txt)>50:
                df.loc[count]=[title,url,date,txt,'fake']
                print("Writing Row {} data ".format(count))
                count+=1
    return df
#df=altnews()
#df.to_csv('altnews.csv')


# In[6]:




