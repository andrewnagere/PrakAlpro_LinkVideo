# Nama: Andrew Christian Nagere
# NIM: 71200641
# Materi: Rekursif
# Sumber: Buku Logika Pemrograman PYTHON by Abdul Kadir hl 444:

'''
Buatlah fungsi yang menerima kode bulan antara 1 dan 12 dan 
memberikan nilai balik berupa nama bulan. Sekiranya argumennya
bernilai tidak antara 1 dan 12, nilai balik berupa " Kode bulan 
tidak valid". Ujilah untuk kode bulan sama dengan 1,2,12 dan 13.

input:
1. print(namaBulan(1))
2. print(namaBulan(2))
3. print(namaBulan(12))
4. print(namaBulan(13))

proses:
1. membuat fungsi Def:
    def namaBulan(kodeBulan):
2. membuat list (berisi nama-nama bulan dan argumen "Kode Bulan tidak Valid")
3. Membuat sebuah percabangan:
    jika kodeBulan >= 1 dan kodeBulan <= 12 --> memanggil nama Bulan yang dimaksud
    jika kodeBulan <= 1 dan kodeBulan >= 12 --> memanggil "Kode bulan tidak valid"
4. melakukan pemanggilan fungsi 

output:
kita akan mendapatkan hasil berupa nama bulan ataupun argumen "Kode bulan tidak valid"

'''
def namaBulan(kodeBulan):
    daftarBulan = [
        'Kode Bulan Tidak Valid',
        'Januari',
        'Februari',
        'Maret',
        'April',
        'Mei',
        'Juni',
        'Juli',
        'Agustus',
        'September',
        'Oktober',
        'November',
        'Desember'
    ]
    if kodeBulan >= 1 and kodeBulan <= 12:
        return daftarBulan[kodeBulan]
    else:
        return daftarBulan[0]
print(namaBulan(1))
print(namaBulan(2))
print(namaBulan(12))
print(namaBulan(13))
print(namaBulan(0))


