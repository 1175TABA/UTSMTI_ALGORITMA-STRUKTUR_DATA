#  Buatlah skrip yang meminta sebuah kalimat dimasukkan dari keyboard. Selanjutnya, skrip 
# menampilkan jumlah spasi, huruf kapital, dan serta jumlah huruf kecil.
# Minta input dari pengguna
kalimat = ("Rajie Al Qadri Anwar")
# Inisialisasi 
jumlah_spasi = 0
jumlah_kapital = 0
jumlah_kecil = 0
# Memeriksa karakter
for karakter in kalimat:
    if karakter == ' ':
        jumlah_spasi += 1
    elif karakter.isupper():
        jumlah_kapital += 1
    elif karakter.islower():
        jumlah_kecil += 1
# panggil hasil dari kalimat
print("Jumlah spasi:", jumlah_spasi)
print("Jumlah huruf kapital:", jumlah_kapital)
print("Jumlah huruf kecil:", jumlah_kecil)