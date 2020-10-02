# Author: Shivam Vishwakarma

### Scrapping

1 Altnews.com scrapping
2 Google Image Scrapping 
3 Instagram user profile scrapping based on username
4 Instagram single post scrapping based on link
5 Facebook post scrapping based on postlink
6 Twitter post scrapping based on link
7 Tradingview chart image scrapping
8 Whatsapp messaging using whatsappweb 

***************************************************************
 1 ALTNEWS

 This is a Indian fact news checking site. this package is helpful to scrape all data and create a dataframe 
 of every article which is available on site .
  data includes:
	Text
	Author name
	Date
	Title
	Link
***************************************************************
2 Google Image Downloader

 In this module you can scrape all images based on given image name . Basically it takes a few minutes to scrape all imaes . it iterates 
  over all image sub categories and scrape them . This is very useful for making dataset of difficult images dataset .
	Required only name of image 

***************************************************************
3 Instagram user profile scrapping

  Scrape a whole user profile images based on instagram userid just need userid .

***************************************************************
4 Scrapping instagram posts

This is helpful to scrape data related to a instagram post . shared link of post.

***************************************************************
5 Scrapping Facebook post

This is related to scrape post of the faceebook based on shared link of facebook post .

***************************************************************
6 Scrapping Twitter post

 Just get the shareable link of twitter post . Use that as a url to the function and it will return data related to posts .

***************************************************************
7 Scrapping trading view image chart

  This is to save image of the tradingview chart based on symbol,timeinterval . THis is helpful to make dataset for trading projects .

***************************************************************
8 Whatsapp messaging

  Here we can send messages to existing friends in the user accout . This is based on whatsapp web . Just need to scan whatsapp QR code and start to message to the friends . You can send a messages n no. of times .
 Ex:
     target='varsha'
     message='Hi'
     n=10
 Then it will send message Hi 10 times to varsha .

 
	 

# Importing scrapperShivam 


```python
***************************************************************

from scrapper import scrape

***************************************************************
```

# 1 # Altnews.com 


```python
***************************************************************

#1 Scrapping full Fake News dataset from altnews.com

scrape.altnews()

***************************************************************
```

# 2 # scrape fb_post


```python
***************************************************************

# Scrapping facebook post based on fb_url

url="""http://www.facebook.com/story.php?story_fbid=1465359780314951&id=100005228298088&scmts=
scwspsdd&extid=zIROvP0jkc3UkapK"""

text,image,url=scrape.fb_post(url)

# Facebook shared link of post 

***************************************************************
```




    ('मेरे द्वारा एक निजी इंजीनियरिंग कॉलेज के फेसबुक पेज पर खुद के वेतन और संस्था की सच्चाई पूर्ण विनम्रता के साथ कॉमेंट बॉक्स में लिखी थी तो कॉलेज प्रशासन ने उसे हटा दिया और सभी स्टाफ मेंबर से बोला है कि...',
     'https://scontent.fixc7-1.fna.fbcdn.net/v/t1.0-9/116582208_1465359653648297_6414823970251708469_o.jpg?_nc_cat=103&_nc_sid=110474&_nc_ohc=dAOYaJ52M2oAX-GH2UF&_nc_ht=scontent.fixc7-1.fna&oh=a5e88e7ad2018bb1764f2c97b2caa9f9&oe=5F9ACA07',
     'https://www.facebook.com/permalink.php?story_fbid=1465359780314951&id=100005228298088')



# 3 # scrape image from google


```python
***************************************************************

# scrapping all images from google based on image name 

scrape.google_image('./chromedriver','football')

# param1 : chromedriver_path
# param 2 : image name to download

***************************************************************
```

# 4 # Instagram scrape post


```python
***************************************************************

# Instagram post scrapping based on link 

insta_post_url='https://www.instagram.com/p/CFy6m47lFJi/?utm_source=ig_web_button_share_sheet'
text,image=scrape.insta_post(insta_post_url)

# param 1 : instagram shared post url

***************************************************************
```

    Trying with : https://www.instagram.com/p/CFy6m47lFJi/?utm_source=ig_web_button_share_sheet





    ('\nAmbivert परिंदा 🦋 (@curlicious_memer) posted on Instagram: “Paisa barbaad bc ..ab lagta Whitehat jr. p hi registration krna pdega 😕😂 Follow @curlicious_memer for more . . . . . . #softwareengineer…” • Oct 1, 2020 at 9:16am UTC\n',
     'https://instagram.fixc7-1.fna.fbcdn.net/v/t51.2885-15/e35/120477874_330305014963377_8160288912634310107_n.jpg?_nc_ht=instagram.fixc7-1.fna.fbcdn.net&_nc_cat=109&_nc_ohc=lesd4rVgfMAAX_z-3yo&_nc_tp=18&oh=5fcfd512ef4c3dbb88fbbe181f2bea3b&oe=5FA1AFA0')



# 5 # Scrape Insta profile 


```python
***************************************************************

# scrapping all images of a insta user profile

scrape.insta_profile('./chromedriver','shivamthevirus')

# param 1 : Chromedriver_path 
# param 2 : instagram profile username

***************************************************************
```

    Retrieving ..............
    Started downloading .........


# 6 # Scrape chart image from tradingview


```python
***************************************************************

# scrapping chart image from tradingview.com based on symbol and time interval 

scrape.trade('./chromedriver','reliance',t='month') #t=month/minute/hour/week/
# param1 : chromedriver_path
#param2 : stock symbol name
# param3 : time_interval

***************************************************************
```

    image_url :  https://www.tradingview.com/x/WVWuMkqj/





    'images/reliance-2.png'



# 7 # Scrapping Post from twitter link 


```python
***************************************************************

twit_url='https://twitter.com/rashtrapatibhvn/status/1311647175747592198?s=20'
text.image,url=scrape.twit_post(twit_url) 

# param1 : shared link of facebook_post

***************************************************************
```

    Trying with : https://mobile.twitter.com/rashtrapatibhvn/status/1311647175747592198?s=20





    ('  आज मेरे जन्मदिन पर मुझे अनेक शुभकामना सन्देश प्राप्त हुए हैं। इसके लिए मैं हृदय से आभार व्यक्त करता हूं। आप सभी देशवासियों के स्नेह और सौहार्द से मुझे राष्ट्र की सेवा में तत्पर रहने की प्रेरणा व ऊर्जा प्राप्त होती है। आप सभी का बहुत-बहुत धन्यवाद!\n',
     '',
     '')



# 8 # messaging with web.whatsapp.com 


```python
***************************************************************
# scan web.whatsapp qrcode and give input y to continue
scrape.whatsapp('./chromedriver') 

#param 1 : chromedriverpath 

***************************************************************
```


```python

```


```python

```
