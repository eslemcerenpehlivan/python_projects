import random

def tas_kagit_makas():
    secenekler = ["taş", "kağıt", "makas"]
    oyuncu_skor = 0
    bilgisayar_skor = 0

    while True:
        print("\n--- Skor Tablosu ---")
        print(f"Sen: {oyuncu_skor} | Bilgisayar: {bilgisayar_skor}")

        oyuncu = input("Taş, kağıt veya makas seçin (çıkış için 'q'): ").lower()

        if oyuncu == 'q':
            print("Oyun bitti. Toplam skor:")
            print(f"Sen: {oyuncu_skor} | Bilgisayar: {bilgisayar_skor}")
            break

        if oyuncu not in secenekler:
            print("Geçersiz seçim, tekrar deneyin.")
            continue

        bilgisayar = random.choice(secenekler)
        print(f"Bilgisayarın seçimi: {bilgisayar}")

        if oyuncu == bilgisayar:
            print("Berabere!")
        elif (oyuncu == "taş" and bilgisayar == "makas") or \
                (oyuncu == "kağıt" and bilgisayar == "taş") or \
                (oyuncu == "makas" and bilgisayar == "kağıt"):
            print("Bu turu kazandın!")
            oyuncu_skor += 1
        else:
            print("Bu turu bilgisayar kazandı!")
            bilgisayar_skor += 1

tas_kagit_makas()