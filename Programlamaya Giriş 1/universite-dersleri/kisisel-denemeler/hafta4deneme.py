oyuncu_bilgi = {"isim": "Ali", "yas": 19, "sehir": "Antalya"}
print(oyuncu_bilgi)
print(oyuncu_bilgi["isim"])

# Sözlüğe veri ekleme ve güncelleme
oyuncu_bilgi["hobi"] = "resim çizmek"
oyuncu_bilgi["yas"] = 20
print(oyuncu_bilgi)

# Test
print(oyuncu_bilgi.keys())
print(oyuncu_bilgi.values())
print(oyuncu_bilgi.items())

# Temel input alma
kullanici_adi = input("Kullanıcı adınızı girin: ")
print("Hoş geldin", kullanici_adi)

# Slayt 9'daki input string çarpma 
test_input = input("Bir şey yazın: ")
print(test_input * 4)

# Dönüşümlü input 
dogum_yili = int(input("Doğum yılınızı girin: "))
print("Hesaplanan Yaş:", 2026 - dogum_yili)
