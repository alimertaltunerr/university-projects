# --- Sözlük Oluşturmak ---
sozluk1 = {"sıfır": 0, "bir": 1, "iki": 2, "üç": 3}
print(sozluk1)

sozluk2 = {}
print(sozluk2)

sozluk3 = dict()
print(sozluk3)

# --- Sözlük Değerine Erişmek ve Değer Eklemek ---
sozluk = {"sıfır": 0, "bir": 1, "iki": 2, "üç": 3}
print(type(sozluk))
print(sozluk["bir"])
print(sozluk["üç"])

# Yeni anahtar-değer ekleme
sozluk["beş"] = 5
sozluk["adiniz"] = "Hale"
print(sozluk)

# --- İç İçe Sözlükler ---
a = {
    "sayılar": {"bir": 1, "iki": 2, "üç": 3},
    "meyveler": {"kiraz": "yaz", "portakal": "kış", "erik": "yaz"}
}
print(a["sayılar"]["bir"])
print(a["meyveler"]["kiraz"])

# --- Dictionary Metodları ---
yeni_sozluk = {"bir": 1, "iki": 2, "üç": 3}
print(yeni_sozluk.values())
print(yeni_sozluk.keys())
print(yeni_sozluk.items())

# --- Kullanıcıdan Girdi Alma (Input) ---
input()
input(25)
input('bir isim giriniz')

x = input("Lütfen bir sayı giriniz:")
print("Kullanıcının girdiği değer:", x)

y = input("lütfen adinizi giriniz:")
print(y)

z = input("Yaşinizi belirtiniz:")
print("Hale hocanin yaşi:", z)
print(type(z))

# Input string döndürdüğü için çarpma işlemi yan yana yazar
print(z * 3)

# --- Input Değerini Sayıya Çevirme ---
ax = int(input("lütffen bir sayi giriniz:"))
print(ax * 5)

ay = float(input("lütffen bir sayi giriniz:"))
print(ay * 6)

# --- Slayt Sonundaki Sayı Toplama Örneği ---
sayi1 = int(input("Birinci Sayı:"))
sayi2 = int(input("İkinci Sayı:"))
sayi3 = int(input("Üçüncü Sayı:"))
print("Toplamları:", sayi1 + sayi2 + sayi3)