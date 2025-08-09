import pandas as pd
import seaborn as sns
pd.set_option("display.max_columns",None)
pd.set_option("display.max_rows",None)
pd.set_option("display.width",1000)


df = sns.load_dataset("titanic")
df.head()
df.shape

# kadin ve erkek yolcularin sayisi

df["sex"].count()
df["sex"].value_counts() #Sayisal
df["sex"].value_counts(normalize=True) #Yuzdesel

#Essiz degerler

df.nunique()
df["sex"].unique()
df["sex"].nunique()

#pclass ve parch degiskenlerinin unique sayisi

df[["pclass","parch"]].nunique()

#embarked degiskeninin tipini kontrol et , sonra kategorik yap bir daha kontrol et

df["embarked"].dtype

df["embarked"] = df["embarked"].astype("category")

df["embarked"].dtype

df.info()

#embarked degeri C olanlari goster

df[df["embarked"] == "C"].head()

#embarked degerleri s olmayanlari goster

df[df["embarked"] != "S"].head()
#Ya da
df[~(df["embarked"]=="S")].head()

df[df["embarked"] != "S"]["embarked"].unique()


#Yasi 30 dan kucuk ve kadin yolculari goster

df[(df["age"]<30) & (df["sex"]=="female")].head()


#Fare i 500 den buyuk veya yasi 70 den buyuk olan yolcu bilgileir

df[(df["fare"] > 500) | (df["age"]>70)].head()


#Her bir degiskenin bos deger toplamini bulunuz

df.isnull().sum()

#Who degiskenini dataframeden dusurun

df.drop("who",axis=1,inplace=True)  #inplace = True ifadesi islemi kalici yapar

#Ya da

df = df.drop("who",axis=1)

#deck degiskenindeki bos degerleri deck degiskeninin en cok tekrar eden degeri ile (mode) ile doldur

type(df["deck"].mode())
type(df["deck"].mode()[0])  #String deger

df["deck"].fillna(df["deck"].mode()[0], inplace=True)

#age degiskeninin bos degerlerini medyan ile doldur

df["age"] = df["age"].fillna(df["age"].median())


#survived degiskeninin pclass ve cinsiyet kiriliminda sum,count,mean degerleri

df.groupby(["pclass","sex"])["survived"].agg(["mean","count","sum"]) #Sadece survived degiskenine odaklanir

df.groupby(["pclass","sex"]).agg({"survived" : ["sum","count","mean"],  #Birden fazla deger icin age degiskeni gibi kullanilabilir
                                   "age": ["sum","count","mean"]})

#30 yasinin altinda olanlara 1 , esit ve buyuk olanlara 0 degerini atayan bir fonksiyon yaz ve age_flag adinda bir degisken olusturarak degeri buraya ata
#Apply ve lambda kullan

def age_30(age):
    if age <30:
        return 1
    else:
        return 0

df["age_flag"]= df["age"].apply(age_30)

# OR
df["age_flag"] = df["age"].apply(lambda x : age_30)

# OR

df["age_flag"] = df["age"].apply(lambda x: 1 if x<30 else 0)

# seaborndaki tips veri setini tanimla

df = sns.load_dataset("tips")
df.head()
df.shape

#time degiskeninin kategorilerine gore total_bill degerlerinin toplam,min,max ve ortalamasin bul

df.groupby("time").agg({"total_bill" : ["sum","min","max","mean"]})

#gunlere ve time gore total_bill degiskeninin toplam,min,max ve ortalamasin bul

df.groupby(["day","time"]).agg({"total_bill" : ["sum","min","max","mean"]})

#Lunch zamanina ve kadin musterilere ait total_bill ve tip degerlerinin day"e gore toplam,min,max ve ortalamasin bul

df[(df["time"]=="Lunch") & (df["sex"]=="Female")].groupby("day").agg({"total_bill" : ["sum","min","max","mean"],
                                                                      "tip" : ["sum","min","max","mean"]})

#size i 3 den kucuk ve total_bill degeri 10 dan buyuk olan siparislerin ortalamasi

df.loc[(df["size"]<3 ) & (df["total_bill"]>10), "total_bill"].mean()

#total_bill_tip_sum adinda yeni bir degisken olustur ve total_bill + tips degerini versin

df["total_bill_tip_sum"] = df["total_bill"] + df["tip"]
df.head()


#total_bill_tip_sum degiskenini buyukten kucuge sirala ve ilk 30 kisiyi yeni bir dataframe e ata

new_df = df.sort_values("total_bill_tip_sum",ascending= False)[:30]
new_df.count()
new_df.shape
