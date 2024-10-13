import sys

# Header dan informasi toko
header = "=" * 50
nama_toko = "TOKO BUAH PAK AMBATUKAM"
alamat_toko = "Jl. *******, No. ***"
lebar_box = 200  # total width of the box

# Menu buah-buahan, harganya, kode pembelian, dan stok
list_item = [
    ("Daftar Buah", "Harga Buah", "Kode Pembelian", "Stok")
]

menu_buah = [
    ("Apel", "Rp 30.000", "A001", "80kg"),
    ("Pisang", "Rp 20.000", "A002", "80kg"),
    ("Jeruk", "Rp 25.000", "A003", "80kg"),
    ("Mangga", "Rp 35.000", "A004", "80kg"),
    ("Anggur", "Rp 50.000", "A005", "80kg"),
    ("Semangka", "Rp 15.000", "A006", "80kg"),
    ("Alpukat", "Rp 30.000", "A007", "80kg"),
    ("Salak", "Rp 20.000", "A008", "80kg"),
    ("Jambu", "Rp 15.000", "A009", "80kg")
]

# Fungsi untuk mengonversi stok "80kg" menjadi integer 80
def ubah_ke_int(stok_str):
    return float(''.join(filter(str.isdigit, stok_str)))

# Membuat garis atas dan bawah
garis_atas_bawah = "=" * (lebar_box - 2)

# Cetak garis atas
print(f"+{garis_atas_bawah}+")

# Cetak header toko
print(f"|{header.center(lebar_box - 2)}|")
print(f"|{nama_toko.center(lebar_box - 2)}|")
print(f"|{alamat_toko.center(lebar_box - 2)}|")
print(f"|{header.center(lebar_box - 2)}|")

# Cetak menu buah
print(f"|{'MENU BUAH PER KG'.center(lebar_box - 2)}|")
print(f"|{'=' * (lebar_box - 2)}|")
for buah, harga, kode, stok in list_item:
    print(f"| {buah.ljust(30)} {harga.center(90)} {kode.center(30)} {stok.rjust(43)} |")
    
print(f"|{'=' * (lebar_box - 2)}|")

for buah, harga, kode, stok in menu_buah:
    print(f"| {buah.ljust(30)} {harga.center(90)} {kode.center(30)} {stok.rjust(43)} |")

# Cetak garis bawah
print(f"+{garis_atas_bawah}+")

# Fungsi untuk mencari buah berdasarkan kode
def buah_code(code):
    for buah in menu_buah:
        if buah[2] == code:
            return buah
    return None

# Fungsi untuk mencetak struk pembelian
def cetak_struk(nama_pelanggan, buah, jumlah_beli, total_harga):
    print("\n" + "=" * 40)
    print(f"{'STRUK PEMBELIAN'.center(40)}")
    print("=" * 40)
    print(f"Nama Toko   : {nama_toko}")
    print(f"Alamat Toko : {alamat_toko}")
    print(f"Nama Pembeli: {nama_pelanggan}")
    print("=" * 40)
    print(f"Buah yang Dibeli: {buah[0]}")
    print(f"Harga per kg   : {buah[1]}")
    print(f"Jumlah Beli    : {jumlah_beli} kg")
    print(f"Total Harga    : Rp {total_harga:,}")
    print("=" * 40)
    print("Terima kasih telah berbelanja di toko kami!")
    print("=" * 40)
    print("\n")


# Fungsi transaksi
def ans_input():
    while True:
        input_continue = str(input("Apakah anda ingin membeli buah di toko ini [y/n]: ")).lower()
        if input_continue == 'y':
            return True
        elif input_continue == 'n':
            sys.exit("Terima kasih telah mengunjungi toko kami!")
        else:
            print("Input yang anda masukkan invalid. Hanya dapat ketik [y/n].")


def process_transaksi():
    while True:
        nama_pelanggan = str(input("Masukkan Nama Pembeli: ")).capitalize()
        code_barang = input("Masukkan Kode Buah: ").upper()
        
        # Cari buah berdasarkan kode
        fruit = buah_code(code_barang)
        
        if fruit:
            print(f"Anda memilih: {fruit[0]} ({fruit[1]})")
            stok_buah = ubah_ke_int(fruit[3])
            while True:
                try:
                    jumlah_beli_str = input(f"Masukkan Jumlah Pembelian (Stok tersedia {stok_buah}kg): ")
                    jumlah_beli = float(jumlah_beli_str)  # Mengonversi jumlah pembelian ke integer
                    
                    if jumlah_beli > stok_buah:
                        print("Maaf, stok tidak mencukupi.")
                    else:
                        total_harga = jumlah_beli * int(fruit[1].replace('Rp ', '').replace('.', ''))
                        print(f"Total Harga untuk {jumlah_beli} kg {fruit[0]}: Rp {total_harga:,}")
                        
                        # Cetak struk pembelian
                        cetak_struk(nama_pelanggan, fruit, jumlah_beli, total_harga)
                        
                        # Update stok
                        stok_baru = stok_buah - jumlah_beli
                        print(f"Stok {fruit[0]} setelah pembelian: {stok_baru}kg")
                        
                        # Perbarui menu_buah
                        index = menu_buah.index(fruit)
                        menu_buah[index] = (fruit[0], fruit[1], fruit[2], f"{stok_baru}kg")
                        
                        print("Terima kasih atas pembelian anda!")
                        break  # Keluar dari loop setelah transaksi selesai
                except ValueError:
                    print("Input tidak valid. Silakan masukkan angka untuk jumlah pembelian.")
            break
        else:
            print("Kode buah tidak ditemukan. Silakan masukkan kode yang valid.")

# Memulai transaksi
if ans_input():
    process_transaksi()

# Cetak stok terbaru
print(f"+{garis_atas_bawah}+")
print(f"|{'STOK TERBARU'.center(lebar_box - 2)}|")
print(f"|{'=' * (lebar_box - 2)}|")

for buah, harga, kode, stok in menu_buah:
    print(f"| {buah.ljust(30)} {harga.center(90)} {kode.center(30)} {stok.rjust(43)} |")

print(f"+{garis_atas_bawah}+")
