##### Günlük Kenara Koyulan Para Miktarını İnceleme Amaçlı Üretilmiştir #####

import time

print("---------------------------------")
print("KUMBARA UYGULAMASINA HOŞ GELDİNİZ")
print("---------------------------------")

while True:
    giris = int(input("\n\n1- Kumbaraya Para Ekle \n2- Biriken Parayı Görüntüle \n3- Çıkış \n==> "))
    if giris == 1:
        while True:
            f = open("kumbara.txt", "a")
            para = input("Bu gün kenara koyduğunuz para miktarını TL cinsinden giriniz: ")
            f.write(para)
            f.write("\t")
            f.write(time.ctime())
            f.write("\n")
            f.close()
            cikis = input("Çıkmak istiyorsanız 'q' Devam etmek için ENTER: ")
            if cikis == 'q':
                break
            else:
                continue
    elif giris == 2:
        f = open("kumbara.txt")
        print(f.read())
    elif giris == 3:
        print("Çıkış işlemi gerçekleştiriliyor...")
        time.sleep(3)
        print("İşlem başarılı bir şekilde sonlandı.\n\n")
        break        
    else:
        print("Seçim hatası.\n")
