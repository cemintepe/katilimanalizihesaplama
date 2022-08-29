# Analiz Hesaplama Programı
epfici=int(input("50 Lt Fıçının Fiyatını Giriniz ? "))
blitre=(epfici/50)
hedefl=int(input("Satılacak Litre ? "))
oranuzun=int(input("Yatırım Oranı Nedir ? "))
oran=int(oranuzun)/100
tciro=hedefl*blitre
print("Toplam Ciro: " + str(tciro))
tmaliyet=tciro*oran
print("Nokta Maliyet: " + str(tmaliyet))
nakit=int(input("İstenen TL Miktarı: "))
if nakit>tmaliyet:
    print("Toplam Cirodan Yüksek")
else:
    print("")
noran=nakit/tciro
print("Nakit Oranı: " + str(noran))
iskoran=oran-noran
isktutar=tciro*iskoran
print("İskonto Oranı: " + str(iskoran))
print("İskonto Toplam Tutarı: " + str(isktutar))
print("")
print("Cem İNTEPE")
print("Tekrar Hesaplamak İçin Bir Tuşa Basın")
print("Programı Sonlardırmak İçin 'ESC'")
