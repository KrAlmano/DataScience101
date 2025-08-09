import pandas as pd

s=pd.Series([1,2,3,4])
type(s)
s.index
s.dtype
s.size
s.ndim
s.values
type(s.values)

##Veri okuma

df=pd.read_csv("advertising.csv")
df.head()

#Veriye bakis

import seaborn as sns

df= sns.load_dataset("titanic")
df.head()
df.tail()
df.ndim
df.shape
df.info()
df.columns
df.index
df.describe().T
df.isnull().values.any()
df.isnull().sum()

##Pandas secim islemleri
df.index
df[0:13]

df.drop(1,axis=0).head()

delete_indexes=[1,2,3]
df.drop(delete_indexes,axis=0).head(7)

#Degiskeni indexe cevirmek

df["age"].head()
df.age.head()

df.drop("age",axis=1).head()
df.head()

df.index = df["age"]

df.drop("age",axis=1,inplace=True) #Kalici olarak silindi
df.head()

#Indexi degiskene cevirmek

df["age"] = df.index
df.head()

df = df.reset_index().head()
df.head()


## Degiskenler uzerinde islemler
import pandas as pd
import seaborn as sns
pd.set_option("display.max_columns",None) #Tum verileri goster aralardaki ... dan kurtul
df= sns.load_dataset("titanic")
df.head()


df["age"].head()
type(df["age"].head()) #Pandas series
type(df[["age"]].head()) #Dataframe 2 tane [] kullanildi

df[["age","alive"]]

col_names=["age", "alive","adult_male"]

type(df[col_names])

df["age2"]= df["age"]**2
df["age3"]=df["age"] / df["age2"]
df.head()

df.drop("age3",axis=1).head()

df.loc[:,df.columns.str.contains("age")].head()

df.loc[:,~df.columns.str.contains("age")].head()

## LOC & ILOC

#iloc = integer based selection

df.iloc[0:3]

#loc : label based selection
df.loc[0:3]

df.iloc[0:3,0:3]

df.loc[0:3,"age"]
col_names=["age","embarked","alive"]

df.loc[0:4,col_names]


#Kosullu secimler (Conditional Selection)

df[df["age"]>50].head()
df[df["age"]>50]["age"].count()
df.loc[df["age"]>50,["age","class"]].head() #Tek kosul

df.loc[(df["age"]>50) & (df["sex"]=="male"),["age","class","sex","embarked"]] .head()  #Birden fazla kosulda paranteze al

df_new = df.loc[(df["age"]>50)
       & (df["sex"]=="male")
       & ((df["embark_town"]=="Cherbourg") | (df["embark_town"]=="Southampton")) ,
        ["age","sex","embark_town"]]

df["embark_town"].value_counts()
df_new["sex"].head()
df_new["embark_town"].value_counts()

df_new.head()


## Toplulastirna ve Gruplama (Aggregation & Grouping)

#count()
#first()
#last()
#mean()
#median()
#min()
#max()
#std()
#var()
#sum()
#pivot table

df["age"].mean()

df.groupby("sex")["age"].mean()
df.groupby("sex").agg({"age":["mean","sum"]})


df.groupby("sex").agg({"age":["mean","sum"],
                       "survived":"mean"})


df.groupby(["sex","embark_town","class"]).agg({"age":"mean",
                                                "survived":"mean",
                                                 "sex":"count"})


## PIVOT TABLE

df.pivot_table("survived","sex","embarked")

df.pivot_table("survived","sex","embarked",aggfunc="std")

df.pivot_table("survived","sex",["embarked","class"])

df["new_age"] = pd.cut(df["age"],[0,10,18,25,40,90])
df =df.drop("new_age2",axis=1)
df.pivot_table("survived","sex",["new_age","class"])

pd.set_option("display.width",500)


## Apply ve Lambda

import pandas as pd
import seaborn as sns
pd.set_option("display.max_columns",None)
pd.set_option("display.width",500)
df = sns.load_dataset("titanic")
df.head()

df["age2"] = df["age"]*2
df["age3"] = df["age"]*5

for col in df.columns:
        if "age" in col:
                print((df[col]/10).head())



for col in df.columns:
        if "age" in col:
                df[col] = df[col]/10

df.head()

df[["age","age2","age3"]].apply(lambda x:x/10).head()

df.loc[:,df.columns.str.contains("age")].apply(lambda x:x/10).head()


df.loc[: , df.columns.str.contains("age")].apply(lambda x: (x-x.mean()) / x.std()).head()

def standart_scaler(col_name):
        return (col_name-col_name.mean()) / col_name.std()

df.loc[: , df.columns.str.contains("age")].apply(standart_scaler).head()

#Kaydetmek icinde

df.loc[: , ["age","age2","age3"]] = df.loc[: , df.columns.str.contains("age")].apply(standart_scaler)
#OR
df.loc[:, df.columns.str.contains("age")] = df.loc[: , df.columns.str.contains("age")].apply(standart_scaler)
df.head()


## Birlestirme (Join) islemleri
import pandas as pd
import numpy as np

m = np.random.randint(1,30,size=(5,3))
df1 = pd.DataFrame(m,columns=["var1","var2","var3"])
df2 = df1 + 99

pd.concat([df1,df2])

pd.concat([df1,df2],ignore_index=True)

#Merge ile birlestirme

df1 = pd.DataFrame({"employees": ["John", "Dennis","Mark","Maria"],
                    "Group": ["Accounting", "Engineering","Engineering","HR"]})

df2 = pd.DataFrame({"employees": ["John", "Dennis","Mark","Maria"],
                    "Start_Date": [2010,2009,2014,2019]})

pd.merge(df1,df2,on="employees")


#Her calisanin mudur bilgisine erismek isteniyor

df3 = pd.merge(df1,df2)

df4 = pd.DataFrame({"Group" : ["Accounting", "Engineering", "HR"],
                    "Manager" : ["Caner","Mustafa","Berkcan"]})

pd.merge(df3,df4)

pd.merge(df3,df4,on="Group")


dict = {"Paris": [10,14], "Berlin" : [20,30]}

dict =pd.DataFrame(dict)
dict
dict.index = ["Row1","Row2"]
dict