class OgrenciNotSistemi:
    def __init__(self):
        self.ogrenciler = {}

    def ogrenci_ekle(self, isim, notlar):
        # notlar bir liste olmalı örn: [85, 90, 70]
        ortalama = sum(notlar) / len(notlar)
        self.ogrenciler[isim] = {"notlar": notlar, "ortalama": ortalama}
        print(f"\n {isim} sisteme eklendi. Ortalaması: {ortalama:.2f}")

    def harf_notu_belirle(self, ortalama):
        if ortalama >= 90:
            return "AA"
        elif ortalama >= 80:
            return "BA"
        elif ortalama >= 70:
            return "BB"
        elif ortalama >= 60:
            return "CC"
        else:
            return "FF (Kaldı)"

    def durumu_goster(self):
        if not self.ogrenciler:
            print("\n Henüz kayıtlı öğrenci yok.")
            return

        print("\n--- ÖĞRENCİ LİSTESİ ---")
        for isim, veri in self.ogrenciler.items():
            harf = self.harf_notu_belirle(veri['ortalama'])
            print(f"Öğrenci: {isim} | Ort: {veri['ortalama']:.2f} | Harf: {harf}")


def main():
    sistem = OgrenciNotSistemi()

    while True:
        print("\n1. Öğrenci ve Not Ekle")
        print("2. Listeyi Görüntüle")
        print("3. Çıkış")

        secim = input("Seçiminiz: ")

        if secim == "1":
            isim = input("Öğrenci adı: ")
            not_girisi = input("Notları girin: ")
            notlar = [float(n) for n in not_girisi.split()]
            sistem.ogrenci_ekle(isim, notlar)

        elif secim == "2":
            sistem.durumu_goster()
        elif secim == "3":
            break


if __name__ == "__main__":
    main()