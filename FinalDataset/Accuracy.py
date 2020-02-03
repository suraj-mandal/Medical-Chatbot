import pickle as pkl

with open('MiniBatchKMeansModel.pkl','rb') as file:
    mkm=pkl.load(file)
file.close()
#
# with open('KMeansModel.pkl','rb') as file:
#     mkm=pkl.load(file)
# file.close()

with open('TrainingPreProcessedData.pkl','rb') as file:
    data=pkl.load(file)
file.close()

# print(data[0])

# import numpy as np
# test=np.array(data)
#
# print(mkm.predict([test[0]]))

with open('DiseaseSymptoms.pkl','rb') as file:
    dict=pkl.load(file)
file.close()
# print(dict)

# with open('Symptoms.pkl','rb') as file:
#     symp=pkl.load(file)
# file.close()

with open('ValueDiseaseDictionary.pkl','rb') as file:
    dis=pkl.load(file)
file.close()
# print(dis)

with open('MiniBatchDictionary.pkl','rb') as file:
    mkmdict=pkl.load(file)
file.close()
# print(mkmdict)
score=0
correct=[]

for i in range(data.shape[0]):
    st='('+str(data[i][0])+', '+str(data[i][1])+')'
    # print(st)
    euclidean_distance=[]
    temp={}
    if(st in dis.keys()):
        print(dis[st])
    else:
        vals=mkmdict[int(str(mkm.predict([[data[i][0],data[i][1]]])).replace('[','').replace(']',''))]
        for val in vals:
            # euclidean_distance.append(((val[0] - x_value) ** 2 + (val[1] - y_value) ** 2)**0.5)
            temp[((val[0] - data[i][0]) ** 2 + (val[1] - data[i][1]) ** 2)**0.5]=[val[0],val[1]]

    # srt=sorted(euclidean_distance)
    predictions=[]
    for j in range(5):
        value=temp[sorted(list(temp.keys()))[j]]
        # print(dis['('+str(value[0])+', '+str(value[1])+')'])
        # print(dis[(542, 636)])
        predictions.extend(dis[tuple(value)])
        # print(dis[tuple(value)])

    # print(predictions)
    # print(list(dict.keys())[i])
    if list(dict.keys())[i] in predictions:
        score=score+1
        correct.append(list(dict.keys())[i])


print(score/data.shape[0])

file=open('CorrectPredictedDiseases.txt','w')

for disease in correct:
    file.writelines(disease+"\n")
