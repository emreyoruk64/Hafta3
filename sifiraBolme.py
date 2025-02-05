# Ödev 2 
# Sıfıra bölme hatası
def bol():
    try:
        sayi1=int(input("1. sayıyı giriniz:"))
        sayi2=int(input("2. sayıyı giriniz:"))
        print("Bölme işleminin sonucu:",sayi1/sayi2)
    except ZeroDivisionError:
        print("Bir sayı 0'a bölünemez!!")

bol()
# NegativeNumberError Hata sınıfı 
import math
class NegativeNumberError(Exception):
    
    def __init__(self, message="Negatif sayı kabul edilmez!"):
        self.message = message
        super().__init__(f"{message}")

def faktoriyel(a):
    if a < 0:
        raise NegativeNumberError
    else:
        print(math.factorial(a))

faktoriyel(-5)

