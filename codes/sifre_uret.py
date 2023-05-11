import random
import string
 
def sifre_uret(uzunluk):
    karakterler =  string.ascii_letters + string.digits + string.punctuation
    sifre = ''.join(random.choice(karakterler) for i in range(uzunluk))
    return sifre
 

uzunluk_giris = input("Şifre Uzunluğunu Girin!")
print(sifre_uret(int(uzunluk_giris)))
