harcamalar = []

while True:

    print("\n1- Harcama Ekle")
    print("2- Harcamaları Göster")
    print("3- Toplam Harcama")
    print("4- Çıkış")

    secim = input("Seçiminiz: ")

    if secim == "1":

        miktar = float(input("Harcama miktarı: "))
        harcamalar.append(miktar)

        print("Harcama eklendi.")

    elif secim == "2":

        print("Harcamalar:")
        print(harcamalar)

    elif secim == "3":

        toplam = 0

        for harcama in harcamalar:
            toplam += harcama

        print("Toplam Harcama:", toplam)

    elif secim == "4":

        print("Program sonlandırıldı.")
        break

    else:
        print("Hatalı seçim.")