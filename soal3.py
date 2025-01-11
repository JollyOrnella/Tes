# Meminta input dari pengguna
damage_diberikan = int(input("Masukkan damage yang diberikan ke musuh: "))

# Menghitung XP berdasarkan damage yang diberikan
if damage_diberikan > 50:
    xp = 100
elif 20 <= damage_diberikan <= 50:
    xp = 50
else:
    xp = 10

# Membuat program memeriksa kesehatan player

player_health = int(input("Masukkan kesehatan pemain: "))

if player_health > 50:
    print("Siap bertempur!")
else:
    print("Cari pemulihan.")


# Menampilkan hasil
print("\nXP yang diperoleh pemain:", xp)