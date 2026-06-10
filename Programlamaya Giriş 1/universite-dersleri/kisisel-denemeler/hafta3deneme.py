test_listesi = ["Antalya", 19, 2026, 3.14]
print(type(test_listesi))
print(len(test_listesi))

# Listeyi tersten parçalama denemesi
rakamlar = [0, 1, 2, 3, 4, 5]
print(rakamlar[::-1])
print(rakamlar[-3:])

# Append ve pop kullanımı 
hobiler = ["resim", "oyun"]
hobiler.append("eğlence")
print(hobiler)
silinen = hobiler.pop(0)
print(silinen)
print(hobiler)

# Sayı ve string listelerinde sıralama 
notlar = [85, 45, 95, 70]
notlar.sort()
print(notlar)

isimler = ["mert", "ali", "ben"]
isimler.sort()
print(isimler)

# İç içe listeden eleman çekme 
matris = [[1, 2], [3, 4]]
print(matris[0])
print(matris[0][1])

# Tuple oluşturma ve metod denemeleri
veriler = (5, 5, 10, 15, "test")
print(veriler[0])
print(veriler.index("test"))
print(veriler.count(5))
