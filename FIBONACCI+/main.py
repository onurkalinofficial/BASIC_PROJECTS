print("************")
print("Hoş Geldiniz")
print("************")


while True:
    n = int(input("Eleman sayısı giriniz: "))

    if n <= 0:
        print("pozitif sayı giriniz ")
        continue

    a, b = 0, 1
    i = 0

    print("Fibonacci dizisi: ")

    while True:
        print(a, end=" ")
        a, b = b, a + b
        i += 1

        if i == n:
            break

    break
