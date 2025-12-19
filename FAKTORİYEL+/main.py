print("****************************************")
print("FAKTORİYEL HESAPLAMA ARACINA HOŞ GELDİNİZ")
print("Çıkmak için q'ya bas")
print("****************************************")

while True:
    sayı = input("Sayı giriniz: ")

    if sayı == "q":
        print("İyi günler dileriz")
        break

    try:
        sayı = int(sayı)
    except ValueError:
        print("Lütfen geçerli bir sayı giriniz!")
        continue

    if sayı < 0:
        print("Negatif sayıların faktöriyeli yoktur!")
        continue

    faktoriyel = 1
    for i in range(2, sayı + 1):
        faktoriyel *= i

    print("Faktöriyel:", faktoriyel)






