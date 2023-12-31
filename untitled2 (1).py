# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rW_HcZctRTnSgfFaImgAeWZbpYZNTYCl
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
df=pd.read_csv('/content/Mall_Customers.csv')
df

b=df.isnull().sum()
print(b)
print(df.head())

x=df[['CustomerID','Annual Income (k$)','Age']]
y=['Genre']

#elbow method
sum_squared_distances=[]
k_values=range(1,11)

#k-means algorthim on the training dataset
for k in k_values:
  kmeans=KMeans(n_clusters=k,random_state=42)
  kmeans.fit(x)
  sum_squared_distances.append(kmeans.inertia_)

#visulization of cluster
plt.plot(k_values,sum_squared_distances,marker='o')
plt.show()