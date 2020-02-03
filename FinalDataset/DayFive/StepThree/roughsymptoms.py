import re

file=open("SymptomList1.txt",'r')
file1=open("henoch-schonlein purpura.txt",'r')
diseaseList=[]

for i in file:
    diseaseList.append(i.rstrip())

with open ('henoch-schonlein purpura.txt','r',encoding='UTF-8') as myfile:
    s=myfile.read()
    for i in diseaseList:
        x = re.findall(i, s)
        if (len(x) > 0):
            print(i)