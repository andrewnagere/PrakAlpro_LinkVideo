#Nama: Andrew Christian Nagere
#NIM: 71200641
#Materi:Tuple
#Sumber: Buku Logika Pemrograman PYTHON by Abdul Kadir hal 333-334

'''Buatlah suatu program untuk mengakses suatu data pada kamus melalui kunci yang dimasukkan pemakai (user).
perulangan berakhir kalau kata kunci yang dimasukkan berupa "Selesai".

input:
1. membuat tuple (Kamus = {"anjing":"Dog"})
2. membuat banner (print("Ketik selesai untuk mengakhiri"))

proses:
1. membuat perulangan (While):
    1. membuat inputan (kunci = inputan user)
    2. membuat inputan jadi huruf kecil (kunci.lower())
    3. membuat percabangan IF/ELSe:
        jika inputan == selesai --> program akan berhenti (break)
        jika inputan != selesai -- > program akan terus berjalan
            hasil = kamus.get(kunci,"saya tidak tahu")
            print("Bahasa Inggrisnya: ",hasil)
            print()
'''
#membuat tuple:
kamus = {'anjing':'dog','kucing':'cat','harimau':'tiger','kelelawar':'bat','sapi':'cow','kelinci':'rabbit'}

#membuat banner:
print("Ketik selesai untuk mengakhiri")

#membuat perulangan while:
while True:
    kunci = input("Nama Hewan: ")
    kunci = kunci.lower() # membuat inputan jadi huruf kecil semua
    if kunci == "selesai":
        break
    else:
        hasil = kamus.get(kunci,"Saya Tidak tahu") #memriksa apakah inputan ada didalam tuple
        print("Bahasa Inggrisnya: ",hasil)
        print()


