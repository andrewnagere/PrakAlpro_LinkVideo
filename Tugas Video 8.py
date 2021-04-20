#Nama: Andrew Christian Nagere
#NIM: 71200641
#Materi: LIST
#Sumber: Buku Logika Pemrograman PYTHON by Abdul Kadir hal 357

'''Buatlah sebuah program yang meminta masukan dari user dalam bentuk angka 
dan diminta unntuk menentukan bulan keberapa dengan inputan tersebut.

input:
1. membuat listnya terlebih dahulu
2. kita membuat inputannya

proses:
akan membuat percabangan (IF/Else):
    if inputan tidak berada di range 1-12 ==> tidak akan jalan (berhenti/hasil)
    if inputan masuk dalam range 1-12 ==> program akan jalan
        kita akan membuat suatu kegiatan (mencari/menentukan inputan adalah bulan keberapa)
output:
kita akan mendapatkan hasil dari inputan
'''
#membuat list:
Nama_Bulan = ["Januari","februari","Maret","April","Mei","Juni","Juli","Agustus","September","Oktober","November","Desember"]

#membuat inputan:
Kode_Bulan = int(input("Masukkan Kode bulan: "))

#membuat percabangan:
if Kode_Bulan < 1 or Kode_Bulan > 12: # if inputan tidak berada di range 1-12 ==> tidak akan jalan (berhenti/hasil)
    print("Kode Bulan harus berada di range 1-12")
else:
    a = Nama_Bulan[Kode_Bulan-1] # if inputan masuk dalam range 1-12 ==> program akan jalan
    print("Nama Bulan yang dimaksud adalah: ",a)