ByOne = [
"sifir",
"bir",
"iki",
"uc",
"dort",
"bes",
"alti",
"yedi",
"sekiz",
"dokuz",
"on",
"on bir",
"on iki",
"on uc",
"on dort",
"on bes",
"on alti",
"on yedi",
"on sekiz",
"on dokuz"
]

ByTen = [
"sifir",
"on",
"yirmi",
"otuz",
"kirk",
"elli",
"altmis",
"yetmis",
"seksen",
"doksan"
]

zGroup = [
"",
"bin",
"milyon",
"milyar",
"trilyon",
"katrilyon",
"kentilyon",
"seksilyon",
"septilyon",
"oktilyon",
"nonilyon",
"desilyon",
"undesilyon",
"dodesilyon",
"tredesilyon",
"kattuordesilyon",
"kendesilyon",
"seksdesilyon",
"septendesilyon",
"oktodesilyon",
"novemdesilyon"
]

strNum = raw_input("Bir sayi giriniz: ")

def subThousand(inputNum):
    num = int(inputNum)
    if 0 <= num <= 19:
        return ByOne[num]
    elif 20 <= num <= 99:
        if inputNum[-1] == "0":
            return ByTen[int(inputNum[0])]
        else:
            return ByTen[int(inputNum[0])] + " " + ByOne[int(inputNum[1])]
    elif 100 <= num <= 999:
        rem = num % 100
        dig = num / 100
        if rem == 0:
            return ByOne[dig] + " yuz"
        else:
            if ByOne[dig] != 1:
                return ByOne[dig] + " yuz " + subThousand(str(rem))
            else:
                return " yuz " + subThousand(str(rem))
            
def thousandUp(inputNum):
    num = int(inputNum)
    arrZero = splitByThousands(num)
    lenArr = len(arrZero) - 1
    resArr = []
    for z in arrZero[::-1]:
        wrd = subThousand(str(z)) + " "
        zap = zGroup[lenArr] + ", "
        if wrd == " ":
            break
        elif wrd == "sifir ":
            wrd, zap = "", ""
        resArr.append(wrd + zap)
        lenArr -= 1
    res = "".join(resArr).strip()
    if res[-1] == ",": res = res[:-1]
    return res

def splitByThousands(inputNum):
    num = int(inputNum)
    arrThousands = []
    while num != 0:
        arrThousands.append(num % 1000)
        num /= 1000
    return arrThousands

intNum = int(strNum)

if intNum < 0:
    print "Eksi",
    intNum *= -1
    strNum = strNum[1:]

if intNum < 1000:
    print subThousand(strNum)
else:
    print thousandUp(strNum)
