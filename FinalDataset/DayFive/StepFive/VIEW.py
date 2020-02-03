import pickle as pkl
with open('Found.pkl','rb') as file:
    found=pkl.load(file)

file=open("DiseaseSymptoms.txt",'r',encoding="UTF-8")
DiseaseList=[]
for line in file:
    DiseaseList.extend(line.rstrip().split(","))

for ind in found:
    print(DiseaseList[ind])