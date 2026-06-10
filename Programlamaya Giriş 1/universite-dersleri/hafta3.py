# --- Liste Oluşturma ve type/len Sorgulama ---
# Listeler köşeli parantez içine veriler konarak oluşturulabilir[cite: 649].
liste = ["Hale", 48, "Merhaba", 3.14, 8]
print(liste)  # Çıktı: ['Hale', 48, 'Merhaba', 3.14, 8] [cite: 652]

liste2 = ["sen", 12, 23, 0.87, "ogrencisin"]
print(liste2)  # Çıktı: ['sen', 12, 23, 0.87, 'ogrencisin'] [cite: 657]

liste3 = []
print(liste3)  # Boş liste çıktısı [cite: 661]

print(type(liste))  # Veri tipi sorgulama 'list' döner [cite: 663]
print(len(liste2))  # Eleman sayısı sorgulama 5 döner [cite: 668, 670]

# Bir string list() fonksiyonu ile listeye dönüştürülebilir[cite: 667].
harf_listesi = list("Merhaba")
print(harf_listesi)  # Çıktı: ['M', 'e', 'r', 'h', 'a', 'b', 'a'] [cite: 676, 677, 678]

# --- Listeleri İndeksleme ve Parçalama ---
# Listeleri indeksleme ve parçalama stringlerle birebir aynıdır[cite: 690, 692, 695].
sayi_listesi = [2, 3, 4, 5, 6, 7, 8, 9, 10]  # Slayttaki liste [cite: 682]
print(sayi_listesi[2])   # Çıktı: 4 [cite: 687, 689]
print(sayi_listesi[8])   # Çıktı: 10 [cite: 691, 694]
print(sayi_listesi[-1])  # Sonuncu eleman çıktısı: 10 [cite: 700, 701, 702]
print(sayi_listesi[2:])  # Çıktı: [4, 5, 6, 7, 8, 9, 10] [cite: 710, 711]
print(sayi_listesi[:7])  # Çıktı: [2, 3, 4, 5, 6, 7, 8] [cite: 713, 714]
print(sayi_listesi[2:7]) # Çıktı: [4, 5, 6, 7, 8] [cite: 715, 716]

# --- Temel Liste İşlemleri ve Metodları ---
# Bir listeyi birbirine toplama işlemi stringlerdeki gibi yapılabilir[cite: 719].
liste1 = [2, 8, "Mehtap"]
liste2 = [0.89, 45, 1]
print(liste1 + liste2)  # Çıktı: [2, 8, 'Mehtap', 0.89, 45, 1] [cite: 724]

# Listelerdeki elemanlar direkt olarak değiştirilebilir[cite: 721].
meyve_listesi = ["Eda", 45, 1, "Hale"]
meyve_listesi[0] = "Eda"
print(meyve_listesi)  # Çıktı: ['Eda', 45, 1, 'Hale'] [cite: 724]

# Bir listeyi bir tamsayıyla çarpabiliriz[cite: 722].
print(meyve_listesi * 3)  # Liste tamamen değişmez, geçici çoğaltır[cite: 722, 724].

# Append metodu verdiğimiz değeri listeye eklememizi sağlar[cite: 727, 729].
islem_listesi = [2, 9.98, "Hale"]
islem_listesi.append(8)
islem_listesi.append("Eda")
print(islem_listesi)  # Çıktı: [2, 9.98, 'Hale', 8, 'Eda'] [cite: 732]

# Pop metodu içine değer vermezsek son elemanı, değer verirse o indeksi atar[cite: 730, 731].
print(islem_listesi.pop(2))  # 'Hale' elemanını atar ve ekrana basar [cite: 731, 733, 734]
print(islem_listesi.pop())   # 'Eda' elemanını atar ve ekrana basar [cite: 731, 736, 737]

# Sort metodu listenin elemanlarını sıralamamızı sağlar[cite: 740, 741].
karisik_liste = [2, 1, 0.87, 98, 67]
karisik_liste.sort()
print(karisik_liste)  # Küçükten büyüğe sıralar [cite: 751, 752, 753]

karisik_liste.sort(reverse=True)
print(karisik_liste)  # Büyükten küçüğe sıralar [cite: 745, 754, 755]

sehirler = ["Karaman", "Muğla", "Antalya", "Zonguldak", "Aydin"]
sehirler.sort()
print(sehirler)  # Alfabetik sıralar [cite: 757, 758, 759]

# Bir listenin içinde başka bir liste bulundurmaya iç içe listeler denir[cite: 761, 762].
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = [7, 8, 9]
yeni_liste = [l1, l2, l3]
print(yeni_liste)  # Çıktı: [[1, 2, 3], [4, 5, 6], [7, 8, 9]] [cite: 767, 768]

# --- Demetler (Tuplelar) ---
# Demetler listelere benzer ancak farkları değiştirilemez oluşudur[cite: 770, 771].
demet = (1, 9, 8, 12, "kedi")
print(demet)  # Çıktı: (1, 9, 8, 12, 'kedi') [cite: 775, 777, 778]
print(type(demet))  # Veri tipi 'tuple' olarak döner [cite: 780, 782]
print(len(demet))   # Eleman sayısı 5 döner [cite: 784, 786]
print(demet[1:])    # Çıktı: (9, 8, 12, 'kedi') [cite: 788, 789]
print(demet[-1])    # Çıktı: 'kedi' [cite: 791, 793]
print(demet[::-1])  # Çıktı: ('kedi', 12, 8, 9, 1) [cite: 795, 796]

# Demet Metodları
# Index metoduyla elemanın hangi indekste olduğunu buluruz[cite: 798, 800].
print(demet.index("kedi"))  # Çıktı: 4 [cite: 801, 803]

# Count metoduyla içine verdiğimiz değerin kaç defa geçtiğini buluruz[cite: 798, 800].
tekrar_demeti = (2, 2, 3, 8, 8, 8, 9, 89, 89, 12, 12, 13, 2, 89)
print(tekrar_demeti.count(2))   # Çıktı: 3 [cite: 806, 808]
print(tekrar_demeti.count(89))  # Çıktı: 3 [cite: 810, 812]
print(tekrar_demeti.count(12))  # Çıktı: 2 [cite: 814, 816]