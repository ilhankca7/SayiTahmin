import random
import time


print("""

SAYI TAHMİN OYUNU

1 ile 1000 arasındakş sayıları tahmin etme

""")


rastgele_sayi = random.randint(1,1000)
tahmin_hakki = 10

while True:
    tahmin=int(input("Tahmininiz:"))

    if (tahmin < rastgele_sayi ):
        print("Bilgiler sorgulanıyor...")
        time.sleep(1)

        print("Daha yüksek bir sayı deneyin.")

        tahmin_hakki -= 1

    elif (tahmin > rastgele_sayi ) :
        print("Bilgiler sorgulanıyor...")
        time.sleep(1)

        print("Daha düşük bir sayı deneyin.")

        tahmin_hakki -= 1
    else:
        print("Bigiler sorgulanıyor...")
        time.sleep(1)

        print("Tebrikler!Sayımız",rastgele_sayi)
        break

    if(tahmin_hakki== 0 ):
        print("Tahmin hakkkınız doldu.")
        print("Sayımız ",rastgele_sayi)
        break           












