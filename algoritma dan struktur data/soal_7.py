# Buatlah fungsi yang dapat digunakan untuk menjumlahkan semua nilai argumennya 
# dengan jumlah argument bisa bervariasi. Contoh:
def Jumlahkan(*args):
    total = 0
    for angka in args:
        total += angka
    return total

# Jumlahkan(1,2) menghasilkan 3
print(Jumlahkan(1, 2))
# Jumlahkan(1,2,3) menghasilkan 6
print(Jumlahkan(1, 2, 3))
# Jumlahkan(1,2,3,4) menghasilkan 10
print(Jumlahkan(1, 2, 3, 4))
