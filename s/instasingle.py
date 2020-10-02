"""
# Author Shivam Vishwakarma 
# sv6375261073@gmail.com
"""

import requests 
from bs4 import BeautifulSoup 
def insta_post(url):
    URL=url
    print('Trying with : {}'.format(URL))
    text,image='',''
    with requests.Session() as session:
        r = requests.get(URL) 
        soup = BeautifulSoup(r.content, 'html.parser')
        json_data=soup.find('script',attrs={'type':"application/ld+json"})
        try:
            lst=list(json_data.children)
            lst=lst[0].replace('\n','').strip()
            json_=json.loads(lst)
#             print(json_)
            text=json_['caption']
            url=json_['mainEntityofPage']['@id']
        except:
            text=soup.title.text
        lst_str=soup.find('meta',attrs={'property':"og:image"})
        image=str(lst_str).split('" property="og:image"')[0].split('<meta content="')[1].strip().replace('amp;','')
    return text,image


# In[2]:


# url=input()
# Instagram_scrape(url)


# In[ ]:





# In[ ]:




