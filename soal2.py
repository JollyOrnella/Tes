
player_health = 100  

# Kode untuk menghitung damage
level_pemain = int(input("Masukkan level pemain: "))
damage_musuh = int(input("Masukkan damage musuh: "))

total_damage = damage_musuh - level_pemain

if total_damage < 0:
    total_damage = 0

health_after_damage = player_health - total_damage

print(f"Hasil Perhitungan:")
print("Damage yang diterima:", total_damage)
print("Kesehatan pemain setelah menerima damage:", health_after_damage)
