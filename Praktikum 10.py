"""
def Salam():
    print("Selamat Datang")
    print("Anda berada di kelas Praktikum Pemrograman Dasar 1")

Salam()

def perkenalan(nama,nim,prodi,tinggi,kondisi):
    print("Nama   :", nama)
    print("NIM    :", nim)
    print("Prodi  :", prodi)
    print("Tinggi :", tinggi)
    print("Kondisi:", kondisi)

perkenalan("Haikal", 2210131210019,"Pendidikan Komputer",176,True)
"""
"""
def pembagian (bil1,bil2):
    if bil2 == 0:
        return 0
    else:
        return bil1/bil2
    
pembagian(2,2)
"""
"""
def nama(saya):
    if saya == 1:
        return "namba 1"
    elif saya == 2:
        return "namba 2"
    else:
        return "namba"

print(nama(3))
"""
"""
def untuk(mulai, sampai):
    if mulai <= sampai:
        print(mulai)
        untuk(mulai + 1, sampai)
    else:
        return None
untuk(1,10)

"""
"""
def name(nama):
    return "halo, selamat siang " + nama

a = input("Masukkan nama anda : ")
print(name(a))

def kubus(p,l,t):
    return p*l*t

a = input("Masukkan : ").replace(",","+")
kubus(int(a))
"""
def ganjil_genap(x):
    if x%2 == 0:
        return "Genap"
    else:
        return "Ganjil"

print(ganjil_genap(int(input("Masukkan angka : "))))
