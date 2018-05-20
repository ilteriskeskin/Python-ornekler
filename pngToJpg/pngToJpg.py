from PIL import Image
import os
import time

while(1):
    if os.path.isfile("a1.png"):
        print("Görüntü bulundu, formatı değiştiriliyor...")
        time.sleep(2)
        image = Image.open("a1.png")
        bg = Image.new("RGB", image.size, (255,255,255))
        bg.paste(image, (0,0), image)
        bg.save("new.jpg", quality = 95)
        print("Görüntü başarılı bir şekilde kaydedildi.")
        break
    else:
        print("Bulunduğunuz dizinde görüntü bulunamadı, görüntü bekleniyor...")
        time.sleep(2)
