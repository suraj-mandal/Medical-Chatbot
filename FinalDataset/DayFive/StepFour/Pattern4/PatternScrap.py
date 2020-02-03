import re

file=open("SymptomList1.txt",'r')
f1=open("DiseasePattern4.txt",'r',encoding="UTF-8")
f2=open("DiseaseSymptomsPattern4.txt",'w',encoding="UTF-8")

diseaseList=[]
for i in file:
    diseaseList.append(i.rstrip())

for filename in f1:
    file1=open(filename.rstrip(),'r',encoding="UTF-8")
    with open (filename.rstrip(),'r',encoding='UTF-8') as myfile:
        s=myfile.read()
        d=filename.replace(".txt",",")
        f2.writelines(d.rstrip())
        print(d.rstrip())
        for i in diseaseList:
            x = re.findall(i, s)
            if (len(x) > 0):
                f2.writelines(str(i)+",")
                # print(i)
        f2.writelines("\n")
