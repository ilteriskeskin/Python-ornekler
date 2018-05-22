import requests
from bs4 import BeautifulSoup

ans = int(input("1-Site Haritası Görüntüle\n2-Sitedeki Linkleri Görüntüle\n3-Çıkış\nSeçim yapınız: "))

while(1):
    
    if ans == 1:
        url = input("URL giriniz: ")
        page = requests.get(url)
        sitemap = BeautifulSoup(page.content, 'html.parser')                                                                                                                                                                                              
        urls = [element.text for element in sitemap.findAll('loc')]                                                                                                                                                                                       
        if len(urls) == 0:                                                                                                   
            print("sitemap.xml dosyası bulunamadı !")                                                                        
            exit(1)
            
        counter = int(input("sitemap.xml dosyasının ne kadarını görmek istiyorsunuz? Tamamı için 0 yazınız: "))               
        if counter == 0:                                                                                                     
            for i in range(len(urls)):                                                                                       
                print(i + 1, ") ", urls[i], "\n")
            break
        else:
            for i in range(counter):                                                                                         
                print(i + 1, ") ", urls[i])
            break
                
    elif ans == 2:
        url = input("URL giriniz: ")
        page = requests.get(url)
        print('Sayfa Durumu: %s' % page)
        
        link = BeautifulSoup(page.content, 'html.parser')

        urls = [element.text for element in link.findAll('a')]

        if len(urls) == 0:
            print("Link bulunamadı !")
            exit(1)

        counter = int(input("Görmek istediğiniz link sayısını giriniz. Tamamı için 0 yazınız: "))

        if counter == 0:
            for i in range(len(urls)):
                print(i + 1, ") ", urls[i], "\n")
            break
        else:
            for i in range(counter):
                print(i + 1, ") ", urls[i])
            break

    elif ans == 3:
        exit(1)
        
    else:
         print("Hatalı Seçim !")       
