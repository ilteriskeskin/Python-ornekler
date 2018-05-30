import os
import processor_info, battery, mem, disk

while(1):

    print('1-İsletim Sistemi Görüntülüme: ')
    print('2-Ayrıntılı İşletim Sistemi Görüntüleme (Yalnızca GNU/Linux Sistemler):')
    print('3-Sistem Bilgilerini Görüntüleme: ')
    print('4-Çıkış: ')
    secim = int(input('==> '))

    if secim == 1:
        print('--------------------------')
        print(os.name)
        print('--------------------------\n')

    elif secim == 2:

        if os.name == 'posix':
            print('--------------------------')
            print(os.uname())
            print('--------------------------\n')

        else:
            print('--------------------------')
            print('Sisteminiz GNU/Linux değil !')
            print('--------------------------\n')

    elif secim == 3:

        while(1):
            yeni = int(input('1-İşlemci Bilgileri\n2-RAM Bilgileri\n3-Disk Bilgileri\n4-Pil Bilgileri\n5-Çıkış\n==> '))

            if yeni == 1:
                print('--------------------------')
                print(processor_info.view())
                print('--------------------------\n')

            elif yeni == 2:
                print('--------------------------')
                mem.main()
                print('--------------------------\n')

            elif yeni == 3:
                print('--------------------------')
                disk.main()
                print('--------------------------\n')

            elif yeni == 4:
                print('--------------------------')
                battery.main()
                print('--------------------------\n')

            elif yeni == 5:
                exit(1)

            else:
                print('Hatalı seçim!')
        elif secim == 4:
            exit(1)

        else:
            print('Hatalı seçim !')
