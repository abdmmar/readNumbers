# BASE NUMBERS
satu_sampai_sebelas = {
    '0' : '',
    '1' : 'Satu',
    '2' : 'Dua',
    '3' : 'Tiga',
    '4' : 'Empat',
    '5' : 'Lima',
    '6' : 'Enam',
    '7' : 'Tujuh',
    '8' : 'Delapan',
    '9' : 'Sembilan',
    '10' : 'Sepuluh',
    '11' : 'Sebelas',
}

# FUNCTIONS
def satuan(satuan):
    """Fungsi untuk mencetak angka satuan"""
    angkaSatuan = satu_sampai_sebelas[satuan]

    return angkaSatuan

def belasan(belasan):
    """Fungsi untuk mencetak angka belasan"""
    angkaBelasan = satu_sampai_sebelas[belasan[1]]

    stringBelasan = angkaBelasan + ' Belas' 
    return stringBelasan

def puluhan(puluhan):
    """Fungsi untuk mencetak angka puluhan"""
    angkaPuluhan = satu_sampai_sebelas[puluhan[0]]
    angkaSatuan = satu_sampai_sebelas[puluhan[1]]

    if(int(puluhan[1]) != 0):
        stringPuluhan = angkaPuluhan + ' Puluh ' + angkaSatuan + ' '
    else:
        stringPuluhan = angkaPuluhan + ' Puluh ' + angkaSatuan
        
    return stringPuluhan

def ratusan(ratusan):
    """Fungsi untuk mencetak angka ratusan"""

    angkaRatusan = ratusan[0] # angka ke-1
    nilaiPuluhan = int(ratusan[1:]) # angka ke-2
    angkaPuluhan = str(nilaiPuluhan) # angka ke-2 dalam string

    if(int(angkaRatusan) == 1):
        if(nilaiPuluhan < 12):
            stringSatuan = satuan(angkaPuluhan)
            stringRatusanSatuan = 'Seratus ' + stringSatuan
            return stringRatusanSatuan
        elif(nilaiPuluhan < 20):
            stringBelasan = belasan(angkaPuluhan)
            stringRatusanBelasan = 'Seratus ' + stringBelasan
            return stringRatusanBelasan
        else:
            stringPuluhan = puluhan(angkaPuluhan)
            stringRatusanPuluhan = 'Seratus ' + stringPuluhan
            return stringRatusanPuluhan
    else:
        strRatusan = satuan(angkaRatusan)
        stringRatusan = strRatusan + ' Ratus '

        if(nilaiPuluhan < 12):
            stringSatuan = satuan(angkaPuluhan)
            stringRatusanSatuan = stringRatusan + stringSatuan
            return stringRatusanSatuan
        elif(nilaiPuluhan < 20):
            stringBelasan = belasan(angkaPuluhan)
            stringRatusanBelasan = stringRatusan + stringBelasan
            return stringRatusanBelasan
        else:
            stringPuluhan = puluhan(angkaPuluhan)
            stringRatusanPuluhan = stringRatusan + stringPuluhan
            return stringRatusanPuluhan

def ribuan(ribuan):
    """Fungsi untuk mencetak angka ribuan"""

    angkaRibuan = ribuan[0] # angka ke-1
    nilaiRatusan = int(ribuan[1:]) # 3 angka terakhir
    angkaRatusan = str(nilaiRatusan) # 3 angka terakhir dalam string

    if(int(angkaRibuan) == 1):
        if(nilaiRatusan < 12):
            stringSatuan = satuan(angkaRatusan)
            stringRibuanSatuan = 'Seribu ' + stringSatuan
            return stringRibuanSatuan
        elif(nilaiRatusan < 20):
            stringBelasan = belasan(angkaRatusan)
            stringRibuanBelasan = 'Seribu ' + stringBelasan
            return stringRibuanBelasan
        elif(nilaiRatusan < 100):
            stringPuluhan = puluhan(angkaRatusan)
            stringRibuanPuluhan = 'Seribu ' + stringPuluhan
            return stringRibuanPuluhan
        else:
            stringRatusan = ratusan(angkaRatusan)
            stringRibuanRatusan = 'Seribu ' + stringRatusan
            return stringRibuanRatusan
    else:
        strRibuan = satuan(angkaRibuan)
        stringRibuan = strRibuan + ' Ribu '

        if(nilaiRatusan < 12):
            stringSatuan = satuan(angkaRatusan)
            stringRibuanSatuan = stringRibuan + stringSatuan
            return stringRibuanSatuan
        elif(nilaiRatusan < 20):
            stringBelasan = belasan(angkaRatusan)
            stringRibuanBelasan = stringRibuan + stringBelasan
            return stringRibuanBelasan
        elif(nilaiRatusan < 100):
            stringPuluhan = puluhan(angkaRatusan)
            stringRibuanPuluhan = stringRibuan + stringPuluhan
            return stringRibuanPuluhan
        else:
            stringRatusan = ratusan(angkaRatusan)
            stringRibuanRatusan = stringRibuan + stringRatusan
            return stringRibuanRatusan

