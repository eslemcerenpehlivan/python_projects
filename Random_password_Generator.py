import random

uzunluk = int(input("Sifre uzunlugunu girin: "))
kucuk = "abcdefghijklmnoprstuvwxyz"
buyuk = "ABCDEFGHIJKLMNOPRSTUVWXYZ"
ozel = "+-?$@%&/!#*"
rakam = "0123456789"

tumu = kucuk + buyuk + rakam + ozel
uzunluk_tumu = len(tumu)

sifre = ""

for i in range(uzunluk):
    rastgele_indeks = random.randint(0, uzunluk_tumu - 1)
    sifre += tumu[rastgele_indeks]

print("Oluşturulan sifre:", sifre)