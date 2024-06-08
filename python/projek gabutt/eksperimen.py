import random

class TiketPesawat:
    def __init__(self):
        print("|==============================================|")
        print("|           TIKET PESAWAT JAKARTA              |")
        print("|==============================================|")
        print("|  Kode   |     Jenis Kelas    |    Harga      |")
        print("|----------------------------------------------|")
        print("|   E     |      Ekonomi       |  Rp. 250.000  |")
        print("|   B     |      Bisnis        |  Rp. 500.000  |")
        print("|   F     |      First         |  Rp. 900.000  |")
        print("|==============================================|")
        print('\n')

        self.nama_pemesan = input("Masukkan nama pemesan                  : ")
        self.id_pemesan = input("Masukkan ID pemesan                    : ")
        self.kode_kelas_pesawat = self.pilih_kelas()
        
        self.nomor_kursi = self.generate_nomor_kursi()
        self.gate = self.pilih_gate()
        self.tujuan = self.pilih_tujuan()
        self.jumlah_pembelian = int(input("Jumlah pembelian tiket pesawat         : "))
        self.total_harga = self.hitung_total_harga()

    def pilih_kelas(self):
        kode_kelas = input("Masukkan kode kelas pesawat (E/B/F)    : ").upper()

        if kode_kelas in ["E", "B", "F"]:
            return kode_kelas
        else:
            print("Kode kelas tidak valid. Silakan pilih lagi.")
            return self.pilih_kelas()

    def generate_nomor_kursi(self):
        # Generate nomor kursi secara otomatis
        return random.choice(["A", "B", "C"])

    def pilih_gate(self):
        list_gate = ["GATE1", "GATE2", "GATE3"]
        print("Pilih nomor gate:")
        for i, gate in enumerate(list_gate, start=1):
            print(f"{i}. {gate}")

        selected_gate = int(input("Masukkan nomor gate (1/2/3)            : "))
        return list_gate[selected_gate - 1]

    def pilih_tujuan(self):
        list_tujuan = ["Jakarta - Surabaya", "Jakarta - Bali", "Jakarta - Medan"]
        print("Pilih tujuan penerbangan:")
        for i, tujuan in enumerate(list_tujuan, start=1):
            print(f"{i}. {tujuan}")

        selected_tujuan = int(input("Masukkan nomor tujuan (1/2/3)          : "))
        return list_tujuan[selected_tujuan - 1]

    def hitung_total_harga(self):
        # Harga tiket sesuai dengan kode kelas pesawat
        if self.kode_kelas_pesawat == "E":
            harga_tiket = 250000
        elif self.kode_kelas_pesawat == "B":
            harga_tiket = 500000
        elif self.kode_kelas_pesawat == "F":
            harga_tiket = 900000
        else:
            harga_tiket = 0

        return self.jumlah_pembelian * harga_tiket

    def tampilkan_struk(self):
        print('\n')
        print("|================================================|")
        print("|   === Struk Pembelian Tiket Pesawat ===        |")
        print("|================================================|")
        print("|Nama Pemesan      : {0:<28}|".format(self.nama_pemesan))
        print("|ID Pemesan        : {0:<28}|".format(self.id_pemesan))
        print("|Kode Kelas Pesawat: {0:<28}|".format(self.kode_kelas_pesawat))
        print("|Nama Kelas Pesawat: {0:<28}|".format(self.nama_kelas_pesawat()))
        print("|Nomor Kursi       : {0:<28}|".format(self.nomor_kursi))
        print("|Gate              : {0:<28}|".format(self.gate))
        print("|Tujuan Penerbangan: {0:<28}|".format(self.tujuan))
        print("|Jumlah Pembelian  : {0:<28}|".format(self.jumlah_pembelian))
        print("|Total Harga       : Rp.{:,}                |".format(self.total_harga).replace(',', '.'))
        print("|================================================|")

    def nama_kelas_pesawat(self):
        if self.kode_kelas_pesawat == "E":
            return "Ekonomi"
        elif self.kode_kelas_pesawat == "B":
            return "Bisnis"
        elif self.kode_kelas_pesawat == "F":
            return "First"
        else:
            return "Tidak Valid"

# Main program
tiket_pesawat = TiketPesawat()
tiket_pesawat.tampilkan_struk()
