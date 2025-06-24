from menu import tambah_produk, tampilkan, simulasi_proses, kalkulator_profit

def main():
    while True:
        print("=== Hanari Bakery ===")
        print("1. Tambah Produk")
        print("2. Tampilkan Semua Produk")
        print("3. Kalkulator estimasi profit")
        print("4. Simulasi proses")
        print("0. Keluar")
        pilih = input("Pilih menu : ")

        if pilih == "1":
            tambah_produk()
        elif pilih == "2":
            tampilkan()
        elif pilih == "3":
            kalkulator_profit()
        elif pilih == "4":
            simulasi_proses()
        elif pilih == "0":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid.\n")

if __name__ == "__main__":
    main()
