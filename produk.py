from abc import ABC, abstractmethod
from proses import Pengadonan, Pengembangan, Pemanggangan, Topping

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

class TampilProduk(ABC):
    @abstractmethod
    def tampil(self):
        pass

class RotiManis(Produk, TampilProduk, Pengadonan, Pengembangan, Pemanggangan):
    def __init__(self, nama, kode, bahan, biaya, harga):
        super().__init__(nama, kode, bahan, biaya, harga)

    def tampil(self):
        print("Jenis produk : Roti Manis")
        print(f"Nama : {self.nama}\nKode : {self.kode}\nBahan : {self.bahan}\nBiaya Produksi : {self.biaya}\nHarga Produk : {self.harga}")

class Croissant(Produk, TampilProduk, Pengadonan, Pengembangan, Pemanggangan):
    def __init__(self, nama, kode, bahan, biaya, harga):
        super().__init__(nama, kode, bahan, biaya, harga)

    def tampil(self):
        print("Jenis produk : Croissant")
        print(f"Nama : {self.nama}\nKode : {self.kode}\nBahan : {self.bahan}\nBiaya Produksi : {self.biaya}\nHarga Produk : {self.harga}")

class ButterCookies(Produk, TampilProduk, Pengadonan, Pemanggangan, Topping):
    def __init__(self, nama, kode, bahan, biaya, harga):
        super().__init__(nama, kode, bahan, biaya, harga)

    def tampil(self):
        print("Jenis produk : Butter Cookies")
        print(f"Nama : {self.nama}\nKode : {self.kode}\nBahan : {self.bahan}\nBiaya Produksi : {self.biaya}\nHarga Produk : {self.harga}")

class Muffin(Produk, TampilProduk, Pengadonan, Pengembangan, Pemanggangan, Topping):
    def __init__(self, nama, kode, bahan, biaya, harga):
        super().__init__(nama, kode, bahan, biaya, harga)

    def tampil(self):
        print("Jenis produk : Muffin")
        print(f"Nama : {self.nama}\nKode : {self.kode}\nBahan : {self.bahan}\nBiaya Produksi : {self.biaya}\nHarga Produk : {self.harga}")
