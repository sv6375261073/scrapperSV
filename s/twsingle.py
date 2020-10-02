"""
# Author Shivam Vishwakarma 
# sv6375261073@gmail.com
"""

import requests 
from bs4 import BeautifulSoup 
    
def twit_post(url):
    URL=url.replace('twitter.com','mobile.twitter.com')
    print('Trying with : {}'.format(URL))
    text,image,url='','',''
    with requests.Session() as session:
        try:
            r = requests.get(URL) 
            soup = BeautifulSoup(r.content, 'html.parser')
            text=soup.find('div',attrs={'class':"dir-ltr"})
            text_val=text.text
            url= str(text).split('data-url="')[1].split('"')[0]
            image=soup.find('div',attrs={'class':"media"}).find('img')
            image=str(image).split('src="')[1].split(':small')[0]
        except :
            pass
    return text_val,image,url
#url=input()
#text,image,url=Twitter_scrape(url)
#print(text)
#print(image)
#print(url)
