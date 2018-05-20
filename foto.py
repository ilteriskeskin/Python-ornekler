import os
import time

while(1):
    if os.path.isfile('a.jpg'):
        print("Görüntü bulundu açılıyor, bekleyiniz...")
        time.sleep(2)
        os.system("xdg-open a.jpg")
        break
    else:
        print("Böyle bir dosya yok, tekrar deneniyor.")
        time.sleep(2)
