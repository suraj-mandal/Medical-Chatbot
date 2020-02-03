import pickle as pkl


class rough2:
    def runRough2(self):
        with open('Partitioning.pkl','rb') as file:
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
        cluster9=[]
        cluster10=[]
        cluster11=[]
        cluster12=[]
        cluster13=[]
        cluster14=[]
        cluster15=[]

        # for i in range(len(z)):
        #     if(z[i]<=499):
        #         cluster1.append(i)
        #     elif (z[i] <=558 and z[i]>499):
        #         cluster2.append(i)
        #     elif (z[i] <= 617 and z[i]>558):
        #         cluster3.append(i)
        #     elif (z[i] <= 676 and z[i]>617):
        #         cluster4.append(i)
        #     elif (z[i] <= 735 and z[i]>676):
        #         cluster5.append(i)
        #     elif (z[i] <= 794 and z[i]>735):
        #         cluster6.append(i)
        #     elif (z[i] <= 853 and z[i]>794):
        #         cluster7.append(i)
        #     elif (z[i] <= 912 and z[i]>853):
        #         cluster8.append(i)
        #     elif (z[i] <= 971 and z[i]>912):
        #         cluster9.append(i)
        #     elif (z[i] <= 1030 and z[i]>971):
        #         cluster10.append(i)
        #     elif (z[i] <= 1089 and z[i]>1030):
        #         cluster11.append(i)
        #     elif (z[i] <= 1148 and z[i]>1089):
        #         cluster12.append(i)
        #     elif (z[i] <= 1207 and z[i]>1148):
        #         cluster13.append(i)
        #     elif (z[i] <= 1266 and z[i]>1207):
        #         cluster14.append(i)
        #     elif (z[i] <= 1325 and z[i]>1266):
        #         cluster15.append(i)

        for i in range(len(z)):
            if(z[i]<=794):
                cluster1.append(i)
            # elif (z[i] <=558 and z[i]>499):
            #     cluster2.append(i)
            # elif (z[i] <= 617 and z[i]>558):
            #     cluster3.append(i)
            # elif (z[i] <= 676 and z[i]>617):
            #     cluster4.append(i)
            # elif (z[i] <= 794 and z[i]>676):
            #     cluster5.append(i)
            # elif (z[i] <= 794 and z[i]>735):
            #     cluster6.append(i)
            elif (z[i] <= 1030 and z[i]>794):
                cluster2.append(i)
            # elif (z[i] <= 912 and z[i]>853):
            #     cluster8.append(i)
            # elif (z[i] <= 971 and z[i]>912):
            #     cluster9.append(i)
            # elif (z[i] <= 1030 and z[i]>971):
            #     cluster3.append(i)
            elif (z[i] <= 1089 and z[i]>1030):
                cluster3.append(i)
            elif (z[i] <= 1148 and z[i]>1089):
                cluster3.append(i)
            elif (z[i] <= 1207 and z[i]>1148):
                cluster4.append(i)
            elif (z[i] <= 1266 and z[i]>1207):
                cluster4.append(i)
            elif (z[i] <= 1300 and z[i]>1266):
                cluster5.append(i)
            elif (z[i] <= 1325 and z[i] > 1266):
                cluster6.append(i)

        with open('X.pkl','rb') as file:
            x=pkl.load(file)
        file.close()
        with open('Y.pkl','rb') as file:
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
        cluster9_x=[]
        cluster10_x=[]
        cluster11_x=[]
        cluster12_x=[]
        cluster13_x=[]
        cluster14_x=[]
        cluster15_x=[]

        cluster1_y=[]
        cluster2_y=[]
        cluster3_y=[]
        cluster4_y=[]
        cluster5_y=[]
        cluster6_y=[]
        cluster7_y=[]
        cluster8_y=[]
        cluster9_y=[]
        cluster10_y=[]
        cluster11_y=[]
        cluster12_y=[]
        cluster13_y=[]
        cluster14_y=[]
        cluster15_y=[]

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

        for i in cluster9:
            cluster9_x.append(x[i])
            cluster9_y.append(y[i])

        for i in cluster10:
            cluster10_x.append(x[i])
            cluster10_y.append(y[i])

        for i in cluster11:
            cluster11_x.append(x[i])
            cluster11_y.append(y[i])

        for i in cluster12:
            cluster12_x.append(x[i])
            cluster12_y.append(y[i])

        for i in cluster13:
            cluster13_x.append(x[i])
            cluster13_y.append(y[i])

        for i in cluster14:
            cluster14_x.append(x[i])
            cluster14_y.append(y[i])

        for i in cluster15:
            cluster15_x.append(x[i])
            cluster15_y.append(y[i])

        import matplotlib.pyplot as plt

        # plt.plot(cluster1_x,cluster1_y,'red',marker='o',linestyle=" ")
        # plt.plot(cluster2_x,cluster2_y,'blue',marker='o',linestyle=" ")
        # plt.plot(cluster3_x,cluster3_y,'green',marker='o',linestyle=" ")
        # plt.plot(cluster4_x,cluster4_y,'yellow',marker='o',linestyle=" ")
        # plt.plot(cluster5_x,cluster5_y,'black',marker='o',linestyle=" ")
        # plt.plot(cluster6_x,cluster6_y,'cyan',marker='o',linestyle=" ")
        # plt.plot(cluster7_x,cluster7_y,'gold',marker='o',linestyle=" ")
        # plt.plot(cluster8_x,cluster8_y,'pink',marker='o',linestyle=" ")
        # plt.plot(cluster9_x,cluster9_y,'navy',marker='o',linestyle=" ")
        # plt.plot(cluster10_x,cluster10_y,'lime',marker='o',linestyle=" ")
        # plt.plot(cluster11_x,cluster11_y,'tomato',marker='o',linestyle=" ")
        # plt.plot(cluster12_x,cluster12_y,'teal',marker='o',linestyle=" ")
        # plt.plot(cluster13_x,cluster13_y,'salmon',marker='o',linestyle=" ")
        # plt.plot(cluster14_x,cluster14_y,'bisque',marker='o',linestyle=" ")
        # plt.plot(cluster15_x,cluster15_y,'limegreen',marker='o',linestyle=" ")
        # # plt.plot(cluster15_x,cluster15_y,'limegreen','o')
        #
        #
        # plt.show()

        data=[]

        for i in range(len(x)):
            data.append([x[i],y[i]])

        import pandas as pd
        data=pd.DataFrame(data)
        print(data.head())

        with open('TrainingPreProcessedData.pkl','wb') as file:
            pkl.dump(data.to_numpy(),file)

        from sklearn.cluster import MiniBatchKMeans
        km=MiniBatchKMeans(n_clusters=9,random_state=5)
        km.fit(data)

        print(km.cluster_centers_)
        print(km.labels_)

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

        for i in range(len(km.labels_)):
            if(km.labels_[i]==0):
                cluster1_x.append(x[i])
                cluster1_y.append(y[i])
            if (km.labels_[i] == 1):
                cluster2_x.append(x[i])
                cluster2_y.append(y[i])
            if (km.labels_[i] == 2):
                cluster3_x.append(x[i])
                cluster3_y.append(y[i])
            if (km.labels_[i] == 3):
                cluster4_x.append(x[i])
                cluster4_y.append(y[i])
            if (km.labels_[i] == 4):
                cluster5_x.append(x[i])
                cluster5_y.append(y[i])
            if (km.labels_[i] == 5):
                cluster6_x.append(x[i])
                cluster6_y.append(y[i])
            if (km.labels_[i] == 6):
                cluster7_x.append(x[i])
                cluster7_y.append(y[i])
            if (km.labels_[i] == 7):
                cluster8_x.append(x[i])
                cluster8_y.append(y[i])
            if (km.labels_[i] == 8):
                cluster9_x.append(x[i])
                cluster9_y.append(y[i])

        plt.plot(cluster1_x,cluster1_y,'red',marker='o',linestyle=" ")
        plt.plot(cluster2_x,cluster2_y,'blue',marker='o',linestyle=" ")
        plt.plot(cluster3_x,cluster3_y,'green',marker='o',linestyle=" ")
        plt.plot(cluster4_x,cluster4_y,'yellow',marker='o',linestyle=" ")
        plt.plot(cluster5_x,cluster5_y,'black',marker='o',linestyle=" ")
        plt.plot(cluster6_x,cluster6_y,'cyan',marker='o',linestyle=" ")
        plt.plot(cluster7_x,cluster7_y,'gold',marker='o',linestyle=" ")
        plt.plot(cluster8_x,cluster8_y,'pink',marker='o',linestyle=" ")
        plt.plot(cluster9_x,cluster9_y,'navy',marker='o',linestyle=" ")

        plt.plot(km.cluster_centers_[0][0],km.cluster_centers_[0][1],'blue',marker='*',markersize=15,linestyle=" ")
        plt.plot(km.cluster_centers_[1][0],km.cluster_centers_[1][1],'green',marker='*',markersize=15,linestyle=" ")
        plt.plot(km.cluster_centers_[2][0],km.cluster_centers_[2][1],'yellow',marker='*',markersize=15,linestyle=" ")
        plt.plot(km.cluster_centers_[3][0],km.cluster_centers_[3][1],'black',marker='*',markersize=15,linestyle=" ")
        plt.plot(km.cluster_centers_[4][0],km.cluster_centers_[4][1],'cyan',marker='*',markersize=15,linestyle=" ")
        plt.plot(km.cluster_centers_[5][0],km.cluster_centers_[5][1],'gold',marker='*',markersize=15,linestyle=" ")
        plt.plot(km.cluster_centers_[6][0],km.cluster_centers_[6][1],'magenta',marker='*',markersize=15,linestyle=" ")
        plt.plot(km.cluster_centers_[7][0],km.cluster_centers_[7][1],'red',marker='*',markersize=15,linestyle=" ")
        plt.plot(km.cluster_centers_[8][0],km.cluster_centers_[8][1],'limegreen',marker='*',markersize=15,linestyle=" ")
        plt.show()

        with open('MiniBatchKMeansLabels.pkl','wb') as file:
            pkl.dump(km.labels_,file)
        file.close()

        with open('MiniBatchKMeansModel.pkl','wb') as file:
            pkl.dump(km,file)
        file.close()

        from sklearn.cluster import KMeans
        km=KMeans(n_clusters=9,random_state=15)
        km.fit(data)

        print(km.cluster_centers_)
        print(km.labels_)

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

        for i in range(len(km.labels_)):
            if(km.labels_[i]==0):
                cluster1_x.append(x[i])
                cluster1_y.append(y[i])
            if (km.labels_[i] == 1):
                cluster2_x.append(x[i])
                cluster2_y.append(y[i])
            if (km.labels_[i] == 2):
                cluster3_x.append(x[i])
                cluster3_y.append(y[i])
            if (km.labels_[i] == 3):
                cluster4_x.append(x[i])
                cluster4_y.append(y[i])
            if (km.labels_[i] == 4):
                cluster5_x.append(x[i])
                cluster5_y.append(y[i])
            if (km.labels_[i] == 5):
                cluster6_x.append(x[i])
                cluster6_y.append(y[i])
            if (km.labels_[i] == 6):
                cluster7_x.append(x[i])
                cluster7_y.append(y[i])
            if (km.labels_[i] == 7):
                cluster8_x.append(x[i])
                cluster8_y.append(y[i])
            if (km.labels_[i] == 8):
                cluster9_x.append(x[i])
                cluster9_y.append(y[i])

        plt.plot(cluster1_x,cluster1_y,'red',marker='o',linestyle=" ")
        plt.plot(cluster2_x,cluster2_y,'blue',marker='o',linestyle=" ")
        plt.plot(cluster3_x,cluster3_y,'green',marker='o',linestyle=" ")
        plt.plot(cluster4_x,cluster4_y,'yellow',marker='o',linestyle=" ")
        plt.plot(cluster5_x,cluster5_y,'black',marker='o',linestyle=" ")
        plt.plot(cluster6_x,cluster6_y,'cyan',marker='o',linestyle=" ")
        plt.plot(cluster7_x,cluster7_y,'gold',marker='o',linestyle=" ")
        plt.plot(cluster8_x,cluster8_y,'pink',marker='o',linestyle=" ")
        plt.plot(cluster9_x,cluster9_y,'navy',marker='o',linestyle=" ")

        plt.plot(km.cluster_centers_[0][0],km.cluster_centers_[0][1],'blue',marker='*',markersize=15,linestyle=" ")
        plt.plot(km.cluster_centers_[1][0],km.cluster_centers_[1][1],'green',marker='*',markersize=15,linestyle=" ")
        plt.plot(km.cluster_centers_[2][0],km.cluster_centers_[2][1],'yellow',marker='*',markersize=15,linestyle=" ")
        plt.plot(km.cluster_centers_[3][0],km.cluster_centers_[3][1],'black',marker='*',markersize=15,linestyle=" ")
        plt.plot(km.cluster_centers_[4][0],km.cluster_centers_[4][1],'cyan',marker='*',markersize=15,linestyle=" ")
        plt.plot(km.cluster_centers_[5][0],km.cluster_centers_[5][1],'gold',marker='*',markersize=15,linestyle=" ")
        plt.plot(km.cluster_centers_[6][0],km.cluster_centers_[6][1],'magenta',marker='*',markersize=15,linestyle=" ")
        plt.plot(km.cluster_centers_[7][0],km.cluster_centers_[7][1],'red',marker='*',markersize=15,linestyle=" ")
        plt.plot(km.cluster_centers_[8][0],km.cluster_centers_[8][1],'limegreen',marker='*',markersize=15,linestyle=" ")
        plt.show()

        with open('KMeansLabels.pkl','wb') as file:
            pkl.dump(km.labels_,file)
        file.close()

        with open('KMeansModel.pkl','wb') as file:
            pkl.dump(km,file)
        file.close()