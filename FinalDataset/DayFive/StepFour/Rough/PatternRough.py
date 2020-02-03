file=open("DiseaseSymptomsPattern1.txt",'r',encoding="UTF-8")
disSym=[]
for i in file:
    disSym.append(list(set(i.rstrip().split(","))))
newDisSym=[]
l=[]
for items in disSym:
    flag=False
    while("" in items):
        items.remove("")
        newDisSym.append(items)
        flag=True
        l.append(len(items))
    if(flag==False):
        newDisSym.append(items)
        l.append(len(items))

print(disSym)
print(l)
# max=0
# min=9
# x=0
# for i in disSym:
#     for j in i:
#         x+=1
#     if(max<x):
#         max=x
#     if (min > x):
#         min = x
#     x=0
# print(max)
# print(min)

import numpy as np
l=np.array(l)
print(l.mean())
print(l.max())
print(l.min())
print(np.median(l))