class Araba():
    def __init__(self, model, renk):
        print('init fonksiyonu çağırıldı')
        self.model = model
        self.renk = renk

araba1 = Araba('Land Rover', 'Siyah')
print(araba1)

araba2 = Araba('Ford', 'Gri')
print(araba2)

print(araba1.model)
print(araba2.model)
