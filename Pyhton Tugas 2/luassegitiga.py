#kelas luas segitiga

class LuasSegitiga:
    Alas = None
    Tinggi = None

#membangun instance/variable sebagai "objek nyata"
LS = LuasSegitiga()
LuasSegitiga.Alas = 8
LuasSegitiga.Tinggi = 6

Hasil = 0.5*LuasSegitiga.Alas*LuasSegitiga.Tinggi

#output yang akan ditampilkan
print("Alas Segitiga : ", LuasSegitiga.Alas)
print("Tinggi Segitiga : ", LuasSegitiga.Tinggi)
print("Hasil Luas Segitiga : ", Hasil) 