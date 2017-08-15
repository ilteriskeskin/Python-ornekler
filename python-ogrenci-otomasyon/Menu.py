from Student import Student

def showMenu():
    try:
        print("\n","#"*5, "Seçim Yapın", "#"*5)
        print("1) Öğrenci ekle")
        print("2) Öğrenci bul")
        print("3) Öğrenci sil")
        print("4) Öğrenci bilgilerini güncelle")
        print("5) Tüm öğrencileri görüntüle")

        secim = input("Seçim yap: ")
        if secim == "q" or secim == "exit":
            exit(0)

        secim = int(secim)

        if secim == 1:
            ad = input("Adı: ")
            soyad = input("Soyad: ")
            sehir = input("Yaşadığın şehir: ")
            okul = input("Okulun: ")
            dogum = int(input("Doğum tarihi: "))
            mail = input("Mail adresi: ")
            tel = input("Telefon numarası: ")
            egitim = []
            while True:
                egt = input("Öğrenmek istediğin teknolojiler: ")
                if egt == "":
                    break
                egitim.append(egt)

            ogrenci = {"dogum_tarihi": dogum, "egitim": egitim, "okul": okul, "soyadi": soyad,
                       "sehir": sehir, "tel": tel, "adi": ad, "mail": mail}

            std = Student()
            std.addStudent(ogrenci)
            print("#"*5,"Öğrenci Eklendi", "#"*5)
            showMenu()
        elif secim == 2:
            ad = input("Aradığınız öğrencinin adı: ")
            soyad = input("Aradığınız öğrencinin soyadı: ")

            std = Student()
            std.viewStudent(ad,soyad)
            showMenu()
        elif secim == 3:
            ad = input("Silinecek öğrencinin adı: ")
            soyad = input("Silinecek öğrencinin soyadı: ")

            std = Student()
            std.deleteStudent(ad,soyad)
            print("#"*5,"Öğrenci silindi", "#"*5)
            showMenu()
        elif secim == 4:
            print("\nGüncellenecek öğrencinin bilgilerini girin.")

            ad = input("Adı: ")
            soyad = input("Soyad: ")

            sehir = input("\nYaşadığın şehir: ")
            okul = input("Okulun: ")
            dogum = int(input("Doğum tarihi: "))
            mail = input("Mail adresi: ")
            tel = input("Telefon numarası: ")
            egitim = []
            while True:
                egt = input("Öğrenmek istediğin teknolojiler: ")
                if egt == "":
                    break
                egitim.append(egt)

            ogrenci = {"dogum_tarihi": dogum, "egitim": egitim, "okul": okul, "soyadi": soyad,
                       "sehir": sehir, "tel": tel, "adi": ad, "mail": mail}

            std = Student()
            std.updateStudent(ad,soyad, ogrenci)
            print("#" * 5, "Öğrenci güncellendi", "#" * 5)
            showMenu()
        elif secim == 5:
            std = Student()
            std.allStudent()
            showMenu()
        else:
            print("#"*5,"Geçersiz işlem","#"*5)
    except Exception as h:
        print("#"*5,"Sayı gir.","#"*5)

showMenu()