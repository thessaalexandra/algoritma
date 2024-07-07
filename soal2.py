def kataTerpanjang(kalimat):
    kataKata = kalimat.split()
    terpanjang = max(kataKata, key=len)
    return terpanjang, len(terpanjang)

kalimat = input("Masukkan sebuah kalimat: ")
terpanjang, panjang = kataTerpanjang(kalimat)
print(f"{terpanjang}: {panjang} karakter")
