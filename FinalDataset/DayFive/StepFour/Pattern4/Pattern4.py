import requests
from bs4 import BeautifulSoup

num=1
links=[]
disease=[]

file = open("signsandsymptoms.txt", 'r', encoding="UTF-8")
exception=open("Exception.txt",'w',encoding="UTF-8")

i=1

for line in file:
    link=str(line.rstrip())
    data = requests.get(link).text
    try:
        info = BeautifulSoup(data, "html5lib").find('div', class_='pageContainer').findAll('div', class_='apPage')[0].findAll('p')
        info1=BeautifulSoup(data,"html5lib").find('div',class_='pageContainer').findAll('div',class_='apPage')[0].findAll('li')

        name = link.replace("https://www.medicinenet.com/", "").replace("/symptoms.htm", "").replace("/article.htm","").replace("_", " ")
        newfile = open(name+".txt", 'w', encoding="UTF-8")
        print(num,name)
        num+=1
        disease.append(name)

        for i in range(len(info)):
            x = info[i].text
            links.append(x)

        for i in range(len(info1)):
            x=(info1[i].text)
            links.append(x)

        for j in links:
            newfile.writelines(str(j) + "\n")
        links=[]

    except:
        exception.writelines(line)
        # continue
        #write the exception link in new file

file1 = open("DiseasePattern4.txt", 'w', encoding="UTF-8")
disease=list(set(disease))
for j in disease:
    file1.writelines(str(j)+".txt"+"\n")
