#Nama: Andrew Christian Nagere
#NIM: 71200641
#Materi: Strings
#Sumber: Buku Logika Pemrograman PYTHON by Abdul Kadir (hal 282)

''' buatlah skkrip yang meminta string dimasukkan dari papan ketik 
dan kemudiann melaporkan jumlah huruf kecil dan huruf kapital masing-masing.

input: memasukan teks (input)

proses:
*memasukkan imput
*membuat variabel:
    -jlh_huruf_kapital = 0
    -jlh_huruf_kecil = 0
membuat perulangan For:
    -membuat list:
    -membuat percabangan (if)
        -jika dia huruf kapital (diprint apa...)
        -jika dia huruf kecil (diprint apa...)
print hasil berapa jumlah huruf kecil dan berapa jumlah huruf kapital.

output: kita akan mendapatkan hasil, berapa jumlah huruf kecil dan berapa jumlah huruf besar.

'''
#membuat Inputan:
teks = str(input("Masukkan Teks: "))

#membuat Variabel:
jlh_huruf_kapital = 0
jlh_huruf_kecil = 0

#membuat perulangan for:
for i in range (0,len(teks)):
    karakter = teks [i]
    if karakter.isupper():
        jlh_huruf_kapital = jlh_huruf_kapital + 1
    elif karakter.islower():
        jlh_huruf_kecil = jlh_huruf_kecil + 1
print("Jumlah Huruf Kapital adalah: ",jlh_huruf_kapital)
print("Jumlah Huruf Kecil adalah: ",jlh_huruf_kecil)






