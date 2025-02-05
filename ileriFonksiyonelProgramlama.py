# Ödev 4
# Map
liste=[1,2,3,4,5]

def carp(sayi):
    return sayi*sayi

def mapFonksiyonu(liste):
    return list(map(carp,liste))

sonuc=mapFonksiyonu(liste)
print(sonuc)

# Filter
yeniListe=["ahmet","ali","mehmet","veli","tuncay"]

def kontrol(stringListe):
    return "e" in stringListe

def filterFonksiyonu(a):
    return list(filter(kontrol,yeniListe))

sonuc1=filterFonksiyonu(yeniListe)
print(sonuc1)

# Reduce
from functools import reduce
sayilar = [11,64,25,21,81]

def topla(x, y):
    return x + y

def toplam(liste):
    return reduce(topla, liste)

print(toplam(sayilar))  

# Sorted
my_list = [(2, 3), (1, 4), (5, 1), (3, 2)]

sorted_list = sorted(my_list, key=lambda x: x[1])

print(sorted_list)
