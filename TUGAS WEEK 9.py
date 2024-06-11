def case1():
    class Mahasiswa:
        def __init__(self, nama, nim, prodi, nilai): #self adalah parameter
            self.nama = nama
            self.nim = nim
            self.prodi = prodi
            self.nilai = nilai

    def input_data_mahasiswa():
        mahasiswa_list = []
        jumlah_mahasiswa = int(input("Masukkan jumlah mahasiswa yang ingin diinput: "))
        for i in range(1, jumlah_mahasiswa + 1):
            print(f"\nData Mahasiswa {i}:")
            nama = input("Masukkan nama mahasiswa: ")
            nim = input("Masukkan NIM mahasiswa: ")
            prodi = input("Masukkan program studi mahasiswa: ")
            nilai = float(input("Masukkan nilai mahasiswa: "))
            mahasiswa_list.append(Mahasiswa(nama, nim, prodi, nilai))
        return mahasiswa_list

    def tampilkan_data(mahasiswa_list):
        print("\nData Mahasiswa:")
        for mahasiswa in mahasiswa_list:
            print(f"Nama: {mahasiswa.nama}, NIM: {mahasiswa.nim}, Prodi: {mahasiswa.prodi}, Nilai: {mahasiswa.nilai}")

    def hitung_rata_rata(mahasiswa_list):
        total_nilai = sum(mahasiswa.nilai for mahasiswa in mahasiswa_list)
        rata_rata = total_nilai / len(mahasiswa_list)
        print(f"\nRata-rata nilai: {rata_rata}")

    def nilai_tertinggi_dan_terendah(mahasiswa_list):
        nilai_tertinggi = max(mahasiswa_list, key=lambda m: m.nilai)
        nilai_terendah = min(mahasiswa_list, key=lambda m: m.nilai)
        print(f"\nMahasiswa dengan nilai tertinggi: {nilai_tertinggi.nama} dengan nilai {nilai_tertinggi.nilai}")
        print(f"Mahasiswa dengan nilai terendah: {nilai_terendah.nama} dengan nilai {nilai_terendah.nilai}")

    mahasiswa_list = input_data_mahasiswa()
    tampilkan_data(mahasiswa_list)
    hitung_rata_rata(mahasiswa_list)
    nilai_tertinggi_dan_terendah(mahasiswa_list)


def case2():
    class Barang:
        def __init__(self, nama_barang, kode_barang, jumlah_barang):
            self.nama_barang = nama_barang
            self.kode_barang = kode_barang
            self.jumlah_barang = jumlah_barang

    inventory = []

    def tambah_barang():
        nama_barang = input("Masukkan nama barang: ")
        kode_barang = input("Masukkan kode barang: ")
        jumlah_barang = int(input("Masukkan jumlah barang: "))
        inventory.append(Barang(nama_barang, kode_barang, jumlah_barang))
        print("Barang berhasil ditambahkan.")

    def tampilkan_barang():
        print("\nData Barang:")
        for barang in inventory:
            print(f"Nama Barang: {barang.nama_barang}, Kode Barang: {barang.kode_barang}, Jumlah Barang: {barang.jumlah_barang}")

    def cari_barang():
        kode_barang = input("Masukkan kode barang yang ingin dicari: ")
        for barang in inventory:
            if barang.kode_barang == kode_barang:
                print(f"Nama Barang: {barang.nama_barang}, Kode Barang: {barang.kode_barang}, Jumlah Barang: {barang.jumlah_barang}")
                return
        print("Barang tidak ditemukan.")

    def hapus_barang():
        kode_barang = input("Masukkan kode barang yang ingin dihapus: ")
        for barang in inventory:
            if barang.kode_barang == kode_barang:
                inventory.remove(barang)
                print("Barang berhasil dihapus.")
                return
        print("Barang tidak ditemukan.")

    while True:
        print("\nMenu Inventaris Barang:")
        print("1. Tambah Barang")
        print("2. Tampilkan Barang")
        print("3. Cari Barang")
        print("4. Hapus Barang")
        print("5. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == '1':
            tambah_barang()
        elif pilihan == '2':
            tampilkan_barang()
        elif pilihan == '3':
            cari_barang()
        elif pilihan == '4':
            hapus_barang()
        elif pilihan == '5':
            break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")


def case3():
    class Transaksi:
        def __init__(self, tipe, jumlah):
            self.tipe = tipe
            self.jumlah = jumlah

    transaksi_list = []

    def tambah_transaksi():
        tipe = input("Masukkan tipe transaksi (uang masuk/uang keluar): ")
        jumlah = float(input("Masukkan jumlah transaksi: "))
        transaksi_list.append(Transaksi(tipe, jumlah))
        print("Transaksi berhasil ditambahkan.")

    def tampilkan_transaksi():
        print("\nData Transaksi:")
        for transaksi in transaksi_list:
            print(f"Tipe: {transaksi.tipe}, Jumlah: {transaksi.jumlah}")

    def hitung_total_pemasukan():
        total_pemasukan = sum(transaksi.jumlah for transaksi in transaksi_list if transaksi.tipe == 'pemasukan')
        print(f"Total Pemasukan: {total_pemasukan}")

    def hitung_total_pengeluaran():
        total_pengeluaran = sum(transaksi.jumlah for transaksi in transaksi_list if transaksi.tipe == 'pengeluaran')
        print(f"Total Pengeluaran: {total_pengeluaran}")

    def hitung_saldo_terakhir():
        saldo = sum(transaksi.jumlah if transaksi.tipe == 'pemasukan' else -transaksi.jumlah for transaksi in transaksi_list)
        print(f"Saldo Terakhir: {saldo}")

    while True:
        print("\nMenu Pengelolaan Keuangan Pribadi:")
        print("1. Tambah Transaksi")
        print("2. Tampilkan Transaksi")
        print("3. Hitung Total Pemasukan")
        print("4. Hitung Total Pengeluaran")
        print("5. Hitung Saldo Terakhir")
        print("6. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == '1':
            tambah_transaksi()
        elif pilihan == '2':
            tampilkan_transaksi()
        elif pilihan == '3':
            hitung_total_pemasukan()
        elif pilihan == '4':
            hitung_total_pengeluaran()
        elif pilihan == '5':
            hitung_saldo_terakhir()
        elif pilihan == '6':
            break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")


def main():
    while True:
        print("\nMenu:")
        print("1. Data Mahasiswa")
        print("2. Inventaris Barang")
        print("3. Pengelolaan Keuangan Pribadi")
        print("4. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == '1':
            case1()
        elif pilihan == '2':
            case2()
        elif pilihan == '3':
            case3()
        elif pilihan == '4':
            break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")
main()
