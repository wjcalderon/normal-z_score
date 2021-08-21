import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

#File upload
df = pd.DataFrame()
df = pd.read_csv('/Users/wendycalderon/Documents/Personal/2021-2/universidad/IOT/Python/normal_zscore/normal_zscore.csv',delimiter=';')
df.head()
#General statics
df.describe()
#Plot histogram
# sn.histplot(df.Weight, kde=True)
# plt.show()

#Clean data
#media
mean =df.Weight.mean()
#desviación estandar
std =df.Weight.std()
#Limite inferior
lowerBound = mean - 3*std
#Limite superior
upperBound = mean + 3*std
#Outlier
df_outlier = df.Weight[ (df.Weight<lowerBound) | (df.Weight>upperBound) ] 
print(df_outlier.count())

df_no_outlier = df.Weight[ (df.Weight>lowerBound) & (df.Weight<upperBound) ] 
print(df_no_outlier.count())

#zscore
df["z-score"] = (df.Weight-mean)/std
print(df.head())
sn.histplot(df["z-score"], kde=True)
plt.show()