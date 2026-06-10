def sifre_kontrol(sifre):

    uzunluk = len(sifre)

    if uzunluk < 6:
        return "Zayıf Şifre"

    elif uzunluk < 10:
        return "Orta Güçlü Şifre"

    else:
        return "Güçlü Şifre"


sifre = input("Şifrenizi giriniz: ")

sonuc = sifre_kontrol(sifre)

print("Sonuç:", sonuc)