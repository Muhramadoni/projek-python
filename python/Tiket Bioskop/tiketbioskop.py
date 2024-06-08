# Data tiket bioskop
film = {
    1: {
        "judul": "Avengers: Endgame",
        "harga_biasa": 50000,
        "harga_weekend": 60000,
        "jumlah_tiket": {"weekday": 100, "weekend": 150}
    },
    2: {
        "judul": "Joker",
        "harga_biasa": 45000,
        "harga_weekend": 55000,
        "jumlah_tiket": {"weekday": 80, "weekend": 120}
    },
    3: {
        "judul": "Spider-Man: No Way Home",
        "harga_biasa": 55000,
        "harga_weekend": 65000,
        "jumlah_tiket": {"weekday": 120, "weekend": 180}
    },
    4: {
        "judul": "The Matrix Resurrections",
        "harga_biasa": 48000,
        "harga_weekend": 58000,
        "jumlah_tiket": {"weekday": 90, "weekend": 140}
    },
    5: {
        "judul": "Dune",
        "harga_biasa": 52000,
        "harga_weekend": 62000,
        "jumlah_tiket": {"weekday": 110, "weekend": 160}
    }
}

# Fungsi untuk membuat struk pembelian
# Penggunaan program def(definisi) pada program ini untuk memungkinkan program untuk lebih terstruktur dan mudah dipelihara (seperti mengelompokkan program)
# Variabel buat_struk untuk membuat struk pembelian tiket dengan informasi judul film, hari, jumlah tiket, nomor kursi, dan total harga
def buat_struk(judul, hari, jumlah, total_harga, nomor_kursi):
    # Membuat struk pembelian dengan informasi judul film, hari, jumlah tiket, nomor kursi, dan total harga
    struk = f"\n===== Struk Pembelian =====\nJudul Film: {judul}\nHari: {hari}\nJumlah Tiket: {jumlah}\nNomor Kursi: {', '.join(nomor_kursi)}\nTotal Harga: {total_harga}\n===========================\n"
    print(struk)

# Fungsi untuk membeli tiket
def beli_tiket(film, nomor, harga, jumlah_tiket, hari, jumlah):
    try:
        if jumlah <= jumlah_tiket[hari]:  # Memeriksa apakah jumlah tiket yang diminta tersedia
            total_harga = jumlah * harga  # Menghitung total harga
            nomor_kursi = generate_nomor_kursi(jumlah)  # Generate nomor kursi
            print(f"Anda telah berhasil membeli {jumlah} tiket untuk film {film[nomor]['judul']} pada hari {hari}. Total harga: {total_harga}")
            print("Nomor Kursi:", nomor_kursi)
            jumlah_tiket[hari] -= jumlah  # Mengurangi jumlah tiket yang tersedia setelah pembelian
            buat_struk(film[nomor]['judul'], hari, jumlah, total_harga, nomor_kursi)  # Memanggil fungsi untuk membuat struk pembelian
            return total_harga
        else:
            print("Maaf, jumlah tiket yang tersedia tidak mencukupi.")
            return None
    except KeyError as e:  # Menangani jika ada kesalahan dalam mengakses elemen dictionary
        print("Error:", e)
        return None

# Fungsi untuk menambah tiket
def tambah_tiket(film, nomor, jumlah_tiket, hari, jumlah):
    try:
        jumlah_tiket[hari] += jumlah  # Menambah jumlah tiket yang tersedia
        print(f"Jumlah tiket untuk film {film[nomor]['judul']} pada hari {hari} berhasil ditambahkan sebanyak {jumlah}.")
    except KeyError as e:  # Menangani jika ada kesalahan dalam mengakses elemen dictionary
        print("Error:", e)

