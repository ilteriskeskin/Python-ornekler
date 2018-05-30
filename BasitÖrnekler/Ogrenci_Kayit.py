class Ogrenci:
    def __init__(self, isim, soyisim):
        self.isim = isim
        self.soyisim = soyisim

class Ogretmen:
    def __init__(self, isim, soyisim):
        self.isim = isim
        self.soyisim = soyisim

class Sinif:
    def __init__(self, sinif):
        self.sinif = sinif

class Sube:
    def __init__(self, sube):
        self.sube = sube

class Ders:
    def __init__(self, ders):
        self.ders = ders

isim = input("Öğrenci adı giriniz: ")
soyisim = input("Öğrenci soyadı giriniz: ")

e_isim = input("Öğretmen adı giriniz: ")
e_soyisim = input("Öğretmen soyadı giriniz: ")

o_sinif = input("Sınıfınızı giriniz: ")

o_sube = input("Şubenizi giriniz: ")

ogrenci = Ogrenci(isim, soyisim)
egitmen = Ogretmen(e_isim, e_soyisim)
sinif = Sinif(o_sinif)
sube = Sube(o_sube)

dersler = []

while True:
    o_ders = input("Almak istediğiniz dersi giriniz: ")

    ders = Ders(o_ders)
    dersler.append(o_ders)

    tercih = input("Yeni bir ders almak istiyor musunuz?: (e/h): ")

    if tercih == 'h':
        break

print("\nÖğrenci Adı: ", isim, soyisim)
print("Eğitmen Adı ", e_isim, e_soyisim)
print("Sınıfı: ", o_sinif)
print("Şubesi: ", o_sube)
print("Seçtiğiniz Dersler: ", dersler, "\n")

