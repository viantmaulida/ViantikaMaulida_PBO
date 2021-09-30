class suku:
    def intro(self):
        print("indonesia mempunyai berbagai macam suku")

    def daerah(self):
        print("suku suku tersebut menetap diberbagai daerah")

class sunda(suku):
    def daerah(self):
        print("Orang Sunda, secara tradisional tinggal di provinsi Jawa Barat , Banten , Jakarta , dan bagian barat Jawa Tengah.")

class jawa(suku):
    def daerah(self):
        print("Orang Jawa, secara tradisional tinggal di provinsi Jawa Tengah, DIY, dan Jawa Timur.")

class lampung(suku):
    def daerah(self):
        print("Orang Lampung, secara tradisional tinggal di provinsi Lampung")

obj_suku = suku()
obj_sunda = sunda()
obj_jawa = jawa()
obj_lampung = lampung()

obj_suku.intro()
obj_suku.daerah()

print("\n")

obj_sunda.intro()
obj_sunda.daerah()

print("\n")

obj_jawa.intro()
obj_jawa.daerah()

print("\n")

obj_lampung.intro()
obj_lampung.daerah()