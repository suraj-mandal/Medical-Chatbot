import pickle as pkl

with open('AllSymptoms.pkl','rb') as file:
    dict=pkl.load(file)

for i in dict:
    print(i)