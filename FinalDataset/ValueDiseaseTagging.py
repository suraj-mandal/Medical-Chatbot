import pickle as pkl


class ValDisTag:
    def valueDisease(self):
        with open('MiniBatchKMeansLabels.pkl','rb') as file:
            mkmlabels=pkl.load(file)
        file.close()

        with open('KMeansLabels.pkl','rb') as file:
            kmlabels=pkl.load(file)
        file.close()

        with open('TrainingPreProcessedData.pkl','rb') as file:
            data=pkl.load(file)
        file.close()

        with open('DiseaseSymptoms.pkl','rb') as file:
            dss=pkl.load(file)
        file.close()

        dict={}

        print(data[0])
        print(kmlabels[0])
        print(mkmlabels[0])

        for i in range(len(data)):
            dict[tuple(data[i])]=[mkmlabels[i],kmlabels[i]]
            # print(dict)
            # break

        mkmind1=[]
        mkmind2=[]
        mkmind3=[]
        mkmind4=[]
        mkmind5=[]
        mkmind6=[]
        mkmind7=[]
        mkmind8=[]
        mkmind9=[]

        mkm={}

        for i in range(len(mkmlabels)):
            if(mkmlabels[i]==0):
                mkmind1.append(data[i])
            if (mkmlabels[i] == 1):
                mkmind2.append(data[i])
            if (mkmlabels[i] == 2):
                mkmind3.append(data[i])
            if (mkmlabels[i] == 3):
                mkmind4.append(data[i])
            if (mkmlabels[i] == 4):
                mkmind5.append(data[i])
            if (mkmlabels[i] == 5):
                mkmind6.append(data[i])
            if (mkmlabels[i] == 6):
                mkmind7.append(data[i])
            if (mkmlabels[i] == 7):
                mkmind8.append(data[i])
            if (mkmlabels[i] == 8):
                mkmind9.append(data[i])

        mkm[0]=mkmind1
        mkm[1]=mkmind2
        mkm[2]=mkmind3
        mkm[3]=mkmind4
        mkm[4]=mkmind5
        mkm[5]=mkmind6
        mkm[6]=mkmind7
        mkm[7]=mkmind8
        mkm[8]=mkmind9

        kmind1=[]
        kmind2=[]
        kmind3=[]
        kmind4=[]
        kmind5=[]
        kmind6=[]
        kmind7=[]
        kmind8=[]
        kmind9=[]

        km={}

        for i in range(len(kmlabels)):
            if(kmlabels[i]==0):
                kmind1.append(data[i])
            if (kmlabels[i] == 1):
                kmind2.append(data[i])
            if (kmlabels[i] == 2):
                kmind3.append(data[i])
            if (kmlabels[i] == 3):
                kmind4.append(data[i])
            if (kmlabels[i] == 4):
                kmind5.append(data[i])
            if (kmlabels[i] == 5):
                kmind6.append(data[i])
            if (kmlabels[i] == 6):
                kmind7.append(data[i])
            if (kmlabels[i] == 7):
                kmind8.append(data[i])
            if (kmlabels[i] == 8):
                kmind9.append(data[i])

        km[0]=kmind1
        km[1]=kmind2
        km[2]=kmind3
        km[3]=kmind4
        km[4]=kmind5
        km[5]=kmind6
        km[6]=kmind7
        km[7]=kmind8
        km[8]=kmind9

        with open('MiniBatchDictionary.pkl','wb') as file:
            pkl.dump(mkm,file)
        file.close()

        with open('KMeansDictionary.pkl','wb') as file:
            pkl.dump(km,file)
        file.close()

        dis={}
        for i in range(len(data)):
            dis[tuple(data[i])]=[list(dss.keys())[i]]

        with open('ValueDiseaseDictionary.pkl','wb') as file:
            pkl.dump(dis,file)
        file.close()

        with open('ValueLabelDictionary.pkl','wb') as file:
            pkl.dump(dis,file)
        file.close()

        print(dis)