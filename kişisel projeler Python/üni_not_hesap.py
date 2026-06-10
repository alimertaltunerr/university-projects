ad = input("Ogrenci adi: ")

vize = float(input("Vize notu: "))
final = float(input("Final notu: "))

ortalama = vize * 0.4 + final * 0.6

print("\n--- RAPOR ---")
print("Ogrenci:", ad)
print("Ortalama:", ortalama)

if ortalama >= 85:
    print("Durum: Basarili")
elif ortalama >= 60:
    print("Durum: Siniri Gecti")
else:
    print("Durum: Kaldi")

if final > vize:
    print("Yorum: Donem boyunca gelisim gostermis.")
else:
    print("Yorum: Final performansi dusuk.")