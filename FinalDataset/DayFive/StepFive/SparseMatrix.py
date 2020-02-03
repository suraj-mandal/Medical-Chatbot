import pandas as pd
import pickle as pkl

with open('DiseaseSymptom.pkl','rb') as file:
    dict=pkl.load(file)

column_name=[]

print(dict)
print(len(dict.keys()))

for i in range(1,723):
    column_name.append(i)
# print(list(dict.keys())[0])
rows=[]
found=[]
for i in range(len(list(dict.keys()))):
    row=[]
    if(len(dict[list(dict.keys())[i]])>=5):
        for j in range(1, 723):
            if(j in dict[list(dict.keys())[i]]):
                found.append(dict.keys())
                row.append(1)
            else:
                row.append(0)
        rows.append(row)

# print(rows)
data=pd.DataFrame(rows)
# print(data.head())
# print(data.shape)
# data.to_csv("SparseMatrixExperiment.csv")

for i in range(722):
    temp=data[i].tolist()
    if(1 not  in temp):
        del data[i]
        # print("Deleting ",i,"th column")
    # break

column_name=[x for x in range(0,230)]
data.to_csv("SparseMatrixExperiment.csv")
print(data.head())
print(data.shape)
data=pd.read_csv("SparseMatrixExperiment.csv")
x_columns=list(data.columns)[:115]
y_columns=list(data.columns)[115:230]

print(len(x_columns))
print(len(y_columns))
# data.rename()

temp_x=[]

data_x=data[x_columns].copy()
data_y=data[y_columns].copy()

print(data_x.shape)
print(data_y.shape)
# l=[]
# for i in range(0,230):
#     l.append(i)
# data=data.reindex(columns=l)

from sklearn.cluster import KMeans
from sklearn.preprocessing import PolynomialFeatures
km=KMeans(n_clusters=11)

km.fit(data)
# print(km.cluster_centers_)
# print(km.labels_)

x=[]
y=[]

for i in list(data.columns.values):
    temp=data[i].tolist()
    x.append(temp[:int(0.5*len(temp)+1)])
    y.append(temp[int(0.5*len(temp))+1:])

# poly = PolynomialFeatures(degree=2)
# X_ = poly.fit_transform(data)
#
# print("Printing first five instances of X_: ",X_[:5])
# print("Printing X[0] shape",len(X_[0]))
# # predict_ = poly.fit_transform()
#
# import matplotlib.pyplot as plt
# plt.scatter(X_)
# plt.show()


# data_x=data_x.values().tolist()
# print(data_x)

import numpy as np
data_x=np.array(data_x)
print(data_x.tolist())
x_values=[]

from AMedicalChatbot.DayFive.StepSix import StringToInt
b=StringToInt.Binary()
for i in range(len(data_x)):
    # print("".join(str(x) for x in data_x[i]))
    x_values.append(int(b._ToNumber("".join(str(x) for x in data_x[i]))))
    # print(x_values[i])
    # break
print(len(x_values))

data_y=np.array(data_y)
print(data_y.tolist())
y_values=[]
# from AMedicalChatbot.DayFive.StepSix import StringToInt
# b=StringToInt.Binary()
for i in range(len(data_y)):
    # print("".join(str(x) for x in data_x[i]))
    y_values.append(int(b._ToNumber("".join(str(y) for y in data_y[i]))))
    # print(x_values[i])
    # break
print(len(y_values))
print('yo')

import matplotlib.pyplot as plt

plt.plot(x_values,y_values,'ro')

# plt.show()

lb=km.labels_.tolist()

cluster_1x=[]
cluster_2x=[]
cluster_3x=[]
cluster_4x=[]
cluster_5x=[]
cluster_6x=[]
cluster_7x=[]
cluster_8x=[]
cluster_9x=[]
cluster_10x=[]



cluster_1y=[]
cluster_2y=[]
cluster_3y=[]
cluster_4y=[]
cluster_5y=[]
cluster_6y=[]
cluster_7y=[]
cluster_8y=[]
cluster_9y=[]
cluster_10y=[]


for index in range(len(lb)):
    if(lb[index] == 0):
        cluster_1x.append(x_values[index])
        cluster_1y.append(y_values[index])
    elif(lb[index] == 1):
        cluster_2x.append(x_values[index])
        cluster_2y.append(y_values[index])
    elif (lb[index] == 2):
        cluster_3x.append(x_values[index])
        cluster_3y.append(y_values[index])
    elif (lb[index] == 3):
        cluster_4x.append(x_values[index])
        cluster_4y.append(y_values[index])
    elif(lb[index]==4):
        cluster_5x.append(x_values[index])
        cluster_5y.append(y_values[index])
    elif (lb[index] == 5):
        cluster_5x.append(x_values[index])
        cluster_5y.append(y_values[index])
    elif (lb[index] == 6):
        cluster_6x.append(x_values[index])
        cluster_6y.append(y_values[index])
    elif (lb[index] == 7):
        cluster_7x.append(x_values[index])
        cluster_7y.append(y_values[index])
    elif (lb[index] == 8):
        cluster_8x.append(x_values[index])
        cluster_8y.append(y_values[index])
    elif (lb[index] == 9):
        cluster_9x.append(x_values[index])
        cluster_9y.append(y_values[index])
    elif (lb[index] == 10):
        cluster_10x.append(x_values[index])
        cluster_10y.append(y_values[index])

plt.plot(cluster_1x,cluster_1y,'ro')
plt.plot(cluster_2x,cluster_2y,'bo')
plt.plot(cluster_3x,cluster_3y,'go')
plt.plot(cluster_4x,cluster_4y,'yo')
plt.plot(cluster_5x,cluster_5y,'mo')
plt.plot(cluster_6x,cluster_6y,'ro')
plt.plot(cluster_7x,cluster_7y,'bo')
plt.plot(cluster_8x,cluster_8y,'go')
plt.plot(cluster_9x,cluster_9y,'yo')
plt.plot(cluster_10x,cluster_10y,'mo')


# plt.show()
print("****************************************")
print(len(x_values))
print(len(y_values))
print("****************************************")

# z=[]
# for i in list(data.columns.values):
#     temp=data[i].tolist()
#     z.append(temp)
# z=z[1:]
# print(z[0])
# print(len(z))
z=np.array(data).tolist()
z_values=[]
for i in range(len(z)):
    # print("".join(str(x) for x in data_x[i]))
    z_values.append(int(b._ToNumber("".join(str(x) for x in z[i]))))
    # print(x_values[i])
    # break
print(len(z_values))
print(z_values[0])

with open('Partitioning.pkl','wb') as file:
    pkl.dump(z_values,file)
file.close()

with open('X.pkl','wb') as file:
    pkl.dump(x_values,file)
file.close()

with open('Y.pkl','wb') as file:
    pkl.dump(y_values,file)
file.close()

# found=list(set(found))

file=open('Found.pkl','wb')
pkl.dump(found,file)
file.close()