player_health = 100
player_speed = 8.6
player_name = "Glinda"
is_alive = True

while True:
    print(f"Pilih yang ingin diedit atau lihat:")
    print("1. Ubah nama karakter (player_name)")
    print("2. Ubah kecepatan pemain (player_speed)")
    print("3. Lihat data karakter")
    print("4. Keluar")

    pilihan = input("Masukkan pilihan (1-4): ")

    if pilihan == "1":
        player_name = input("Masukkan nama baru: ")
        print("Nama berhasil diubah menjadi:", player_name)

    elif pilihan == "2":
        player_speed = float(input("Masukkan kecepatan baru: "))
        print("Kecepatan berhasil diubah menjadi:", player_speed)

    elif pilihan == "3":
        # Menampilkan data karakter
        print("Nama:", player_name)
        print("Kecepatan:", player_speed)

    elif pilihan == "4":
        print("Terima kasih! Program selesai.")
        break  

    else:
        print("Pilihan tidak valid. Silakan coba lagi.")