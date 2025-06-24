from produk import RotiManis, Croissant, ButterCookies, Muffin

list_produk = []

def tambah_produk():
    print("\n Pilih jenis produk")
    print("1. Roti Manis\n2. Croissant\n3. Butter Cookies\n4. Muffin")
    pilih_tambah = input("Pilih Produk : ")
    nama = input("Nama produk : ")
    kode = input("Kode produk : ")
    bahan = {}
    while True:
        bahan_baku = input("Masukkan bahan (ketikkan '0' untuk menyelesaikan) : ")
        if bahan_baku == "0": break
        jumlah = input(f"Jumlah {bahan_baku} (gram, butir, dsb) : ")
        bahan[bahan_baku] = jumlah
    biaya = float(input("Biaya produksi per pcs : "))
    harga = float(input("Harga jual per pcs : "))

    if pilih_tambah == "1":
        produk = RotiManis(nama, kode, bahan, biaya, harga)
    elif pilih_tambah == "2":
        produk = Croissant(nama, kode, bahan, biaya, harga)
    elif pilih_tambah == "3":
        produk = ButterCookies(nama, kode, bahan, biaya, harga)
    elif pilih_tambah == "4":
        produk = Muffin(nama, kode, bahan, biaya, harga)
    else:
        print("Silakan pilih menu yang ada.")
        return
    
    list_produk.append(produk)
    print("Produk ditambahkan.\n")

def tampilkan():
    if not list_produk:
        print("Tidak ada produk.")
    for n in list_produk:
        n.tampil()

def simulasi_proses():
    if not list_produk:
        print("Belum ada produk.\n")
        return
    
    print("\n=== Simulasi Proses Produksi ===")
    for i, produk in enumerate(list_produk):
        print(f"{i + 1}. {produk.nama} ({produk.kode})")
    try:
        idx = int(input("Pilih produk (nomor): ")) - 1
        produk = list_produk[idx]
    except (ValueError, IndexError):
        print("Input tidak valid.")
        return

    print(f"\nSimulasi proses produksi untuk {produk.nama}:\n")
    
    if hasattr(produk, "pengadon"): produk.pengadon()
    if hasattr(produk, "pengembang"): produk.pengembang()
    if hasattr(produk, "pemanggang"): produk.pemanggang()
    if hasattr(produk, "pemberi_topping"): produk.pemberi_topping()
    
    print("Proses produksi selesai.\n")

def kalkulator_profit():
    if not list_produk:
        print("Belum ada produk.\n")
        return

    print("\n=== Kalkulator Estimasi Profit ===")
    for i, produk in enumerate(list_produk):
        print(f"{i + 1}. {produk.nama} ({produk.kode})")
    try:
        idx = int(input("Pilih produk (nomor): ")) - 1
        produk = list_produk[idx]
    except (ValueError, IndexError):
        print("Input tidak valid.")
        return

    try:
        jumlah = int(input("Masukkan jumlah pcs yang akan diproduksi: "))
    except ValueError:
        print("Jumlah harus berupa angka.")
        return

    estimasi = produk.estimasi(jumlah)
    print(f"\nEstimasi profit dari {jumlah} pcs {produk.nama}: Rp{estimasi:,.2f}\n")
