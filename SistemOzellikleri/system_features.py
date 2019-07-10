import os
import processor_info, battery, mem, disk

while(1):

    print('1-view operating system: ')
    print('2-view detailed operating system (GNU/Linux only):')
    print('3-view system information: ')
    print('4-exit: ')
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
            print('Your sistem not  GNU/Linux!')
            print('--------------------------\n')

    elif secim == 3:

        while(1):
            yeni = int(input('1-Processor information\n2-RAM information\n3-Disk information\n4-Battery information\n5-Exit\n==> '))

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
                print('Incorrect selection!')
    elif secim == 4:
        exit(1)

    else:
        print('Incorrect selection!')
