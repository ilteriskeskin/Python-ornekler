      kullaniciAdi = input('Kullanici adinizi giriniz: ') #kullanici adi girisini aldik.
      parola       = input('Parolanizi giriniz       : ') #parola girisini aldik.

      toplamUzunluk = len(kullaniciAdi) + len(parola) #len fonksiyonu ile karakter sayisini ogrendik.

      mesaj = 'Kullanici adi ve parolaniz toplam {} karakterden olusuyor.' #mesajimizi yazdirdik.

      print(mesaj.format(toplamUzunluk)) #format fonksiyonu ile toplam karakter sayisini yazdirdik.

      if toplamUzunluk > 25: #toplam karakter sayisinin 25 ten kucuk olma kosulunu koyduk.
          print('Kullanici adiniz ve parolaniz toplam 25 karakteri gecmemeli')
      else:
          print('Sisteme kaydiniz alinmistir. Lütfen Giris yapiniz.')

      kullaniciAdi1 = input('Kullanici Adi: ')
      parola1       = input('Parola       : ')
      
      if kullaniciAdi1 == kullaniciAdi and parola1 == parola: #and parametresi ile kullanici adi ve
          print('Sisteme girisiniz basarili!') 		    #parolanin dogrulugunu test ettik.
      else:
          print('Kullanici Adi veya Parola Hatali')
