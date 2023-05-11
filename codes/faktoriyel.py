def faktoriyel(x):
    if x == 0:
        return 1
    else:
        return x * faktoriyel(x-1)

sayi = input("Hesaplamak istediğiniz sayıyı girin: ")    
print("Girdiğiniz sayının faktöriyeli = ",faktoriyel(int(sayi)))