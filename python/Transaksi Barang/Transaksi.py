class Barang:
    def __init__(self, kode, nama, harga, stok):
        self.kode = kode
        self.nama = nama
        self.harga = harga
        self.stok = stok

    def tambah_stok(self, jumlah):
        self.stok += jumlah
        print(f"Stok {self.nama} bertambah sebanyak {jumlah}. Stok sekarang: {self.stok}")

    def ambil_stok(self, jumlah):
        if self.stok >= jumlah:
            self.stok -= jumlah
            print(f"Berhasil mengambil {jumlah} {self.nama}. Stok sekarang: {self.stok}")
        else:
            print(f"Stok {self.nama} tidak mencukupi.")

class Penjualan:
    def __init__(self):
        self.transaksi = []

    def jual_barang(self, barang, jumlah):
        if barang.stok >= jumlah:
            total = barang.harga * jumlah
            barang.stok -= jumlah
            self.transaksi.append({"barang": barang.nama, "jumlah": jumlah, "total": total})
            print(f"Berhasil menjual {jumlah} {barang.nama}. Total penjualan: {total}")
        else:
            print(f"Stok {barang.nama} tidak mencukupi untuk dijual sebanyak {jumlah}.")

    def cetak_transaksi(self):
        print("Transaksi:")
        for idx, transaksi in enumerate(self.transaksi, start=1):
            print(f"{idx}. Barang: {transaksi['barang']}, Jumlah: {transaksi['jumlah']}, Total: {transaksi['total']}")

# Inisialisasi barang
barang1 = Barang("B001", "Buku", 5000, 50)
barang2 = Barang("P002", "Pensil", 1000, 100)
# Tambahkan barang lain sesuai kebutuhan

# Tampilkan daftar barang beserta kodenya
print("Daftar Barang:")
for barang in [barang1, barang2]:  # Tambahkan barang lain jika perlu
    print(f"Kode: {barang.kode}, Nama: {barang.nama}, Harga: {barang.harga}, Stok: {barang.stok}")

# Inisialisasi penjualan
penjualan = Penjualan()

# Fungsi untuk meminta input dari pengguna dan melakukan operasi sesuai permintaan
def main_menu():
    print("\nSelamat datang!")
    while True:
        print("\nPilih operasi:")
        print("1. Tambah Stok Barang")
        print("2. Ambil Stok Barang")
        print("3. Jual Barang")
        print("4. Cetak Transaksi")
        print("5. Keluar")

        pilihan = input("Masukkan pilihan: ")

        if pilihan == "1":
            tambah_stok_menu()
        elif pilihan == "2":
            ambil_stok_menu()
        elif pilihan == "3":
            jual_barang_menu()
        elif pilihan == "4":
            penjualan.cetak_transaksi()
        elif pilihan == "5":
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

def tambah_stok_menu():
    print("\nTambah Stok Barang:")
    print("Daftar Barang:")
    tampilkan_daftar_barang()
    kode_barang = input("Masukkan kode barang: ")
    jumlah = int(input("Masukkan jumlah yang ingin ditambahkan: "))
    # Cari barang berdasarkan kode
    barang = cari_barang(kode_barang)
    if barang:
        barang.tambah_stok(jumlah)
    else:
        print("Barang tidak ditemukan.")

def ambil_stok_menu():
    print("\nAmbil Stok Barang:")
    print("Daftar Barang:")
    tampilkan_daftar_barang()
    kode_barang = input("Masukkan kode barang: ")
    jumlah = int(input("Masukkan jumlah yang ingin diambil: "))
    # Cari barang berdasarkan kode
    barang = cari_barang(kode_barang)
    if barang:
        barang.ambil_stok(jumlah)
    else:
        print("Barang tidak ditemukan.")

def jual_barang_menu():
    print("\nJual Barang:")
    print("Daftar Barang:")
    tampilkan_daftar_barang()
    kode_barang = input("Masukkan kode barang: ")
    jumlah = int(input("Masukkan jumlah barang yang dijual: "))
    # Cari barang berdasarkan kode
    barang = cari_barang(kode_barang)
    if barang:
        penjualan.jual_barang(barang, jumlah)
    else:
        print("Barang tidak ditemukan.")

def tampilkan_daftar_barang():
    for barang in [barang1, barang2]:  # Tambahkan barang lain jika perlu
        print(f"Kode: {barang.kode}, Nama: {barang.nama}, Harga: {barang.harga}, Stok: {barang.stok}")

def cari_barang(kode):
    for barang in [barang1, barang2]:  # Tambahkan barang lain jika perlu
        if barang.kode == kode:
            return barang
    return None

# Memulai program
main_menu()
