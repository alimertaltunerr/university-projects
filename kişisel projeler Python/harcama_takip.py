toplam = 0

while True:

    tutar = float(input("Harcama giriniz (cikis icin 0): "))

    if tutar == 0:
        break

    toplam += tutar

print("\nToplam Harcama:", toplam)

if toplam > 5000:
    print("Bu ay fazla harcama yaptiniz.")

else:
    print("Harcamalar kontrol altinda.")