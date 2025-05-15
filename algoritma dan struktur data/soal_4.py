# Dengan menggunakan loop while serta dengan menggunakan nilai input buatlah skrip
# untuk menghitung volume balok, tabung, dan limas segitiga.
# Program untuk menghitung volume bangun ruang
print("\nKalkulator Volume Bangun Ruang!")
# Loop utama menggunakan while
while True:
    # Tampilkan menu pilihan
    print("\nPilih bangun ruang yang ingin dihitung volumenya:")
    print("1. Balok")
    print("2. Tabung")
    print("3. Limas Segitiga")
    print("4. Keluar")
    # Ambil input pilihan dari pengguna
    pilihan = input("Masukkan pilihan (1-4): ")
    
    # Cek pilihan pengguna
    # Volume Balok
    if pilihan == "1":  
        print("\nMenghitung Volume Balok")
        panjang = float(input("Masukkan panjang balok: "))
        lebar = float(input("Masukkan lebar balok: "))
        tinggi = float(input("Masukkan tinggi balok: "))
        volume = panjang * lebar * tinggi
        print("Volume balok adalah:", volume)
        # Volume Tabung
    elif pilihan == "2":  
        print("\nMenghitung Volume Tabung")
        jari_jari = float(input("Masukkan jari-jari tabung: "))
        tinggi = float(input("Masukkan tinggi tabung: "))
        volume = 3.14 * jari_jari * jari_jari * tinggi 
        print("Volume tabung adalah:", volume)
        # Volume Limas Segitiga
    elif pilihan == "3": 
        print("\nMenghitung Volume Limas Segitiga")
        luas_alas = float(input("Masukkan luas alas segitiga: "))
        tinggi = float(input("Masukkan tinggi limas: "))
        volume = (1/3) * luas_alas * tinggi
        print("Volume limas segitiga adalah:", volume)
        # pilihan keluar
    elif pilihan == "4":  
        print("Terima kasih telah menggunakan program ini!")
        break  
        
    else:
        print("Pilihan tidak valid, silakan masukkan angka 1-4.")