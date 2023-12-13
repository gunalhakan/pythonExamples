'''
Klavyeden 0 girilene kadar girilen sayıların adedini bulan
bu sayıları toplayan ve sayıların ortalamasını bulup ekrana yazdıran programı yazınız.
'''
sayac = 0
toplam = 0
ortalama = 0 
while True:
    sayi = int(input("Sayı girmeyi durdurmak için 0 giriniz : "))
    if sayi == 0 : 
        break
     
    sayac += 1
    toplam = toplam + sayi
    ortalama = toplam / sayac


print("Girdiğiniz sayıların adeti : ", sayac )
print("Girdiğiniz sayıların toplamı : ", toplam )
print("Girdiğiniz sayıların ortalaması : ", ortalama )

