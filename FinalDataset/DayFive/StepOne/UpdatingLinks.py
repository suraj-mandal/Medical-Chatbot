file1=open("whataresymptoms.txt",'r',encoding="UTF-8")
file2=open("UpdatedLinks2.txt",'r',encoding="UTF-8")

file3=open("UpdatedLinks3.txt",'w',encoding="UTF-8")

list1=[]
list2=[]
c=1
for line in file1:
    list1.append(line.rstrip())
    c+=1
print(c)
c=1
for line in file2:
    list2.append(line.rstrip())
    c+=1
print(c)
z=list(set(list2)-set(list1))
c=1

for i in z:
    file3.writelines(str(i.rstrip())+"\n")
    c+=1
print(c)