def puluhanRibu(ribuan):
    """Fungsi untuk mencetak angka puluhan ribu"""

    nilaiPuluhanRibuan = ribuan[0:2] # 2 angka pertama
    nilaiRibuan = int(ribuan[2:]) # 3 angka terakhir ubah ke int
    angkaRibuan = str(nilaiRibuan) # angka terakhir dalam string

    if(int(nilaiPuluhanRibuan) < 12):
        angkaDepan = satuan(nilaiPuluhanRibuan)
        strDepan = angkaDepan + ' Ribu '

        if(nilaiRibuan < 12):
            stringSatuan = satuan(angkaRibuan)
            stringRibuanSatuan = strDepan + stringSatuan
            return stringRibuanSatuan
        elif(nilaiRibuan < 20):
            stringBelasan = belasan(angkaRibuan)
            stringRibuanBelasan = strDepan + stringBelasan
            return stringRibuanBelasan
        elif(nilaiRibuan < 100):
            stringPuluhan = puluhan(angkaRibuan)
            stringRibuanPuluhan = strDepan + stringPuluhan
            return stringRibuanPuluhan
        else:
            stringRatusan = ratusan(angkaRibuan)
            stringRibuanRatusan = strDepan + stringRatusan
            return stringRibuanRatusan

    elif(int(nilaiPuluhanRibuan) < 20):
        angkaDepan = belasan(nilaiPuluhanRibuan)
        strDepan = angkaDepan + ' Ribu '
        
        if(nilaiRibuan < 12):
            stringSatuan = satuan(angkaRibuan)
            stringRibuanSatuan = strDepan + stringSatuan
            return stringRibuanSatuan
        elif(nilaiRibuan < 20):
            stringBelasan = belasan(angkaRibuan)
            stringRibuanBelasan = strDepan + stringBelasan
            return stringRibuanBelasan
        elif(nilaiRibuan < 100):
            stringPuluhan = puluhan(angkaRibuan)
            stringRibuanPuluhan = strDepan + stringPuluhan
            return stringRibuanPuluhan
        else:
            stringRatusan = ratusan(angkaRibuan)
            stringRibuanRatusan = strDepan + stringRatusan
            return stringRibuanRatusan

    else:
        angkaDepan = puluhan(nilaiPuluhanRibuan)
        strDepan = angkaDepan + 'Ribu '
        
        if(nilaiRibuan < 12):
            stringSatuan = satuan(angkaRibuan)
            stringRibuanSatuan = strDepan + stringSatuan
            return stringRibuanSatuan
        elif(nilaiRibuan < 20):
            stringBelasan = belasan(angkaRibuan)
            stringRibuanBelasan = strDepan + stringBelasan
            return stringRibuanBelasan
        elif(nilaiRibuan < 100):
            stringPuluhan = puluhan(angkaRibuan)
            stringRibuanPuluhan = strDepan + stringPuluhan
            return stringRibuanPuluhan
        else:
            stringRatusan = ratusan(angkaRibuan)
            stringRibuanRatusan = strDepan + stringRatusan
            return stringRibuanRatusan

def ratusanRibu(ribuan):
    """Fungsi untuk mencetak angka ratusan ribu"""
    
    angkaRatusanRibu = ribuan[0:3] # 3 angka pertama dalam str
    nilaiRatusan = int(ribuan[3:]) # 3 angka belakang dalam int
    angkaRatusan = str(nilaiRatusan) # 3 angka belakang dalam str

    strRatusan = ratusan(angkaRatusanRibu)
    strRatusanRibu = strRatusan + ' Ribu '

    if(nilaiRatusan < 12):
        stringSatuan = satuan(angkaRatusan)
        stringRibuanSatuan = strRatusanRibu + stringSatuan
        return stringRibuanSatuan
    elif(nilaiRatusan < 20):
        stringBelasan = belasan(angkaRatusan)
        stringRibuanBelasan = strRatusanRibu + stringBelasan
        return stringRibuanBelasan
    elif(nilaiRatusan < 100):
        stringPuluhan = puluhan(angkaRatusan)
        stringRibuanPuluhan = strRatusanRibu + stringPuluhan
        return stringRibuanPuluhan
    else:
        stringRatusan = ratusan(angkaRatusan)
        stringRibuanRatusan = strRatusanRibu + stringRatusan
        return stringRibuanRatusan