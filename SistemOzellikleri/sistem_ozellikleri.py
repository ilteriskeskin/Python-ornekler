import os
import psutil

print('1-İsletim sistemi görüntülüme: ')
print('2-Ayrıntılı işletim sistemi görüntüleme (Yalnızca GNU/Linux sistemler):')
print('3-Sistem bilgilerini görüntüleme: ')
print('4-Çıkış: ')

while(1):

    secim = int(input('Giriniz: '))

    if secim == 1:
        print(os.name)

    elif secim == 2:

        if os.name == 'posix':
            print(os.uname())

        else:
            print('Sisteminiz GNU/Linux değil !')

    elif secim == 3:
        print('Henüz hazır değil')

    elif secim == 4:
        exit(1)

    else:
        print('Hatalı seçim !')
