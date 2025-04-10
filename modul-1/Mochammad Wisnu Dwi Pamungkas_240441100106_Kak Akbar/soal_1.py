class manusia:
    def __init__(self, nama, umur, alamat):
        self.nama = nama
        self.umur = umur
        self.alamat = alamat

    def aktifitas(self, sedang):
        print(f"nama: {self.nama}, umur: {self.umur}, alamat {self.alamat}, dia sedang {sedang}")

manusia1 = manusia("wisnu",18,"sidoarjo")
manusia2 = manusia("puki",19,"lamongan")
manusia3 = manusia("tius",17,"lamongan")
manusia4 = manusia("hendrik",18,"sidoarjo")
manusia5 = manusia("syahrul",20,"jombang")  

manusia1.aktifitas("berjalan")
manusia2.aktifitas("berjalan")
manusia3.aktifitas("berlari")
manusia4.aktifitas("berlari")
manusia5.aktifitas("berjalan")