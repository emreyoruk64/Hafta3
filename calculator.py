# Ödev 1 ve bu haftanın projelerinden 3. sü gelişmiş hesap makinesi. İkisini aynı yaptım :) 
import math
toplama="+"
cikarma="-"
carpma="*"
bolme="/"
try:
    while True:
        sayi1=int(input("1. sayiyi giriniz:"))
        sayi2=int(input("2. sayiyi giriniz:"))
        islem=input("Lutfen yapmak istediginiz islemi seciniz:")
        if islem=="+":
            print(sayi1+sayi2)
        elif islem=="-":
            print(sayi1-sayi2)
        elif islem=="*":
            print(sayi1*sayi2)
        elif islem=="/":
            if sayi2==0:
                print("Bir sayi 0'a bölünemez!")
            else:
                print(sayi1/sayi2)
        elif islem=="^":
            print(math.pow(sayi1,sayi2))
        elif islem=="!" and sayi1>=0 and sayi2 >=0:
            print(math.factorial(sayi1))
            print(math.factorial(sayi2))
        elif islem=="|":
            print(math.fabs(sayi1))
            print(math.fabs(sayi2))
        elif islem=="sqrt" and sayi1>=0 and sayi2 >=0:
            print(math.sqrt(sayi1))
            print(math.sqrt(sayi2))
        elif islem=="sin":
            print(math.sin(math.radians(sayi1)))
            print(math.sin(math.radians(sayi2)))
        elif islem=="cos":
            print(math.cos(math.radians(sayi1)))
            print(math.cos(math.radians(sayi2)))
        elif islem=="tan":
            print(math.tan(math.radians(sayi1)))
            print(math.tan(math.radians(sayi2)))
        elif islem=="arcsin" and -1<=sayi1<=1 and -1<=sayi2<=1:
            print(math.degrees(math.asin(sayi1)))
            print(math.degrees(math.asin(sayi2)))
        elif islem=="arccos" and -1<=sayi1<=1 and -1<=sayi2<=1:
            print(math.degrees(math.acos(sayi1)))
            print(math.degrees(math.acos(sayi2)))
        elif islem=="arctan":
            print(math.degrees(math.atan(sayi1)))
            print(math.degrees(math.atan(sayi2)))
        elif islem=="log" and sayi1>0 and sayi2>0:
            print(math.log(sayi1))
            print(math.log(sayi2))
        elif islem=="q":
            print("Çıkış yapılıyor")
            break
        else:
            print("Lutfen gecerli bir islem giriniz veya giriş değerlerini kontrol ediniz")
except ValueError:
    print("Lutfen gecerli bir deger giriniz")


from my_module import cember_cevresi
from my_module import daire_alan
cember_cevresi=cember_cevresi(5)
daire_alan=daire_alan(10)
print("Çemberin çevresi:",cember_cevresi)
print("Dairenin alanı:",daire_alan)

