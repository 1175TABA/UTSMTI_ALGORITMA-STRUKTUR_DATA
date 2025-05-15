# Terdapat list seperti berikut:
d = [2, 5, 7, 3, 2, 6, 2, 3]
# (a) Buatlah perintah untuk mendapatkan elemen terbesar dalam list tersebut.
elemen_terbesar = d[0]  
for angka in d:
    if angka > elemen_terbesar:
        elemen_terbesar = angka
print("(a) Elemen terbesar adalah:", elemen_terbesar)
# (b) Buatlah perintah untuk mendapatkan elemen yang bernilai 2
elemen_dua = []
for angka in d:
    if angka == 2:
        elemen_dua.append(angka)
print("(b) Elemen yang bernilai 2:", elemen_dua)
# (c) Buatlah perintah untuk menghitung rata-rata dalam list tersebut.
total = 0
for angka in d:
    total += angka  # Menjumlahkan semua elemen
rata_rata = total / len(d)  # Membagi total dengan jumlah elemen
print("(c) Rata-rata:", rata_rata)