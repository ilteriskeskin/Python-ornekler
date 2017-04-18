print simpleCalculator_ico
 
islem_numarasi_ico = """
(1) Toplama
(2) Çıkartma
(3) Çarpma
(4) Bölme
"""
 
print islem_numarasi_ico
 
star = "**********************************************";
 
print star 
 
islem_numarasi = input("İslem Numarasini Seciniz : ")
 
print star
 
def toplama():
 print star
 sayi_toplama_1 = input("Birinci Sayiyi Giriniz : ")
 sayi_toplama_2 = input("Ikinci Sayiyi Giriniz : ")
 print star
 print "Sonuç = " , sayi_toplama_1, " + ", sayi_toplama_2, "=", sayi_toplama_1 + sayi_toplama_2
 print star
 
def cikarma():
 print star
 sayi_cikartma_1 = input("Birinci Sayiyi Giriniz : ")
 sayi_cikartma_2 = input("Ikinci Sayiyi Giriniz : ")
 print star 
 print "Sonuç = " , sayi_cikartma_1, " - ", sayi_cikartma_2, "=", sayi_cikartma_1 - sayi_cikartma_2
 print star
 
def carpma():
 print star
 sayi_carpma_1 = input("Birinci Sayiyi Giriniz : ")
 sayi_carpma_2 = input("Ikinci Sayiyi Giriniz : ")
 print star 
 print "Sonuç = " , sayi_carpma_1, " X ", sayi_carpma_2, "=", sayi_carpma_1 * sayi_carpma_2
 print star
 
def bolme():
 print star
 sayi_bolme_1 = input("Birinci Sayiyi Giriniz : ")
 sayi_bolme_2 = input("Ikinci Sayiyi Giriniz : ")
 print star        
 print "Sonuç = " , sayi_bolme_1, " / ", sayi_bolme_2, "=", sayi_bolme_1 / sayi_bolme_2
 print star
 
if islem_numarasi == 1:
 toplama()
 
elif islem_numarasi == 2:
 cikarma()
 
elif islem_numarasi == 3:
 carpma()
 
elif islem_numarasi == 4:
 bolme()
 
else:
 if islem_numarasi != 1 and 2 and 3 and 4:  
 print star
 hata_mesaji = "Boyle bir islem numarasi yoktur! Tekrar deneyiniz.";
 print hata_mesaji
 print star
