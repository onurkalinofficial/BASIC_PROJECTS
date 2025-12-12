print("Hesap Makinesine Hoş Geldiniz!")

sayı1 = float(input("ilk sayıyı giriniz: "))
sayı2 = float(input("ikinci sayıyı giriniz: "))

işlem = input("yapacağınız işlemin türünü seçiniz: ")

if işlem == "/" :
    print("bölme işleminin sonucu: ",sayı1/sayı2,)

elif işlem == "*" :
    print("çarpma işleminin sonucu: ",sayı1*sayı2,)

elif işlem == "+" :
    print("toplama işleminin sonucu: ",sayı1+sayı2,)

elif işlem == "-" :
    print("çıkarma işleminin sonucu: ",sayı1-sayı2,)

print("İYİ GÜNLER DİLERİZ")

