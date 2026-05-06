seferler = {}
while True:
    print ("\n--- OTOBÜS SİSTEMİ ---")
    print ("1-Seferleri Gör")
    print ("2- Sefer Ekle")
    print ("3- Sefer Sil")
    print ("4- Çıkış")
    secim = input ("seçim: ")

    if secim == "2":
        sehir = input ("Şehir")
        saat = input ("saat (örn: 14:30):")
        if sehir in seferler:
            seferler[sehir].append(saat)
        else:
            seferler[sehir] = [saat]
            print ("sefer eklendi!")
    elif secim =="3":
        sehir = input ("şehir: ")
        if sehir in seferler:
            print ("Saatler:",",".join(seferler[sehir]))
            saat = input ("silinecek saat: ")
            if saat in seferler[sehir]:
                seferler[sehir].remove(saat)
                print("silindi!")
                if not seferler [sehir]:
                    del seferler[sehir]
        else :
            print ("Saat bulunmadı")
    else:
        print (" şehir bulunamadı")

