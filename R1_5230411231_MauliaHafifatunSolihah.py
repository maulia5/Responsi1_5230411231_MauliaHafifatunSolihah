class Pegawai:
    def __init__(self, nik, nama, alamat):
        self.nik = nik
        self.nama = nama
        self.alamat = alamat 

    def tampilan(self):
        return f"NIK: {self.nik}\nNama: {self.nama}\nAlamat: {self.alamat}"
    
class Produk:
    def __init__(self, kode_produk, nama_produk, jenis_produk):
        self.kode_produk = kode_produk
        self.nama_produk = nama_produk
        self.jenis_produk = jenis_produk

    def tampilan(self):
        return f"Kode: {self.kode_produk}\nNama: {self.nama_produk}\nJenis: {self.jenis_produk}"
    
    def hitung_harga(self):
        pass

class Snack(Produk):
    def __init__(self, kode_produk, nama_snack, harga):
        super().__init__(kode_produk, nama_snack, "Snack")
        self.nama_snack = nama_snack
        self.harga = harga

    def tampilan(self):
        return f"{super().tampilan()}\nHarga Snack: Rp{self.harga}"
    
    def hitung_harga(self):
        return self.harga
    
class Makanan(Produk):
    def __init__(self, kode_produk, nama_snack, harga):
        super().__init__(kode_produk, nama_snack, "Makanan")
        self.nama_snack = nama_snack
        self.harga = harga

    def tampilan(self):
        return f"{super().tampilan()}\nHarga Makanan: Rp{self.harga}"
    
    def hitung_harga(self):
        return self.harga
    
class Minuman(Produk):
    def __init__(self, kode_produk, nama_snack, harga):
        super().__init__(kode_produk, nama_snack, "Minuman")
        self.nama_snack = nama_snack
        self.harga = harga

    def tampilan(self):
        return f"{super().tampilan()}\nHarga Minuman: Rp{self.harga}"
    
    def hitung_harga(self):
        return self.harga
    
class Transaksi:
    def __init__(self, no_transaksi):
        self.no_transaksi = no_transaksi
        self.detail_transaksi = []

    def tambah_detail(self, produk, jumlah):
        self.detail_transaksi.append({
            "produk": produk,
            "jumlah": jumlah
        })

    def hitung_total(self):
        total = 0
        for item in self.detail_transaksi:
            total += item["produk"].hitung_harga() * item["jumlah"]
        return total

    def cetak_struk(self):
        print("=============================================")
        print("                STRUK PEMBELIAN              ")
        print("=============================================")
        print(f"No Transaksi: {self.no_transaksi}")
        for item in self.detail_transaksi:
            produk = item["produk"]
            jumlah = item["jumlah"]
            print(f"Produk: {produk.nama_produk}, Jumlah: {jumlah}, Harga: Rp{produk.harga * jumlah}")
        print(f"Total: Rp{self.hitung_total()}")
        print("=============================================")

if __name__ == "__main__":
    pegawai1 = Pegawai("12345678", "ifah", "Jl. Dahlia")
    
   
    snack1 = Snack("S001", "Qtela", 5000)
    makanan1 = Makanan("M001", "Mie Ayam", 25000)
    minuman1 = Minuman("N001", "Le Mineral", 5000)
    
    transaksi1 = Transaksi("T001")
    transaksi1.tambah_detail(snack1, 5)
    transaksi1.tambah_detail(makanan1, 3)
    transaksi1.tambah_detail(minuman1, 3)
    
    total = transaksi1.hitung_total()
    
    print("\nInformasi Pegawai:")
    print("========================")
    print(pegawai1.tampilan())
    print("========================")
    
    print("\nInformasi Produk:")
    print("========================")
    print(snack1.tampilan())
    print("\n" + makanan1.tampilan())
    print("\n" + minuman1.tampilan())
    print("========================")
    
    print("\nStruk Pembelian:")
    transaksi1.cetak_struk()