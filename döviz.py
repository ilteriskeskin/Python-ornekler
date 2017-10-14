import requests
import sys

url = "http://api.fixer.io/latest?base="

ilk_doviz = input("İlk Döviz: ")
ikinci_doviz = input("İkinci Döviz: ")
miktar = float(input("Miktar: "))

response = requests.get(url + ilk_doviz)

json_verisi = response.json()

try:
    print(json_verisi["rates"][ikinci_doviz] * miktar)
except KeyError:
    sys.stderr.write("Para birimlerini doğru giriniz.\n")
    sys.stderr.flush()
