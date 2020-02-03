import requests
from bs4 import BeautifulSoup

"""
symptomsandsigns pattern
"""
# link="https://www.medicinenet.com/esophageal_cancer/article.htm"
# data=requests.get(link).text
# info=BeautifulSoup(data,"html5lib").find('div',class_='pageContainer').findAll('div',class_='apPage')[3].findAll('p')
# info1=BeautifulSoup(data,"html5lib").find('div',class_='pageContainer').findAll('div',class_='apPage')[3].findAll('li')
#
# for i in range(len(info)):
#     print(info[i].text)
# for i in range(len(info1)):
#    print(info1[i].text)

"""
whataresymptoms pattern
"""
# link="https://www.medicinenet.com/objects_or_insects_in_ear/article.htm"
# data=requests.get(link).text
# info=BeautifulSoup(data,"html5lib").find('div',class_='pageContainer').findAll('div',class_='apPage')[0].findAll('p')
#
# for i in range(len(info)):
#     print(info[i].text)

"""
whatarethesymptoms pattern 
"""
# link="https://www.medicinenet.com/turner_syndrome/article.htm"
# data=requests.get(link).text
# info=BeautifulSoup(data,"html5lib").find('div',class_='pageContainer').findAll('div',class_='apPage')[1].findAll('p')
# info1=BeautifulSoup(data,"html5lib").find('div',class_='pageContainer').findAll('div',class_='apPage')[1].findAll('li')
# for i in range(len(info)):
#     print(info[i].text)
# for i in range(len(info1)):
#     print(info1[i].text)

"""
signsandsymptoms pattern
"""
# link="https://www.medicinenet.com/drug_allergies/article.htm"
# data=requests.get(link).text
#
# info=BeautifulSoup(data,"html5lib").find('div',class_='pageContainer').findAll('div',class_='apPage')[0].findAll('p')
# info1=BeautifulSoup(data,"html5lib").find('div',class_='pageContainer').findAll('div',class_='apPage')[0].findAll('li')
#
# for i in range(len(info)):
#     print(info[i].text)
# for i in range(len(info1)):
#     print(info1[i].text)