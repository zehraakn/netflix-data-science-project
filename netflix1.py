import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

netflix=pd.read_csv("netflix_titles.csv")

movie = netflix.head()
print(movie)

movie1= netflix.shape
print(movie1)

movie2=netflix.columns
print(movie2)

movie3=netflix.isnull().sum()
print(movie3)

movie4=netflix.nunique()

data=netflix.copy()
data.shape
print(data)

data=data.dropna()
print(data)

# sns.countplot(data=netflix, x="type")
# sns.countplot(netflix["type"])
# fig=plt.gcf()
# fig.set_size_inches(5,5)
# plt.title("tür")
# plt.show()
# sns.countplot(data=netflix, x="rating")
# sns.countplot(data=netflix, x="rating").set_xticklabels(sns.countplot(netflix["rating"]).get_xticklabels(),rotation=90,ha="right")
# fig=plt.gcf()
# fig.set_size_inches(13,13)
# plt.title("rating")
# plt.show()

# Veriyi netflix adlı bir DataFrame'den aldığınızı varsayalım

# Grafik
plt.figure(figsize=(13, 13))   #Figür boyutunu ayarla

# Çubuk grafiği oluştur
sns.countplot(data=netflix, x="rating")

# x eksenindeki etiketlerin dönüşümü
plt.xticks(rotation=90, ha="right")

plt.title("Rating")  # Başlık ekle
plt.show()  # Grafiği göster


plt.figure(figsize=(10,8))
sns.countplot(x="rating",hue="type",data=netflix)
plt.title("tür ve reyting oranları")
plt.show()

labels=["Movie","TV Show"]
size=netflix["type"].value_counts()
colors = plt.cm.Wistia(np.linspace(0, 1, 2))
explode=[0,0.1]
plt.rcParams["figure.figsize"]=(9,9)
plt.pie(size,labels=labels,colors=colors,explode=explode,shadow=True,startangle=90)
plt.title("Tür görünümü",fontsize=25)
plt.legend()
plt.show()

netflix["rating"].value_counts().plot.pie(autopct="%1.1f%%",shadow=True,figsize=(10,8))
plt.show()



