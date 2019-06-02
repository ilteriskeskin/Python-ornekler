class Kitap():
    pass

kitap = Kitap() # __init__ metodu çağırılır
print(kitap) # __str__ metodu çağırılır

del kitap # __del__ metodu çağırılır

class YeniKitap():
    def __init__(self, isim, yazar, sayfa):
        print('init fonksiyonu')
        self.isim = isim
        self.yazar = yazar
        self.sayfa = sayfa
    def __str__(self):
        return 'İsim: {}\nYazar: {}\nSayfa Sayısı: {}'.format(self.isim, self.yazar, self.sayfa)
    def __len__(self):
        return self.sayfa
    def __del__(self):
        print('Kitap objesi siliniyor......')

kitap = YeniKitap('Kitap1', 'Ali Keskin', 240)
print(kitap)
print(len(kitap))
del kitap
