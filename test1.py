# Data pesanan
nama_pemesan = "Syaeful"
daftar_barang = {
    "Laptop": 8000,
    "Mouse": 30,
    "Keyboard": 50
}

# Menghitung total harga
total_harga = sum(daftar_barang.values())

# Menentukan diskon dan pajak
diskon = 0.10  # 5% diskon
pajak = 0.10   # 10% pajak

# Menghitung total setelah pajak dan diskon
total_setelah_pajak = total_harga * (1 + pajak)
total_setelah_diskon = total_setelah_pajak * (1 - diskon)

# Menampilkan pesanan
print(f"Pesanan untuk : {nama_pemesan}")
print("Daftar Barang yang dibeli :")
for barang, harga in daftar_barang.items():
    print(f"- {barang}: Rp {harga}")
print(f"Total Harga: Rp {total_harga}")
print(f"Total setelah diskon dan pajak: Rp {total_setelah_diskon:.2f}")
