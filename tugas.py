class Mahasiswa:
    def __init__(self, nama):
        self.nama = nama
        self.spp_dibayar = False
        self.kuliah_diikuti = False
        self.nilai_akhir = None

    def bayar_spp(self):
        print(f"{self.nama} membayar SPP...")
        self.spp_dibayar = True

    def ikuti_kuliah(self):
        if not self.spp_dibayar:
            print("Tidak bisa mengikuti kuliah sebelum membayar SPP.")
            return
        print(f"{self.nama} mulai mengikuti perkuliahan.")
        self.kuliah_diikuti = True

    def kerjakan_tugas(self):
        if not self.kuliah_diikuti:
            print("Tidak bisa mengerjakan tugas sebelum mengikuti kuliah.")
            return
        print(f"{self.nama} mengerjakan tugas dan proyek selama semester.")

    def ikuti_ujian(self):
        if not self.kuliah_diikuti:
            print("Tidak bisa mengikuti ujian sebelum mengikuti kuliah.")
            return
        print(f"{self.nama} mengikuti ujian akhir semester.")

    def terima_nilai_akhir(self, nilai):
        if not self.kuliah_diikuti:
            print("Tidak bisa mendapatkan nilai sebelum mengikuti kuliah.")
            return
        self.nilai_akhir = nilai
        print(f"{self.nama} mendapatkan nilai akhir: {self.nilai_akhir}")

# Simulasi proses mengikuti kuliah
mahasiswa1 = Mahasiswa("Budi")
mahasiswa1.bayar_spp()
mahasiswa1.ikuti_kuliah()
mahasiswa1.kerjakan_tugas()
mahasiswa1.ikuti_ujian()
mahasiswa1.terima_nilai_akhir("A")
