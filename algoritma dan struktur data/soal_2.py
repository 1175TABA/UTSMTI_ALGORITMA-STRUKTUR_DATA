# Buatlah program loop untuk menghitung:
n = 5
hasil = 0
# Cetak judul
print("\nPerhitungan deret: 1/2² + 1/3² + 1/4² + ... + 1/n²")
print("-" * 50)
# Proses perhitungan dengan loop sederhana
print("Proses perhitungan:")
for i in range(2, n+1):
    # menghitung nilai suku 1
    nilai_suku = 1 / (i * i)

    print(f"1/{i}² = 1/{i*i} = {nilai_suku}")
    hasil = hasil + nilai_suku

print("-" * 50)
print(f"Hasil penjumlahan = {hasil}")
# Tampilkan bentuk deret lengkap
print("\nBentuk deret lengkap:")
deret = ""
for i in range(2, n+1):
    if i < n:
        deret = deret + f"1/{i}² + "
    else:
        deret = deret + f"1/{i}²"
print(deret, "=", hasil)