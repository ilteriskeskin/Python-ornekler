import os

while(1):

    print("-------------------------------------------------------------------")
    print("1-Bulunduğun dizinin içindekileri gör")
    print("2-Dosya/dizin sil")
    print("3-Çıkış")
    print("-------------------------------------------------------------------")

    menu = input("Yapmak istediğiniz işlem menüsünü seçiniz: ")

    if menu == '1':
        print("\n\n-------------------------------------------------------------------")
        print("1-Dizinin içindekileri listele")
        print("2-Dizinin içindekileri detaylı listele")
        print("-------------------------------------------------------------------")

        ls = input("Bir menü seçiniz: ")

        if ls == '1':
            print(os.system("ls"))

        elif ls == '2':
            print(os.system("ls -lah"))

        else:
            print("Hatalı seçim")

    elif menu == '2':
            path = input("Silmek istediğiniz dosya/dizin adını yolu ile birlikte giriniz(/opt/local/dosya/dizin_adi): ")
            os.system("rm -r " + path)
            print("İşlem tamamlandı.")

    elif menu == '3':
        print("Çıkış işlemi gerçekleştiriliyor...")
        os.system("exit")
        break

    else:
        print("Hatalı seçim")
