#Bu girilen veriyi harflerine ayıran dizileri anlaşılır hale getirmeyi amaçlayan basit bir python programıdır.


dizi = input("Bir şeyler yazın\n==>")

print("Girdiğiniz verinin uzunluğu= ", len(dizi))

for i in range(len(dizi)):
    print("Girdiğiniz verinin {}. harfi: {}".format(i, dizi[i]))

print("Girdiğiniz dizinin ters çevrilmiş hali\n==> ", dizi[::-1])