# Fungsi untuk menghasilkan nomor kursi
def generate_nomor_kursi(jumlah):
    kursi = []  # Daftar untuk menyimpan nomor kursi
    huruf = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # Daftar huruf untuk nomor kursi
    for i in range(jumlah):  # Loop untuk menghasilkan nomor kursi
        kursi.append(huruf[i % len(huruf)] + str((i // len(huruf)) + 1))  # Menambahkan nomor kursi ke dalam daftar
    return kursi

# Loop utama
while True:  # Memulai loop utama untuk menjalankan program secara berulang
    print("\nMenu:")  # Menampilkan menu pilihan
    print("1. Beli Tiket")  # Opsi untuk membeli tiket
    print("2. Tambah Tiket")  # Opsi untuk menambah jumlah tiket
    print("3. Keluar")  # Opsi untuk keluar dari program
    pilihan = input("Pilih menu: ")  # Meminta pengguna untuk memilih menu

    if pilihan == '1':  # Jika pengguna memilih untuk membeli tiket
        print("\nDaftar Film:")  # Menampilkan daftar film yang tersedia
        for nomor, info in film.items():
            print(f"{nomor}. {info['judul']}")
        nomor = int(input("Masukkan nomor film yang ingin dibeli tiketnya: "))  # Meminta nomor film yang ingin dibeli tiketnya
        if nomor in film:  # Memeriksa apakah nomor film valid
            print("Pilih hari:")  # Meminta pengguna untuk memilih hari
            print("1. Hari Biasa (Senin-Jumat)")
            print("2. Akhir Pekan (Sabtu-Minggu)")
            hari = input("Masukkan pilihan: ")  # Meminta pilihan hari dari pengguna
            if hari == '1':
                hari = "weekday"  # Menyesuaikan dengan key dalam dictionary
                harga = film[nomor]["harga_biasa"]  # Mengambil harga tiket untuk hari biasa
            elif hari == '2':
                hari = "weekend"  # Menyesuaikan dengan key dalam dictionary
                harga = film[nomor]["harga_weekend"]  # Mengambil harga tiket untuk akhir pekan
            else:
                print("Pilihan tidak valid.")
                continue  # Melanjutkan iterasi loop
            jumlah = int(input("Masukkan jumlah tiket yang ingin dibeli: "))  # Meminta jumlah tiket yang ingin dibeli
            jumlah_tiket = film[nomor]["jumlah_tiket"]  # Mengambil jumlah tiket yang tersedia untuk film tersebut
            total_harga = beli_tiket(film, nomor, harga, jumlah_tiket, hari, jumlah)  # Memanggil fungsi untuk membeli tiket
            if total_harga is not None and total_harga > 0:
                pass  # Struk sudah dicetak dalam fungsi beli_tiket()
        else:
            print("Film tidak ditemukan.")
    elif pilihan == '2':  # Jika pengguna memilih untuk menambah jumlah tiket
        print("\nDaftar Film:")  # Menampilkan daftar film yang tersedia
        for nomor, info in film.items():
            print(f"{nomor}. {info['judul']}")
        nomor = int(input("Masukkan nomor film yang ingin ditambahkan tiketnya: "))  # Meminta nomor film yang ingin ditambahkan tiketnya
        if nomor in film:  # Memeriksa apakah nomor film valid
            print("Pilih hari:")  # Meminta pengguna untuk memilih hari
            print("1. Hari Biasa (Senin-Jumat)")
            print("2. Akhir Pekan (Sabtu-Minggu)")
            hari = input("Masukkan pilihan: ")  # Meminta pilihan hari dari pengguna
            if hari == '1':
                hari = "weekday"  # Menyesuaikan dengan key dalam dictionary
            elif hari == '2':
                hari = "weekend"  # Menyesuaikan dengan key dalam dictionary
            else:
                print("Pilihan tidak valid.")
                continue  # Melanjutkan iterasi loop
            jumlah = int(input("Masukkan jumlah tiket yang ingin ditambahkan: "))  # Meminta jumlah tiket yang ingin ditambahkan
            jumlah_tiket = film[nomor]["jumlah_tiket"]  # Mengambil jumlah tiket yang tersedia untuk film tersebut
            tambah_tiket(film, nomor, jumlah_tiket, hari, jumlah)  # Memanggil fungsi untuk menambah jumlah tiket
        else:
            print("Film tidak ditemukan.")
    elif pilihan == '3':  # Jika pengguna memilih untuk keluar dari program
        print("Terima kasih telah menggunakan layanan kami.")  # Menampilkan pesan terima kasih
        break  # Keluar dari loop utama dan mengakhiri program
    else:
        print("Pilihan tidak valid.")  # Pesan jika pilihan tidak valid