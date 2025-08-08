text = "The goal is to turn data into information, and information into insight."
text.upper().replace(',','').replace('.','').split()

lst = ["D","A","T","A","S","C","I","E","N","C","E"]

lst.pop(8)
lst.append('A')
lst.insert(8,'N')

#append sona ekler , insert istedigin indexe

dict = {'Christian': ["America",18],
        'Daisy':["England",12],
        'Antonio':["Spain",22],
        'Dante':["Italy",25]}

dict.values()
dict.keys()
dict.update({'Daisy':["England",13]})
dict

dict.update({'Ahmet':['Turkey',22]})
dict

dict.pop('Daisy')
dict


###############################################
# GÖREV 5: Arguman olarak bir liste alan, listenin içerisindeki tek ve çift sayıları ayrı listelere atıyan ve bu listeleri return eden fonskiyon yazınız.
###############################################

l = [2,13,18,93,22]

def odd_even_num_divider(list):
    even_list=[]
    odd_list =[]

    for i in list:
        if i%2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)

    return even_list,odd_list

odd_even_num_divider(l)

#List Comp cozumu
#a = [even_list.append(i) if i%2 ==0 else odd_list.append(i) for i in l] boyle olmuyor ayri ayri yapilirmis append metodu kullanilmiyor
even_list=[i for i in l if i%2==0]
odd_list=[i for i in l if i%2==1]
even_list
odd_list

ogrenciler = ["Ali","Veli","Ayşe","Talat","Zeynep","Ece"]
for i,x in enumerate(ogrenciler):
    if i<3:
        i += 1
        print("Mühendislik Fakültesi",i,". öğrenci: ",x)
    else:
        i -= 2
        print("Tıp Fakültesi",i,". öğrenci: ",x)



###############################################
# GÖREV 7: Aşağıda 3 adet liste verilmiştir. Listelerde sırası ile bir dersin kodu, kredisi ve kontenjan bilgileri yer almaktadır. Zip kullanarak ders bilgilerini bastırınız.
###############################################

ders_kodu = ["CMP1005","PSY1001","HUK1005","SEN2204"]
kredi = [3,4,2,4]
kontenjan = [30,75,150,25]

for ders_kodu,kredi,kontenjan in zip(ders_kodu,kredi,kontenjan):
    print(f'Kredisi {kredi} olan ders kodu {ders_kodu} no lu dersin {kontenjan} kontenjani kalmistir')


kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])

def kume(set1,set2):
    if set1.issuperset(set2):
        print(set1.intersection(set2)) #ortak eleman
    else:
        print(set2.difference(set1)) #farklari

kume(kume1,kume2)


