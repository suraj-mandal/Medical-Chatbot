import requests
from bs4 import BeautifulSoup

basicLinks=[]
scrapLinks=[]
file=open("UpdatedLinks3.txt",'r',encoding="UTF-8")

for line in file:
    basicLinks.append(line.rstrip())

for link in basicLinks:
    data = requests.get(link)
    scrap = BeautifulSoup(data.text, 'html5lib')
    info = scrap.find('div', class_="toc").findAll('li')

    questionList = []
    for i in range(len(info)):
        question = info[i].text.lower()
        questionList.append(question)

    for i in questionList:
        if ("symptoms" in i):
            print(i,link)
            scrapLinks.append(i+","+link)
#
# c=1
file1=open("exceptions.txt",'w',encoding="UTF-8")
for links in scrapLinks:
    file1.writelines(str(links)+"\n")
    # c+=1
# print(c)