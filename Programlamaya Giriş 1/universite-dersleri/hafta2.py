print('Bilgisayar Teknolojileri Bölümü')
print("Bilgisayar Teknolojileri Bölümü")
print("""Bilgisayar Teknolojileri Bölümü""")

a = "Merhaba"
print(a)

naber = "Naber iyi misin ?"
print(naber)

# --- Stringleri İndeksleme ve Parçalama ---
# Slayt 4 ve 5: "emre" ve "Python Programlama Dili" üzerinden indeks denemeleri
isim = "emre"
print(isim[0])  # 'e'
print(isim[1])  # 'm'
print(isim[2])  # 'r'
print(isim[3])  # 'e'

metin = "Python Programlama Dili"
print(metin[4:10])  # 'on Pro' (4. indeksten 10. indekse kadar)
print(metin[:11])   # 'Python Prog' (Baştan 11. indekse kadar)
print(metin[3:])    # 'hon Programlama Dili' (3. indeksten sona kadar)

# --- Veri Tipi Dönüşümleri ---
# Slayt 6: Tamsayıyı Ondalıklıya Çevirme
sayi1 = 34
print(float(sayi1))  # 34.0

# Slayt 7: Ondalıklı Sayıyı Tamsayıya Çevirme (Tam kısmı alır)
sayi2 = 2.87
print(int(sayi2))  # 2

# Slayt 8: Sayıyı Stringe Çevirme ve len() ile Boyutunu Bulma
x = 98987213
x_str = str(x)
print(x_str)       # '98987213'
print(len(x_str))  # 8

# Slayt 9 ve 10: Düzgün formatlı Stringleri Sayıya Çevirme
a_str = "32434324324234"
print(int(a_str))

b_str = "3.144545"
print(float(b_str))

# --- Print Fonksiyonunun Özellikleri ve Özel Karakterler ---
# Slayt 11: Virgülle birden fazla değer basma
print(21, 12, 33, "Hale")
print("Raziye", "Hale", "Topaloglu")

# Slayt 12: \n (Alt satır) ve \t (Tab boşluğu) kullanımı
print("Raziye\nHale\nTopaloglu")
print("Ocak\tSubat\t\tMart")

# Slayt 13: sep parametresi ve Yıldızlı (*) Parametre
print(9, 19, 29, 39, 49, sep=".")
print(14, 10, 2024, sep="/")
print(*"Python", sep="\n")  # Harfleri ayırıp alt alta basar
print(*"TBMM", sep=".")      # T.B.M.M yazar

# --- type() Fonksiyonu ---
# Slayt 14: Veri tiplerini kontrol etme
print(type(256))       # <class 'int'>
print(type(10.98))     # <class 'float'>
print(type("hello"))   # <class 'str'>