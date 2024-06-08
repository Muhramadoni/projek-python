import calendar

# Fungsi untuk mencetak kalender
def cetak_kalender(tahun):
    # Membuat objek kalender untuk tahun dan bulan yang diberikan
    kalender_tahun = calendar.TextCalendar(firstweekday=6)  # Mengatur hari pertama dalam seminggu ke Minggu
    # Mencetak kalender untuk tahun tertentu
    for bulan in range(1, 13):
        print(kalender_tahun.formatmonth(tahun, bulan))  # Menggunakan formatmonth untuk mencetak bulan

# Main program
while True:
    try:
        # Meminta input tahun dari pengguna
        tahun = int(input("Masukkan tahun (dari tahun 1990 hingga tahun sekarang): "))
        # Validasi tahun
        if tahun < 1990 or tahun > 2024:
            print("Masukkan tahun antara 1990 dan tahun sekarang.")
            continue
        # Memanggil fungsi untuk mencetak kalender
        cetak_kalender(tahun)
        break
    except ValueError:
        print("Masukkan tahun dalam bentuk angka.")
