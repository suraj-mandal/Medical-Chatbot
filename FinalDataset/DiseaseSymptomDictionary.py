class DisSym:
    def DiseaseSymptomD(self):
        file=open('C:\\Users\HP\Downloads\Codes\Fyp\AMedicalChatbot\FinalDataset\Dataset.txt','r',encoding='UTF-8')
        disease={}
        for line in file:
            line=line.lower()
            if(' or' in line):
                line=line.replace(' or','')
            if (' and' in line):
                line=line.replace(' and', '')
            if ('.' in line):
                line=line.replace('.', '')
            if ('  ' in line):
                line=line.replace('  ', ' ')
            lt=line.rstrip().strip().split(',')
            if '' in lt:
                lt.remove('')
            # print(lt)
            if(len(lt)>3):
                disease[lt[0]]=lt[1:]
            # print(len(disease.keys()))
            # break

        dis2={}
        for key in disease.keys():
            symps=set(disease[key])
            l=[]
            for symp in symps:
                if(symp != key or symp == ''):
                    if(symp in disease.keys()):
                        l.append(symp.strip().rstrip())
                        for elem in disease[symp]:
                            l.append(elem.rstrip().strip())
                    else:
                        l.append(symp.strip().rstrip())
            l=set(l)
            dis2[key]=l
        file=open("ProcessedDataset.txt",'w',encoding="UTF-8")
        for i in list(dis2.keys()):
            file.writelines(str(i)+"-->"+str(dis2[i])+"\n")
        # print(dis2)
        # print(len(dis2))
        symps=[]
        for key in dis2.keys():
            symps.extend(dis2[key])
        symps=list(set(symps))
        # print(len(symps))

        import pickle as pkl
        with open('DiseaseSymptoms.pkl','wb') as file:
            pkl.dump(dis2,file)
        file.close()
        with open('Symptoms.pkl','wb') as file:
            pkl.dump(symps,file)
        file.close()

        sparse=[]
        for key in dis2.keys():
            lt=[0]*len(symps)
            for sym in dis2[key]:
                lt[symps.index(sym)]=1
            sparse.append(lt)

        with open('SparseList.pkl','wb') as file:
            pkl.dump(sparse,file)
        file.close()

        import pandas as pd
        data=pd.DataFrame(sparse)
        print(data.head())
        print(data.shape)
        data.to_csv('SparseMatrix.csv')
