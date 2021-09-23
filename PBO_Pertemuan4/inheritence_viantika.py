#Superclass
class Pendidikan():
    
    def __init__(self, nama_sekolah, alamat_sekolah ) :
        self.nama_sekolah = nama_sekolah
        self.alamat_sekolah = alamat_sekolah

#Subclass Pendidikan Sekolah Menengah Pertama dan Sekolah Menengah Atas
class Pendidikan_SekolahMenengahPertama(Pendidikan):
    pass

class Pendidikan_SekolahMenengahAtas(Pendidikan):
    pass

SDN03JembatanBesi = Pendidikan("SDN03JembatanBesi", "Jakarta")
SMPN63Jakarta = Pendidikan_SekolahMenengahPertama("SMPN63", "Jakarta")
SMAN17Jakarta = Pendidikan_SekolahMenengahAtas("SMAN17Jakarta", "Jakarta")

#Output
print(SDN03JembatanBesi.nama_sekolah, SDN03JembatanBesi.alamat_sekolah)
print(SMPN63Jakarta.nama_sekolah, SMPN63Jakarta.alamat_sekolah)
print(SMAN17Jakarta.nama_sekolah, SMAN17Jakarta.alamat_sekolah)
