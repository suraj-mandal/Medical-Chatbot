# file=open("DiseaseSymptoms.txt",'r',encoding="UTF-8")
# disSym=[]
# for i in file:
#     disSym.append(list(set(i.rstrip().split(","))))
# newDisSym=[]
# print(disSym)
# # l=[]
# for items in disSym:
#     flag=False
#     while("" in items):
#         items.remove("")
#         newDisSym.append(items)
#         flag=True
#         l.append(len(items))
#     if(flag==False):
#         newDisSym.append(items)
#         l.append(len(items))
# #
# print(l)

# # max=0
# # min=9
# # x=0
# # for i in disSym:
# #     for j in i:
# #         x+=1
# #     if(max<x):
# #         max=x
# #     if (min > x):
# #         min = x
# #     x=0
# # print(max)
# # print(min)
#
# import numpy as np
# l=np.array(l)
# print(l.mean())
# print(l.max())
# print(l.min())
# print(np.median(l))

import pickle as pkl

file = open("DiseaseSymptoms.txt", 'r', encoding="UTF-8")
DiseaseList = []
for line in file:
    DiseaseList.extend(line.rstrip().split(","))

while ("" in DiseaseList):
    DiseaseList.remove("")
# print(list(set(DiseaseList)))
j = 1

listAndIn = []
for i in DiseaseList:
    if (" and " in i):
        j += 1
        for elem in i.split(" and "):
            if (" in " in elem):
                sample = elem.split(" in ")
                # print(sample)
                listAndIn.append(sample[0])

# print(list(set(listAndIn)))
# print(len(listAndIn))

c = 0
for i in DiseaseList:
    c += 1
# print(c)
dictAnd = {}
listAnd = []
for i in DiseaseList:
    if (" and " in i):
        j += 1
        sample = i.split(" and ")
        # print(sample)
        listAnd.append(sample[0])
        dictAnd[i] = [sample[0], sample[1]]
# print(dictAnd)
# print(list(set(listAnd)))
# print(len(listAnd))
dictIn = {}
listIn = []
for i in DiseaseList:
    if (" in " in i):
        j += 1
        sample = i.split(" in ")
        # print(sample)
        listIn.append(sample[0])
        dictIn[i] = [sample[0], sample[1]]
# print(dictIn)
# print(list(set(listIn)))
# print(len(listIn))

x = listAnd + listIn
y = list(set(x) - set(listAndIn))
c = 1
for i in y:
    c += 1
# print(y)

newDiseaseList = set(DiseaseList) - set(y)
newDiseaseList = list(newDiseaseList)
c = 0
for i in newDiseaseList:
    c += 1
# print(c)

dict = {}
for i in range(len(newDiseaseList)):
    dict[newDiseaseList[i]] = i + 1
# print(dict)

dict["depression"] = len(newDiseaseList)
dict["heart attack"] = len(newDiseaseList) + 1
dict["thrush"] = len(newDiseaseList) + 2
dict["urinary incontinence"] = len(newDiseaseList) + 3

print(len(dict.keys()))

with open("AllSymptoms.pkl", 'wb') as file:
    pkl.dump(dict, file)
file.close()
file = open("DiseaseSymptoms.txt", 'r')
diseasedict = {}

for line in file:
    lt = line.rstrip().split(",")
    key = lt[0]
    del lt[0]
    lt = list(set(lt))
    if ("" in lt):
        lt.remove("")
    encoded_lt = []
    for elem in lt:
        encoded_lt.append(dict[elem])
    diseasedict[key] = encoded_lt
    # print(diseasedict)
# print(diseasedict)
file.close()
with open('DiseaseSymptom.pkl', 'wb') as file:
    pkl.dump(diseasedict, file)

file.close()
