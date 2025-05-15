# Buatlah skrip yang menghitung penjumlahan bilangan ganjil dari 1 sampai dengan 40.
bilangan_ganjil = [x for x in range(1, 41) if x % 2 != 0]
total = sum(bilangan_ganjil)
print("Total penjumlahan bilangan ganjil dari 1 sampai 40 adalah:", total)