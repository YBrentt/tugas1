import sys
import colorama
from colorama import Fore, Back, Style
from typing import Tuple, List, Optional
from dataclasses import dataclass
from decimal import Decimal, ROUND_DOWN

@dataclass
class DataBuah:
    nama: str
    harga: Decimal
    kode: str
    stok: float

@dataclass
class Transaksi:
    nama_pembeli: str
    buah: DataBuah
    jumlah: float
    total_harga: Decimal
    diskon: Decimal
    harga_akhir: Decimal

class TokoBuah:
    def __init__(self):
        self.nama_toko = "AMBATUFRUITS STORE"
        self.alamat_toko = "Jl. Jomokerto, No. 69"
        self.daftar_kasir = ["Brandon", "Steve", "Adit", "Aliya"]
        self.lebar_tampilan = 200
        self.batas_diskon = 20  # kg
        self.persentase_diskon = 20  # %
        
        # Inisialisasi persediaan buah
        self.persediaan_buah = [
            DataBuah("Apel", Decimal('30000'), "A001", 80.0),
            DataBuah("Pisang", Decimal('20000'), "A002", 80.0),
            DataBuah("Jeruk", Decimal('25000'), "A003", 80.0),
            DataBuah("Mangga", Decimal('35000'), "A004", 80.0),
            DataBuah("Anggur", Decimal('50000'), "A005", 80.0),
            DataBuah("Semangka", Decimal('15000'), "A006", 80.0),
            DataBuah("Alpukat", Decimal('30000'), "A007", 80.0),
            DataBuah("Salak", Decimal('20000'), "A008", 80.0),
            DataBuah("Jambu", Decimal('15000'), "A009", 80.0)
        ]
        
    def tampilkan_header(self) -> None:
        """Menampilkan header toko dengan format yang rapi."""
        pemisah = "=" * (self.lebar_tampilan - 2)
        header = "=" * 50
        
        print(f"+{pemisah}+")
        print(f"|{header.center(self.lebar_tampilan - 2)}|")
        print(f"|{self.nama_toko.center(self.lebar_tampilan - 2)}|")
        print(f"|{self.alamat_toko.center(self.lebar_tampilan - 2)}|")
        print(f"|{header.center(self.lebar_tampilan - 2)}|")
        
    def tampilkan_persediaan(self) -> None:
        """Menampilkan persediaan buah dalam bentuk tabel."""
        pemisah = "=" * (self.lebar_tampilan - 2)
        print(f"|{'DAFTAR BUAH PER KILOGRAM'.center(self.lebar_tampilan - 2)}|")
        print(f"|{pemisah}|")
        
        # Header tabel
        header = ("Nama Buah", "Harga Buah", "Kode Pembelian", "Stok")
        print(f"| {header[0].ljust(30)} {header[1].center(90)} {header[2].center(30)} {header[3].rjust(43)} |")
        print(f"|{pemisah}|")
        
        # Daftar buah
        for buah in self.persediaan_buah:
            print(f"| {buah.nama.ljust(30)} {'Rp {:,.0f}'.format(buah.harga).center(90)} "
                  f"{buah.kode.center(30)} {f'{buah.stok:.1f}kg'.rjust(43)} |")
        
        print(f"+{pemisah}+")
        
    def cari_buah(self, kode: str) -> Optional[DataBuah]:
        """Mencari buah berdasarkan kode."""
        return next((buah for buah in self.persediaan_buah if buah.kode == kode), None)
    
    def proses_pembayaran(self, total_bayar: Decimal) -> Tuple[bool, Decimal]:
        """Memproses pembayaran pelanggan dan menghitung kembalian."""
        while True:
            try:
                uang_pembeli = Decimal(input(f"Total yang harus dibayar: Rp {total_bayar:,.2f}\nMasukkan jumlah uang: Rp "))
                if uang_pembeli >= total_bayar:
                    return True, uang_pembeli - total_bayar
                print("Pembayaran kurang dari total belanja.")
            except ValueError:
                print("Masukkan nominal yang valid.")
    
    def cetak_struk(self, transaksi: Transaksi, pembayaran: Decimal, kembalian: Decimal) -> None:
        """Mencetak struk belanja."""
        print("\n" + "=" * 50)
        print(f"{'STRUK PEMBELIAN'.center(50)}")
        print("=" * 50)
        print(f"Nama Toko    : {self.nama_toko}")
        print(f"Alamat       : {self.alamat_toko}")
        print(f"Nama Pembeli : {transaksi.nama_pembeli}")
        print("=" * 50)
        print(f"Buah         : {transaksi.buah.nama}")
        print(f"Harga per kg : Rp {transaksi.buah.harga:,.2f}")
        print(f"Jumlah Beli  : {transaksi.jumlah:.1f} kg")
        print(f"Total Harga  : Rp {transaksi.total_harga:,.2f}")
        if transaksi.diskon > 0:
            print(f"Diskon {self.persentase_diskon}%  : Rp {transaksi.diskon:,.2f}")
            print(f"Harga Akhir  : Rp {transaksi.harga_akhir:,.2f}")
        print(f"Pembayaran   : Rp {pembayaran:,.2f}")
        print(f"Kembalian    : Rp {kembalian:,.2f}")
        print("=" * 50)
        print("Terima kasih telah berbelanja di toko kami!")
        print("=" * 50 + "\n")
    
    def proses_transaksi(self) -> Optional[Transaksi]:
        """Memproses satu transaksi pembelian."""
        nama_pembeli = input("Masukkan Nama Pembeli: ").capitalize()
        
        while True:
            kode = input("Masukkan Kode Buah: ").upper()
            buah = self.cari_buah(kode)
            
            if not buah:
                print("Kode buah tidak ditemukan. Silakan coba lagi.")
                continue
                
            print(f"Anda memilih: {buah.nama} (Rp {buah.harga:,.2f})")
            
            try:
                jumlah = float(input(f"Masukkan Jumlah Pembelian (Stok tersedia {buah.stok:.1f}kg): "))
                if jumlah <= 0:
                    print("Jumlah pembelian harus lebih dari 0.")
                    continue
                if jumlah > buah.stok:
                    print("Maaf, stok tidak mencukupi.")
                    continue
                    
                total_harga = Decimal(str(jumlah)) * buah.harga
                diskon = Decimal('0')
                harga_akhir = total_harga
                
                if jumlah >= self.batas_diskon:
                    diskon = total_harga * Decimal(str(self.persentase_diskon / 100))
                    harga_akhir = total_harga - diskon
                
                # Proses pembayaran
                sukses, kembalian = self.proses_pembayaran(harga_akhir)
                if not sukses:
                    continue
                
                # Update stok
                buah.stok -= jumlah
                
                transaksi = Transaksi(
                    nama_pembeli=nama_pembeli,
                    buah=buah,
                    jumlah=jumlah,
                    total_harga=total_harga,
                    diskon=diskon,
                    harga_akhir=harga_akhir
                )
                
                self.cetak_struk(transaksi, harga_akhir + kembalian, kembalian)
                return transaksi
                
            except ValueError:
                print("Input tidak valid. Silakan masukkan angka yang valid.")
    
    def validasi_kasir(self) -> bool:
        """Memvalidasi nama kasir."""
        while True:
            kasir = input("Masukkan nama kasir: ").capitalize()
            if kasir in self.daftar_kasir:
                print(f"Selamat datang, {kasir}!")
                return True
            print("Nama kasir tidak valid. Silakan coba lagi.")
    
    def jalankan_program(self):
        """Program utama."""
        self.tampilkan_header()
        self.tampilkan_persediaan()
        print(f"\nKasir yang bertugas: {', '.join(self.daftar_kasir[:-1])} dan {self.daftar_kasir[-1]}")
        
        if not self.validasi_kasir():
            return
        
        while True:
            lanjut_belanja = input("\nApakah anda ingin membeli buah di toko ini? [y/n]: ").lower()
            
            if lanjut_belanja == 'n':
                print("\nTerima kasih telah mengunjungi toko kami!")
                break
            elif lanjut_belanja != 'y':
                print("Input tidak valid. Silakan ketik 'y' atau 'n'.")
                continue
            
            transaksi = self.proses_transaksi()
            if not transaksi:
                continue
            
            self.tampilkan_persediaan()  # Tampilkan persediaan terbaru

def main():
    toko = TokoBuah()
    toko.jalankan_program()

if __name__ == "__main__":
    main()
