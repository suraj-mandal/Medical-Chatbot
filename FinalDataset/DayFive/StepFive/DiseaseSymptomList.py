f2=open("DiseaseSymptoms.txt",'a+',encoding="UTF-8")
for i in range(1,5):
    file=open("DiseaseSymptomsPattern"+str(i)+".txt",'r',encoding="UTF-8")
    for line in file:
        f2.writelines(line.rstrip()+"\n")
    file.close()

