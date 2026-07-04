def hesap_makinesi():
    while True:
        print("\n=== HESAP MAKİNESİ ===")
        print("1 - Toplama")
        print("2 - Çıkarma")
        print("3 - Çarpma")
        print("4 - Bölme")
        print("5 - Üs Alma")
        print("6 - Mod Alma")
        print("0 - Çıkış")

        try:
            secim = int(input("İşlem seçiniz: "))

            if secim == 0:
                print("Programdan çıkılıyor.")
                break

            if secim < 1 or secim > 6:
                print("Geçersiz işlem seçtiniz.")
                continue

            sayi1 = float(input("1. sayıyı giriniz: "))
            sayi2 = float(input("2. sayıyı giriniz: "))

            if secim == 1:
                sonuc = sayi1 + sayi2
                print("Sonuç:", sonuc)
            elif secim == 2:
                sonuc = sayi1 - sayi2
                print("Sonuç:", sonuc)
            elif secim == 3:
                sonuc = sayi1 * sayi2
                print("Sonuç:", sonuc)
            elif secim == 4:
                if sayi2 == 0:
                    print("Hata! Bir sayı 0'a bölünemez.")
                else:
                    sonuc = sayi1 / sayi2
                    print("Sonuç:", sonuc)
            elif secim == 5:
                sonuc = sayi1 ** sayi2
                print("Sonuç:", sonuc)
            elif secim == 6:
                if sayi2 == 0:
                    print("Hata! Mod 0 olamaz.")
                else:
                    sonuc = sayi1 % sayi2
                    print("Sonuç:", sonuc)
        except ValueError:
            print("Hata! Lütfen sadece sayı giriniz.")

hesap_makinesi()