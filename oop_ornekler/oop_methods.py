class Yazilimci():
    def __init__(self, isim, soyisim, maas):
        self.isim = isim
        self.soyisim = soyisim
        self.maas = maas

    def bilgileri_goster(self):
        print("""
        Yazılımcı objesinin özellikleri
        İsim   : {}
        Soyisim: {}
        Maaş   : {}""".format(self.isim, self.soyisim, self.maas))

    def zam_yap(self, miktar):
        print('Zam yapılıyor...')
        self.maas += miktar

    def isim_guncelle(self, isim):
        self.isim = isim

yazilimci = Yazilimci("Ali İlteriş", "Keskin", 1000)
yazilimci.bilgileri_goster()
yazilimci.isim_guncelle('Ali')
yazilimci.bilgileri_goster()
yazilimci.zam_yap(500)
yazilimci.bilgileri_goster()

