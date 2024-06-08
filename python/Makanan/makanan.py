# Data menu makanan
menu_makanan = {
    1: {"nama": "Nasi Goreng", "harga": 15000},
    2: {"nama": "Mie Goreng", "harga": 12000},
    3: {"nama": "Ayam Goreng", "harga": 20000},
    4: {"nama": "Sate Ayam", "harga": 25000},
    5: {"nama": "Capcay", "harga": 18000}
}

# Fungsi untuk menampilkan menu makanan
def tampilkan_menu():
    print("Menu Makanan:")
    for nomor, makanan in menu_makanan.items():
        print(f"{nomor}. {makanan['nama']} - Rp{makanan['harga']}")

# Fungsi untuk menghitung total harga
def hitung_total(pesanan):
    total = 0
    for nomor, jumlah in pesanan.items():
        total += menu_makanan[nomor]["harga"] * jumlah
    return total

# Fungsi untuk memproses pesanan
def pesan_makanan():
    pesanan = {}
    while True:
        tampilkan_menu()
        nomor = int(input("Masukkan nomor makanan yang ingin dipesan: "))
        if nomor not in menu_makanan:
            print("Nomor makanan tidak valid.")
            continue
        jumlah = int(input("Masukkan jumlah porsi: "))
        if jumlah <= 0:
            print("Jumlah porsi tidak valid.")
            continue
        elif nomor in pesanan:
            pesanan[nomor] += jumlah
        else:
            pesanan[nomor] = jumlah
        tanya_lagi = input("Apakah Anda ingin memesan lagi? (Y/T): ")
        if tanya_lagi.lower() != "y":
            break

    total_harga = hitung_total(pesanan)
    print("\nPesanan Anda:")
    for nomor, jumlah in pesanan.items():
        print(f"{menu_makanan[nomor]['nama']} - {jumlah} porsi")
    print(f"\nTotal harga: Rp{total_harga}")

    # Mencetak struk pembelian
    print("\n===== Struk Pembelian =====")
    for nomor, jumlah in pesanan.items():
        makanan = menu_makanan[nomor]
        print(f"{makanan['nama']} - {jumlah} porsi")
    print(f"Total harga: Rp{total_harga}")
    print("============================")

# Main program
if __name__ == "__main__":
    pesan_makanan()
