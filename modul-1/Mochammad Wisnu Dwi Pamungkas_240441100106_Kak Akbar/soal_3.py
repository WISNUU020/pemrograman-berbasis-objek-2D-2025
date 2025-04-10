class Kucing:
    def __init__(self, nama, warna, umur):
        self.nama = nama
        self.warna = warna
        self.umur = umur
    
    def suara(self):
        print(f"{self.nama} mengeong: 'Meow! Meow!'")

class Anjing:
    def __init__(self, nama, ras, umur):
        self.nama = nama
        self.ras = ras
        self.umur = umur
    
    def suara(self):
        print(f"{self.nama} menggonggong: 'Guk! Guk!'")

class Burung:
    def __init__(self, nama, jenis, warna):
        self.nama = nama
        self.jenis = jenis
        self.warna = warna
    
    def suara(self):
        print(f"{self.nama} berkicau: 'Cuit! Cuit!'")

# List untuk menyimpan objek hewan
hewan_list = []

# Looping untuk membuat 3 objek dari tiap class
for i in range(3):
    nama_kucing = input(f"Masukkan nama kucing ke-{i+1}: ")
    warna_kucing = input("Masukkan warna kucing: ")
    umur_kucing = input("Masukkan umur kucing: ")
    hewan_list.append(Kucing(nama_kucing, warna_kucing, umur_kucing))
    
    nama_anjing = input(f"Masukkan nama anjing ke-{i+1}: ")
    ras_anjing = input("Masukkan ras anjing: ")
    umur_anjing = input("Masukkan umur anjing: ")
    hewan_list.append(Anjing(nama_anjing, ras_anjing, umur_anjing))
    
    nama_burung = input(f"Masukkan nama burung ke-{i+1}: ")
    jenis_burung = input("Masukkan jenis burung: ")
    warna_burung = input("Masukkan warna burung: ")
    hewan_list.append(Burung(nama_burung, jenis_burung, warna_burung))
    print()

# Menampilkan suara hewan
print("Suara Hewan:")
for hewan in hewan_list:
    hewan.suara()
