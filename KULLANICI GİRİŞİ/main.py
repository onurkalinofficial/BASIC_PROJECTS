
print("********************\nSİSTEME HOŞ GELDİNİZ\n********************\n")

sys_kuladı = "admin"
sys_parola = "00000"

hak = 5

while True:
    kullanıcıadı = input("kullanıcı adı giriniz: ")
    parola = input("parola giriniz: ")

    if(kullanıcıadı != sys_kuladı and parola == sys_parola):
        print("hatalı kullanıcı adı... ")
        hak -= 1
        print("kalan deneme hakkınız: ",hak,)

    elif(kullanıcıadı == sys_kuladı and parola != sys_parola):
        print("hatalı parola... ")
        hak -= 1
        print("kalan deneme hakkınız: ", hak, )

    elif(kullanıcıadı != sys_kuladı and parola != sys_parola):
        print("kullanıcı adı ve parola hatalı tekrar deneyin... ")
        hak -= 1
        print("kalan deneme hakkınız: ", hak, )

    else:
        print("sisteme başarılı bir şekilde giriş yaptınız ")
        break
    if(hak == 0):
        print("giriş hakkınız bitmiştir, parolayı veya kullanıcı adını yenileyiniz.")
        break






