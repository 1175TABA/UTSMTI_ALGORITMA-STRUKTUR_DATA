# Buatlah skrip untuk menghitung rerata bergerak per 5 data pada 30 data masing-masing 
# baris berikut (bisa gunakan data acak):
# Baris 1: 2, 3, 5, 4, 1, 3, 5, 7, 9, 1,…,……,……..X30
# Baris 2: 1, 1, 2, 2, 4, 3, 4, 4, 5, 4…,….., ……….X30
# Hasil eksekusi:
# Baris 1: (2+3+5+4+1)/5 = 3, (3+5+7+9+1)/5 = 5,…,…,X6
# Baris 2: 2, 4,….,…., ….. ,X6
# Sajikan hasil perhitungan tersebut dalam matriks ordo 2 x 6.

# Data dari baris 1 dan baris 2
baris1 = [2, 3, 5, 4, 1, 3, 5, 7, 9, 1]  
baris2 = [1, 1, 2, 2, 4, 3, 4, 4, 5, 4]  
# data dummy berdasarkan soal 30 data dari masing masing
for i in range(20):  
    baris1.append(baris1[-1])  
    baris2.append(baris2[-1])
# List untuk menyimpan hasil rata-rata
hasil_baris1 = []
hasil_baris2 = []
# Hitung rata-rata bergerak per 5 data untuk baris 1
for i in range(0, 30, 5):  
    kelompok = baris1[i:i+5] 
    rata_rata = sum(kelompok) / 5  
    hasil_baris1.append(rata_rata)
# Hitung rata-rata bergerak per 5 data untuk baris 2
for i in range(0, 30, 5):
    kelompok = baris2[i:i+5]
    rata_rata = sum(kelompok) / 5
    hasil_baris2.append(rata_rata)
# dalam bentuk matris 2x6
print("Hasil dalam matriks 2x6:")
print("Baris 1:", hasil_baris1)
print("Baris 2:", hasil_baris2)
# Tampilkan dalam format matriks
print("\nMatriks 2x6:")
for j in range(6):
    print(hasil_baris1[j], hasil_baris2[j])