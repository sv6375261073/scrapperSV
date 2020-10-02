"""
# Author Shivam Vishwakarma 
# sv6375261073@gmail.com
"""

from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait  
from selenium.webdriver.common.keys import Keys 
import time 


# In[4]:


def send_message(target,message,n=1):
    global driver
    input_block=driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div')
    for i in range(n):
        try:
            time.sleep(1)
            input_block.send_keys(Keys.CONTROL+'a')
            time.sleep(2)
            input_block.send_keys(message)
            send_button=driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button/span').click()
        except:
            time.sleep(1)


# In[ ]:



def whatsapp(chromedriver_path):
    """
    1 Chromedriver_path
    """
    driver = webdriver.Chrome(chromedriver_path) 
    driver.get("https://web.whatsapp.com/")
    agreement=input('did you scanned your web.whatsapp QR code y/n')
    if agreement =='y':
        while True:
            target=input("Enter receiver name : ")
            message=input("Enter message : ")
            n=int(input("Enter no. of time : "))
            try:
                time.sleep(2)
                search=driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
                search.send_keys(target)
                time.sleep(2)
                search.send_keys(Keys.ENTER)
                send_message(target,message,n)
            except:
                print('receiver name does not exist in your contact ')
                try:
                    page=driver.current_url
                    print(target+" does not exist in your account ")
                except:
                    print('Web.whatsapp.com closed ')
                    return
#try:                    
#    start()
#except:
#    pass




