import pandas as pd
import requests
from bs4 import BeautifulSoup
#url = 'https://www.fragrancenet.com/perfume'
for i in range(1, 5):
    url = "https://www.fragrancenet.com/ni/fragrances?f=1f!3D/1f!6R/1f!do?&page="+ str(i)
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'lxml')
    allDivs = soup.findAll('div',attrs= {'class' : 'resultItem heightSync'})
    print('number of perfumes : ',len(allDivs))
    print('--------------')
    for div in allDivs:
        link= div.find('a')
        linktoperfume = link.get('href')
       
       
       
       
        name = div.find("span", {"itemprop" : "name"}).text
        rating =div.find('div',{'class':'starRating'})["data-score"]
        secondDiv = div.find("div")
        pTag_brand = secondDiv.find('p',{'class':'des'})
        if(pTag_brand):
            brand = pTag_brand.find('a').text
        else:
            brand = secondDiv.find('a').text
        pTag_cat=secondDiv.find('p',{'class':'desc'})
        category = pTag_cat.find('a').text
        itag_women = secondDiv.find('i',{'class':'gender_womens'})
        itag_unisex = secondDiv.find('i',{'class':'gender_unisex'})
        itag_men = secondDiv.find('i',{'class':'gender_mens'})
        if(itag_women):
            gender = 'women'
        elif(itag_unisex):
            gender = 'unisex'
        elif(itag_men):
            gender = 'men'

        res1 = requests.get(linktoperfume)
       
        soup2= BeautifulSoup(res1.content, 'lxml')
        thirdDiv = soup2.findAll('div',{'class' : 'tab-content'})
        for div in thirdDiv:
            Notes= None
            recommendedTime= None
            Year= None
            if(div.find('ul',{'class':'notes cf' })):
                notesDiv= div.find('ul',{'class':'notes cf' })
                for li in notesDiv.findAll('li'):
                    if li.findAll('span')[0].text=="Fragrance Notes:":
                        Notes = li.findAll('span')[1].text
                    if li.findAll('span')[0].text=="Recommended Use:":
                        recommendedTime = li.findAll('span')[1].text
                    if li.findAll('span')[0].text=="Year Introduced:":
                        Year = li.findAll('span')[1].text
            
            if(div.findAll('div',{'class': 'review'})):
                reviews =div.findAll('div',{'class': 'review'})
                for review in reviews:
                    print (review.find('p',{'class': 'text'}).text)
                    print (review.find('div',{'class': 'starRating'})["data-score"])

       
       
        print('--> Brand : ',brand)
        print('--> Category : ',category)
        print('--> Perfume Name : ',name)
        print('--> Rating : ',rating)
        print('--> Gender : ',gender)
        print('--> Link : ',linktoperfume)
        print('--> Notes : ',Notes)
        print('--> Recommended time : ',recommendedTime)
        print('--> Year Introduced: : ',Year)
        print ("------------------")
