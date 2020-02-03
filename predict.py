import pickle

import numpy as np

from FinalDataset.DayFive.StepSix import StringToInt


def predict(symptoms_list):
    if not symptoms_list:
        return []
    mkm = pickle.load(open('./FinalDataset/MiniBatchKMeansModel.pkl',
                           'rb'))
    symptoms_model = pickle.load(open('./FinalDataset/Symptoms.pkl',
                                      'rb'))
    data = pickle.load(open('./FinalDataset/TrainingPreProcessedData.pkl', 'rb'))

    dis = pickle.load(open('./FinalDataset/ValueDiseaseDictionary.pkl', 'rb'))

    mkmdict = pickle.load(open('./FinalDataset/MiniBatchDictionary.pkl',
                               'rb'))

    conv = []
    for symptom in symptoms_model:
        if symptom in symptoms_list:
            conv.append(1)
        else:
            conv.append(0)
    conv = np.array(conv)
    data_x = conv.tolist()[:int(1909 / 2)]
    data_y = conv.tolist()[int(1909 / 2):1909]

    b = StringToInt.Binary()
    x_value = int(b._ToNumber("".join(str(x) for x in data_x)))
    y_value = int(b._ToNumber("".join(str(y) for y in data_y)))

    st = '(' + str(x_value) + ', ' + str(y_value) + ')'

    temp = {}
    if st in dis.keys():
        print(dis[st])
    else:
        vals = mkmdict[int(str(mkm.predict([[x_value, y_value]])).replace('[', '').replace(']', ''))]
        for val in vals:
            # euclidean_distance.append(((val[0] - x_value) ** 2 + (val[1] - y_value) ** 2)**0.5)
            temp[((val[0] - x_value) ** 2 + (val[1] - y_value) ** 2) ** 0.5] = [val[0], val[1]]

    predicted_diseases = []

    for i in range(5):
        value = temp[sorted(list(temp.keys()))[i]]
        # print(dis['('+str(value[0])+', '+str(value[1])+')'])
        # print(dis[(542, 636)])
        predicted_diseases.extend(dis[tuple(value)])

    return predicted_diseases
