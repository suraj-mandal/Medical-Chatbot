import requests
from bs4 import BeautifulSoup

file=open("SymptomList.txt",'r',encoding="UTF-8")
file1=open("SymptomList1.txt",'w',encoding="UTF-8")

SymptomList=[]

for i in file:
    name = i.replace("https://www.medicinenet.com/", "").replace("/symptoms.htm", "").replace("/article.htm","").replace("_", " ")
    SymptomList.append(name.rstrip().lower())

SymptomList=list(set(SymptomList))

c=1
for i in SymptomList:
    i.replace("-"," ")
    file1.writelines(str(i)+"\n")


