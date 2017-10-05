soru1 = int(input("Bulunduğun oda hangisi? (1/2): "))

if soru1 == 1:
    soru2 = input("Bulunduğun oda temiz mi? (e/h): ")
    if soru2 == 'e':
        soru3 = input("2 nolu odayı kontrol et. Temiz mi? (e/h): ")
        if soru3 == 'e':
            print("Odalar temiz vakumu çalıştırma.")
        elif soru3 == 'h':
            print("2 nolu oda kirli temizle.")
            print("Odalar artık temiz.")
        else:
            print("Seçim hatası.")
    elif soru2 == 'h':
        print("Bulunduğun odayı temizle.")
        soru4 = input("2 nolu odayı kontrol et. Temiz mi? (e/h): ")
        if soru4 == 'e':
            print("Odalar temiz vakumu çalıştırma.")
        elif soru4 == 'h':
            print("2 nolu odayı temizle.")
            print("Odalar artık temiz.")
        else:
            print("Seçim hatası.")
    else:
        print("Seçim hatası.")
elif soru1 == 2:
    soru5 = input("Bulunduğun oda temiz mi? (e/h): ")
    if soru5 == 'e':
        soru6 = input("1 nolu odayı kontrol et. Temiz mi? (e/h): ")
        if soru6 == 'e':
            print("Odalar temiz vakumu çalıştırma.")
        elif soru6 == 'h':
            print("1 nolu oda kirli temizle.")
            print("Odalar artık temiz.")
        else:
            print("Seçim hatası.")
    elif soru5 == 'h':
        print("Bulunduğun odayı temizle.")
        soru7 = input("1 nolu odayı kontrol et. Temiz mi? (e/h): ")
        if soru7 == 'e':
            print("Odalar temiz vakumu çalıştırma.")
        elif soru7 == 'h':
            print("1 nolu odayı temizle.")
            print("Odalar artık temiz.")
        else:
            print("Seçim hatası.")
    else:
        print("Seçim hatası.")
else:
    print("Seçim hatası.")
