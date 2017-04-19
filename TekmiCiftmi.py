bölünen = int(input("Bir sayi girin: "))
bölen = int(input("Bir sayi daha girin: "))

şablon = "{} sayısı {} sayısına tam".format(bölünen, bölen)

if bölünen % bölen == 0:
    print(şablon, "bölünüyor")
else:
    print(şablon, "bölünmüyor !")
