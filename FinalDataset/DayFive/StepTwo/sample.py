import requests
from bs4 import BeautifulSoup

link="https://www.medicinenet.com/henoch-schonlein_purpura/article.htm"
name = link.replace("https://www.medicinenet.com/", "").replace("/symptoms.htm", "").replace("/article.htm","").replace("_", " ")
file=open(name+".txt",'w',encoding="UTF-8")

data=requests.get(link).text
info=BeautifulSoup(data,"html5lib").find('div',class_='pageContainer').findAll('div',class_='apPage')[1].findAll('p')
info1=BeautifulSoup(data,"html5lib").find('div',class_='pageContainer').findAll('div',class_='apPage')[1].findAll('li')

for i in range(len(info)):
    file.writelines(info[i].text+"\n")
    print(info[i].text)
for i in range(len(info1)):
    file.writelines(info1[i].text + "\n")
    print(info1[i].text)

file.close()