import requests
from bs4 import BeautifulSoup

basicLinks=[]
scrapLinks=[]
file=open("UpdatedLinks1.txt",'r',encoding="UTF-8")

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
        if ("what are the symptoms" in i):
            # file1.writelines(link)
            print(i,link)
            scrapLinks.append(link)

c=1
file1=open("whatarethesymptoms .txt",'w',encoding="UTF-8")
for links in scrapLinks:
    file1.writelines(str(links)+"\n")
    c+=1
print(c)