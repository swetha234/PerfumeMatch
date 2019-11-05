
#url = 'https://www.fragrancenet.com/perfume'
import pandas as pd
import requests
from bs4 import BeautifulSoup
import csv
import math

def getPerfumeData():
    perfume_id =0
    perfumeUrls = []
    with open('eg.csv', 'w', newline='') as csvfile:
        fieldnames = ['Id','Brand', 'Category', 'Name', 'Rating','Gender','Notes','Recommended Time','Year','Perfume Url']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(1, 364):
            print(i)
            url = "https://www.fragrancenet.com/ni/fragrances?f=1f!3D/1f!6R/1f!do?&page="+ str(i)
            res = requests.get(url)
            soup = BeautifulSoup(res.content, 'lxml')
            allDivs = soup.findAll('div',attrs= {'class' : 'resultItem heightSync'})
            for div in allDivs:
                perfume_id +=1
                link= div.find('a')
                linktoperfume = link.get('href')

                perfumeDict={}
                perfumeDict["id"]=perfume_id
                perfumeDict["url"]=linktoperfume
                perfumeUrls.append(perfumeDict)

                # name = div.find("span", {"itemprop" : "name"}).text
                # if (div.find('div',{'class':'starRating'})):
                #     rating =div.find('div',{'class':'starRating'})["data-score"]
                # else:
                #     rating =None

                # secondDiv = div.find("div")
                # pTag_brand = secondDiv.find('p',{'class':'des'})
                # if(pTag_brand):
                #     brand = pTag_brand.find('a').text
                # else:
                #     brand = secondDiv.find('a').text
                # pTag_cat=secondDiv.find('p',{'class':'desc'})
                # category = pTag_cat.find('a').text
                # itag_women = secondDiv.find('i',{'class':'gender_womens'})
                # itag_unisex = secondDiv.find('i',{'class':'gender_unisex'})
                # itag_men = secondDiv.find('i',{'class':'gender_mens'})
                # if(itag_women):
                #     gender = 'women'
                # elif(itag_unisex):
                #     gender = 'unisex'
                # elif(itag_men):
                #     gender = 'men'

                # res1 = requests.get(linktoperfume)
            
                # soup2= BeautifulSoup(res1.content, 'lxml')
                # thirdDiv = soup2.findAll('div',{'class' : 'tab-content'})
                # for div in thirdDiv:
                #     Notes= None
                #     recommendedTime= None
                #     Year= None
                #     if(div.find('ul',{'class':'notes cf' })):
                #         notesDiv= div.find('ul',{'class':'notes cf' })
                #         for li in notesDiv.findAll('li'):
                #             if li.findAll('span')[0].text=="Fragrance Notes:":
                #                 Notes = li.findAll('span')[1].text
                #             if li.findAll('span')[0].text=="Recommended Use:":
                #                 recommendedTime = li.findAll('span')[1].text
                #             if li.findAll('span')[0].text=="Year Introduced:":
                #                 Year = li.findAll('span')[1].text
                # writer.writerow({'Id': perfume_id, 'Brand': brand,'Category': category,'Name': name,'Rating': rating,'Gender': gender,'Notes': Notes,'Recommended Time':recommendedTime ,'Year':Year,'Perfume Url':linktoperfume})

    return perfumeUrls

def getReviews(perfumeUrls):
    with open('reviews.csv', 'w', newline='') as csvfile:
        fieldnames = ['Id','Review', 'Rating']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for perfumeUrl in perfumeUrls:
            print(perfumeUrl["id"])
            res1 = requests.get(perfumeUrl["url"])
            soup2= BeautifulSoup(res1.content, 'lxml')
            reviewCount = soup2.find('li', {"id": "reviewTab"}).text
            reviewCount = reviewCount.replace("Reviews", "")
            reviewCount =reviewCount.replace(" ", "")
            reviewCount =reviewCount.replace("(", "")
            reviewCount =reviewCount.replace(")", "")

            reviewPages= math.ceil(int(reviewCount)/5)
            thirdDiv = soup2.findAll('div',{'class' : 'tab-content'})

            for div in thirdDiv:
                if(div.findAll('div',{'class': 'review'})):
                    reviews =div.findAll('div',{'class': 'review'})
                    for review in reviews:
                        reviewText = review.find('p',{'class': 'text'}).text
                        if (review('div',{'class':'starRating'})):
                            reviewRating =review.find('div',{'class': 'starRating'})["data-score"]
                        writer.writerow({'Id': perfumeUrl["id"], 'Review': reviewText,'Rating': reviewRating})
perfumeUrls=getPerfumeData()
getReviews(perfumeUrls)

