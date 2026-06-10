kitaplar = []

while True:

    print("\n1- Kitap Ekle")
    print("2- Kitapları Listele")
    print("3- Son Kitabı Sil")
    print("4- Çıkış")

    secim = input("Seçiminiz: ")

    if secim == "1":

        kitap = input("Kitap adı: ")
        kitaplar.append(kitap)

        print("Kitap eklendi.")

    elif secim == "2":

        print("Kütüphanedeki Kitaplar:")

        for kitap in kitaplar:
            print("-", kitap)

    elif secim == "3":

        if len(kitaplar) > 0:
            silinen = kitaplar.pop()
            print("Silinen kitap:", silinen)
        else:
            print("Listede kitap yok.")

    elif secim == "4":
        break

    else:
        print("Hatalı seçim.")