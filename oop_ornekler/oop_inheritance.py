class Calisan():
    def __init__(self, isim, maas, departman):
        print('Çalışan sınıfının init fonksiyonu')
        self.isim = isim
        self.maas = maas
        self.departman = departman

    def bilgileri_goster(self):
        print('Çalışan sınıfının bilgileri:')
        print("""
        İsim     : {}
        Maaş     : {}
        Departman: {}
        """.format(self.isim, self.maas, self.departman))

    def departman_degistir(self, yeni_departman):
        self.departman = yeni_departman

class Yonetici(Calisan):
    def __init__(self, isim, maas, departman, kisi_sayisi):
        print('Yönetici sınıfının init fonksiyonu')
        self.isim = isim
        self.maas = maas
        self.departman = departman
        self.kisi_sayisi = kisi_sayisi

    def zam_yap(self, miktar):
        self.maas += miktar

yonetici = Yonetici('Ali İlteriş', 2000, 'Frontend')
yonetici.bilgileri_goster()
yonetici.departman_degistir('Backend')
yonetici.bilgileri_goster()

yonetici = Yonetici('Selamet Şamlı', 4000, 'Müdür')
yonetici.zam_yap(1000)
yonetici.bilgileri_goster()

yonetici = Yonetici('Uğur Yüce', 5500, 'Frontend', 10)

