import requests as rq

import pandas as pd

from bs4 import BeautifulSoup

from bs4 import NavigableString

mUrl = 'https://www.commonsensemedia.org/lists/bollywood-movies'

mHeader = {
   'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
}

mResp = rq.get(url= mUrl, headers= mHeader)

# print(mResp.status_code)

bSoup = BeautifulSoup(mResp.content,'html.parser')

# print(bSoup)

# allDiv = bSoup.find_all('div',{'class':'review-info'}) # without including url data
# print(allDiv)

allDiv = list(bSoup.find_all('div',{'class':'review-teaser'})) # including url data
# print(allDiv)

# url = bSoup.find('div',{'class' : 'review-image'}).find('a').get('href')
# print(url)

# title = bSoup.find('h3',{'class':'review-title'}).find('a').getText()
# print(title)

# discription = bSoup.find('p',{'class':'review-one-liner'}).getText()
# print(discription)

movieData = []


for i in allDiv:
    Title = i.find('h3',{'class':'review-title'}).find('a').getText()
    Discription = i.find('p',{'class':'review-one-liner'}).getText()
    url = i.find('div',{'class' : 'review-image'}).find('a').get('href')


    movieData.append({
        'Title' : Title,
        'Discription' : Discription,
        'URL' : url
    })

print(movieData)

# movieData = pd.DataFrame(movieData)

# movieData.to_csv('MovieData.csv')




