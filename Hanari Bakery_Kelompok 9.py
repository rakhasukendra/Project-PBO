#anggota kelompok :
#Ahmad Dhani K (K3524003)
#Naufal Daaris F (K3524015)
#Ammar Rozan A (K3524043)
#Rakha Atmaja S (K3524065)

from abc import ABC, abstractmethod

class Produk:
    def __init__(self, nama, kode, bahan, biaya, harga):
        self.nama = nama
        self.kode = kode
        self.bahan = bahan
        self.biaya = biaya
        self.harga = harga
    
    def estimasi(self, jumlah):
        biaya_produksi = self.biaya * jumlah
        penjualan = self.harga * jumlah
        return penjualan - biaya_produksi

#interface
    
class TampilProduk(ABC):
    @abstractmethod
    def tampil(self):
        pass

class Pengadonan:
    def pengadon(self):
        print(f"{self.nama} : Pengadonan dimulai.")

class Pengembangan:
    def pengembang(self):
        print(f"{self.nama} : Melakukan pengembangan.")

class Pemanggangan:
    def pemanggang(self):
        print(f"{self.nama} : Memanggang.")

class Topping:
    def pemberi_topping(self):
        print(f"{self.nama} : Memberi topping.")

#subclassproduk
class RotiManis(Produk, TampilProduk, Pengadonan, Pengembangan, Pemanggangan):
    def __init__(self, nama, kode, bahan, biaya, harga):
        super().__init__(nama, kode, bahan, biaya, harga)
    
    def tampil(self):
        print("Jenis produk : Roti Manis")
        print(f"Nama : {self.nama}\nKode : {self.kode}\nBahan : {self.bahan}\nBiaya Produksi : {self.biaya}\nHarga Produk : {self.harga}")
    
    def pengadon(self):
        return super().pengadon()
    
    def pengembang(self):
        return super().pengembang()
    
    def pemanggang(self):
        return super().pemanggang()

class Croissant(Produk, TampilProduk, Pengadonan, Pengembangan, Pemanggangan):
    def __init__(self, nama, kode, bahan, biaya, harga):
        super().__init__(nama, kode, bahan, biaya, harga)

    def estimasi(self, jumlah):
        return super().estimasi(jumlah)
    
    def tampil(self):
        print("Jenis produk : Croissant")
        print(f"Nama : {self.nama}\nKode : {self.kode}\nBahan : {self.bahan}\nBiaya Produksi : {self.biaya}\nHarga Produk : {self.harga}")

    def pengadon(self):
        return super().pengadon()
    
    def pengembang(self):
        return super().pengembang()
    
    def pemanggang(self):
        return super().pemanggang()

class ButterCookies(Produk, TampilProduk, Pengadonan, Pemanggangan, Topping):
    def __init__(self, nama, kode, bahan, biaya, harga):
        super().__init__(nama, kode, bahan, biaya, harga)
    
    def tampil(self):
        print("Jenis produk : Butter Cookies")
        print(f"Nama : {self.nama}\nKode : {self.kode}\nBahan : {self.bahan}\nBiaya Produksi : {self.biaya}\nHarga Produk : {self.harga}")
    
    def pengadon(self):
        return super().pengadon()
    
    def pemanggang(self):
        return super().pemanggang()
    
    def pemberi_topping(self):
        return super().pemberi_topping()

class Muffin(Produk, TampilProduk, Pengadonan, Pengembangan, Pemanggangan, Topping):
    def __init__(self, nama, kode, bahan, biaya, harga):
        super().__init__(nama, kode, bahan, biaya, harga)
    
    def tampil(self):
        print("Jenis produk : Muffin")
        print(f"Nama : {self.nama}\nKode : {self.kode}\nBahan : {self.bahan}\nBiaya Produksi : {self.biaya}\nHarga Produk : {self.harga}")

    def pengadon(self):
        return super().pengadon()
    
    def pengembang(self):
        return super().pengembang()
    
    def pemanggang(self):
        return super().pemanggang()
    
    def pemberi_topping(self):
        return super().pemberi_topping()
    



#main menu
list_produk = []

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
        produk = RotiManis(nama, kode, bahan, float(biaya), float(harga))
    elif pilih_tambah == "2":
        produk = Croissant(nama, kode, bahan, float(biaya), float(harga))
    elif pilih_tambah == "3":
        produk = ButterCookies(nama, kode, bahan, float(biaya), float(harga))
    elif pilih_tambah == "4":
        produk = Muffin(nama, kode, bahan, float(biaya), float(harga))
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

main()