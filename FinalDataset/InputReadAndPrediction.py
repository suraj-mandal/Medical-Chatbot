import pickle as pkl

class Predict:
    def PredDisease(self,s):
        with open('MiniBatchKMeansModel.pkl','rb') as file:
            mkm=pkl.load(file)
        file.close()

        with open('KMeansModel.pkl','rb') as file:
            km=pkl.load(file)
        file.close()

        with open('TrainingPreProcessedData.pkl','rb') as file:
            data=pkl.load(file)
        file.close()

        import numpy as np
        test=np.array(data)

        # print(mkm.predict([test[1]]))
        # print(test[1])

        with open('DiseaseSymptoms.pkl','rb') as file:
            dict=pkl.load(file)
        file.close()

        with open('Symptoms.pkl','rb') as file:
            symp=pkl.load(file)
        file.close()

        with open('ValueDiseaseDictionary.pkl','rb') as file:
            dis=pkl.load(file)
        file.close()

        with open('MiniBatchDictionary.pkl','rb') as file:
            mkmdict=pkl.load(file)
        file.close()

        # s=['blackout', 'dizziness', 'shakiness', 'craving','sweating','aggression', 'agitation', 'compulsive behaviour', 'self-destructive behaviour', 'lack of restraint','anxiety', 'euphoria', 'general discontent', 'guilt','loneliness', 'nausea','vomiting','delirium' ,'fear','physical substance dependence', 'problems with coordination', 'slurred speech']
        # s=['vision disorder', 'feeling of something in eye', 'blurred vision', 'pain in the eyes', 'watery eyes', 'sensitivity to light', 'eye redness']

        conv=[]
        for i in symp:
            # if(i in dict[list(dict.keys())[0]]):
            if (i in s):
                conv.append(1)
            else:
                conv.append(0)

        conv=np.array(conv)
        print(conv.shape)

        data_x=conv.tolist()[:int(1909/2)]
        data_y=conv.tolist()[int(1909/2):1909]

        from FinalDataset.DayFive.StepSix import StringToInt
        b=StringToInt.Binary()
        x_value=int(b._ToNumber("".join(str(x) for x in data_x)))
        y_value=int(b._ToNumber("".join(str(y) for y in data_y)))

        print(x_value,y_value)

        print(mkm.predict([[x_value,y_value]]))

        st='('+str(x_value)+', '+str(y_value)+')'

        euclidean_distance=[]
        temp={}
        if(st in dis.keys()):
            print(dis[st])
        else:
            vals=mkmdict[int(str(mkm.predict([[x_value,y_value]])).replace('[','').replace(']',''))]
            for val in vals:
                # euclidean_distance.append(((val[0] - x_value) ** 2 + (val[1] - y_value) ** 2)**0.5)
                temp[((val[0] - x_value) ** 2 + (val[1] - y_value) ** 2)**0.5]=[val[0],val[1]]

        # srt=sorted(euclidean_distance)
        sharob=[]

        for i in range(5):
            value=temp[sorted(list(temp.keys()))[i]]
            # print(dis['('+str(value[0])+', '+str(value[1])+')'])
            # print(dis[(542, 636)])
            sharob.extend(dis[tuple(value)])

        return sharob

pr=Predict()
# s=['blackout', 'dizziness', 'shakiness', 'craving','sweating','aggression', 'agitation', 'compulsive behaviour', 'self-destructive behaviour', 'lack of restraint','anxiety', 'euphoria', 'general discontent', 'guilt','loneliness', 'nausea','vomiting','delirium' ,'fear','physical substance dependence', 'problems with coordination', 'slurred speech']
# s=['vision disorder', 'feeling of something in eye', 'blurred vision', 'pain in the eyes', 'watery eyes']
# s=['headache', 'fever']
#
# print(pr.PredDisease(s))

