#Nama: Andrew Christian Nagere
#NIM: 71200641
#MATERI: Files
#Sumber: Buku Logika Pemrograman PYTHON by Abdul Kadir

''' Buatlah soal yang dimana user bisa menulis Biodata seseorang didalam sebuah data txt. Isi biodatanya sebagai berikut:
Nama:
Jenis Kelamin:
Umur:
Alamat: 
Status:
Kewarganegaraan:

input:
1. open file txt (kita menggunakan fungsi write)

proses:
1. memsukkan input biodata
2. memformat teks biodata
3. kita menggunakan fungsi write
4. fungsi close

output:
kita akan mendapatkan hasil teks biodata didalam file txt yang dimaksud
'''

#open file txt:
file_bio = open("biodata.txt","w") # menggunakan w untuk menulis di file txt

#input data:
nama = input("Nama: ")
jenis = input("Jenis Kelamin: ")
umur = input("Umur: ")
alamat = input("Alamat: ")
status = input("Status: ")
kewarganegaraan = input("Kewarganegaraan: ")

# format data dari inputan:
teks = "Nama: {}\nJenis Kelamin: {}\nUmur: {}\nAlamat: {}\nStatus: {}\nKewarganegaraan: {}\n".format(nama,jenis,umur,alamat,status,kewarganegaraan)

#menggunakan fungsi write:
file_bio.write(teks)

#menutup
file_bio.close()