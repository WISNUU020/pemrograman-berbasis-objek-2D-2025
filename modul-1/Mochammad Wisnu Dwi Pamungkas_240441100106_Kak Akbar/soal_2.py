class Mahasiswa:
    def __init__(self, nama, nim, jurusan, alamat):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.alamat = alamat

    def info(self):
        print(f"Nama: {self.nama}, NIM: {self.nim}, Jurusan: {self.jurusan}, Alamat: {self.alamat}")

# Input data dari pengguna
mahasiswa_list = []
for i in range(3):  # Membuat minimal 3 objek
    print(f"Masukkan data mahasiswa ke-{i+1}:")
    nama = input("Nama: ")
    nim = input("NIM: ")
    jurusan = input("Jurusan/Prodi: ")
    alamat = input("Alamat: ")
    mahasiswa_list.append(Mahasiswa(nama, nim, jurusan, alamat))
    print()

# Menampilkan informasi mahasiswa
print("Data Mahasiswa:")
for mahasiswa in mahasiswa_list:
    mahasiswa.info()
    print()
