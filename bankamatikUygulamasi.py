#Bankamatik uygulamasi
TesnimHesap = {
    'ad':'Tesnim Strazimiri',
    'HesapNo':'132456879',
    'bakiye':5000,
    'ekhesap':3000
}
    
JasminHesap = {
    'ad':'Jasmin Strazimiri',
    'HesapNo':'146756879',
    'bakiye':3000,
    'ekhesap':1000
}

def paraCek(hesap,miktar):
    print(f"Merhaba {hesap['ad']}")

    if(hesap['bakiye']>=miktar):
        hesap['bakiye']-=miktar
        print('paranizi alabilirsiniz.')
        bakiyeSorgula(hesap)
    else:
            toplam = hesap['bakiye'] + hesap['ekhesap']

            if(toplam>=miktar):
                ekhesapKullanimi=input('ek hesap kullanilsin mi (e/h)')

                if ekhesapKullanimi=='e':
                    bakiye=hesap['bakiye']

                    ekhesapKullanilacakMiktar=miktar-hesap[bakiye]
                    hesap['bakiye']=0
                    hesap['ekhesap']-=ekhesapKullanilacakMiktar
                    print('Paranizi alabilirsiniz.')
                    bakiyeSorgula(hesap)
                else:
                        print(f"{hesap['HesapNo']}nolu hesabinizda{hesap['bakiye']}bulunmaktadir.")
            else:
                    print("Uzgunuz bakiye yetersiz.")

def bakiyeSorgula(hesap):
    print(f"{hesap['HesapNo']}nolu hesabinizda {hesap['bakiye']} TL bulunmaktadir.Ek hesap limitiniz ise{hesap['ekhesap']} TL bulunmaktadir.")

paraCek(TesnimHesap,9000)    
bakiyeSorgula(TesnimHesap) 
paraCek(TesnimHesap,7000)  
bakiyeSorgula(TesnimHesap)