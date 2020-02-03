import pickle as pkl

with open('D:\Sharob\AMedicalChatbot\DayFive\StepFive\Partitioning.pkl','rb') as file:
    z=pkl.load(file)
file.close()

import numpy as np

z=np.array(z)

print(z.shape)

print(z.min())
print(z.max())

z=z.tolist()

cluster1=[]
cluster2=[]
cluster3=[]
cluster4=[]
cluster5=[]
cluster6=[]
cluster7=[]
cluster8=[]

for i in range(len(z)):
    if(z[i]<=106):
        cluster1.append(i)
    # elif (z[i] <=95 and z[i]>84):
    #     cluster2.append(i)
    # elif (z[i] <= 106 and z[i]>95):
    #     cluster3.append(i)
    elif (z[i] <= 117 and z[i]>106):
        cluster4.append(i)
    elif (z[i] <= 128 and z[i]>117):
        cluster5.append(i)
    elif (z[i] <= 139 and z[i]>128):
        cluster6.append(i)
    elif (z[i] <= 150 and z[i]>139):
        cluster7.append(i)
    elif (z[i] <= 155 and z[i]>150):
        cluster8.append(i)
    elif (z[i] <= 161 and z[i]>155):
        cluster2.append(i)

with open('D:\Sharob\AMedicalChatbot\DayFive\StepFive\X.pkl','rb') as file:
    x=pkl.load(file)
file.close()
with open('D:\Sharob\AMedicalChatbot\DayFive\StepFive\Y.pkl','rb') as file:
    y=pkl.load(file)
file.close()

cluster1_x=[]
cluster2_x=[]
cluster3_x=[]
cluster4_x=[]
cluster5_x=[]
cluster6_x=[]
cluster7_x=[]
cluster8_x=[]

cluster1_y=[]
cluster2_y=[]
cluster3_y=[]
cluster4_y=[]
cluster5_y=[]
cluster6_y=[]
cluster7_y=[]
cluster8_y=[]

# print(cluster1)
print(len(x))
print(len(y))

for i in cluster1:
    cluster1_x.append(x[i])
    cluster1_y.append(y[i])

for i in cluster2:
    cluster2_x.append(x[i])
    cluster2_y.append(y[i])

for i in cluster3:
    cluster3_x.append(x[i])
    cluster3_y.append(y[i])

for i in cluster4:
    cluster4_x.append(x[i])
    cluster4_y.append(y[i])

for i in cluster5:
    cluster5_x.append(x[i])
    cluster5_y.append(y[i])

for i in cluster6:
    cluster6_x.append(x[i])
    cluster6_y.append(y[i])

for i in cluster7:
    cluster7_x.append(x[i])
    cluster7_y.append(y[i])

for i in cluster8:
    cluster8_x.append(x[i])
    cluster8_y.append(y[i])

import matplotlib.pyplot as plt

plt.plot(cluster1_x,cluster1_y,'ro')
plt.plot(cluster2_x,cluster2_y,'yo')
plt.plot(cluster3_x,cluster3_y,'bo')
plt.plot(cluster4_x,cluster4_y,'go')
plt.plot(cluster5_x,cluster5_y,'co')
plt.plot(cluster6_x,cluster6_y,'mo')
plt.plot(cluster7_x,cluster7_y,'ko')
plt.plot(cluster8_x,cluster8_y,'bo')

plt.show()