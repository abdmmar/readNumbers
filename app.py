from functions import satuan, belasan, puluhan, ratusan, ribuan, puluhanRibu, ratusanRibu

# MAIN
def readNumbers(number):
    """Fungsi untuk membaca angka yang dimasukkan"""

    strNumber = str(number)
    lengthNum = len(strNumber)
    firstNumber = int(strNumber[0])

    if(number == 0):
        return 'Nol'
    elif(number < 12):
        angkaSatuan = satuan(strNumber)
        return angkaSatuan
    elif(lengthNum == 2):
        if( firstNumber == 1):
            stringBelasan = belasan(strNumber)
            return stringBelasan
        else:
            angkaPuluhan = strNumber
            stringPuluhan = puluhan(angkaPuluhan)
            return stringPuluhan
    elif(lengthNum == 3):
        stringRatusan = ratusan(strNumber)
        return stringRatusan
    elif(lengthNum == 4):
        stringRibuan = ribuan(strNumber)
        return stringRibuan
    elif(lengthNum == 5):
        stringPuluhanRibu = puluhanRibu(strNumber)
        return stringPuluhanRibu
    elif(lengthNum == 6):
        stringRatusanRibu = ratusanRibu(strNumber)
        return stringRatusanRibu

result = readNumbers(0)

print('------------------------------------------')
print(result)
print('------------------------------------------')

# END MAIN