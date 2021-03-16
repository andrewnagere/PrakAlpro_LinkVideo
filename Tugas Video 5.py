#Nama: Andrew Christian Nagere
#NIM: 71200641
#Materi: Struktur Kontrol Kompleks
#Sumber: Soal dibuat Sendiri!!!!

''' Buatlah sebuah program yang bisa menampilakn Jadwal Kuliah semester 1 dan semester 2. 
dimana dengan menginputkan "71200641" sebagai kata sandi akses dan akan menampilkan "Access Denied" jika salah kata sandi.
semester 1:
Senin: Matematika Teknik (07.30-09.20) & Bahasa Indonesia (11.30-13.20 ) & Praktikum Teknologi Komputer (15.30-17.20)
Selasa: Teknologi Komputer (11.30-13.20)
Rabu: Logika Matematika (07.30-09.20) & Praktikum Teknologi Komputer (09.30-11.20) & Pendidikan Agama Kristen (11.30-13.20)
Kamis : Interaksi Manusia dan Komputer (11.30-13.20)
Jumat: Kuliah Umum
Sabtu: Tidak ada Kelas
Minggu: Tidak ada Kelas
SEMESTER 2:
Senin: Algoritma & Pemrograman (11.30-13.20) & Praktikum Algoritma & Pemrograman(13.30-15.30)
Selasa: Arsitektur & Organisasi Komputer (11.30-13.20)
Rabu: Matematika Diskrit (07.30-09.20) & ICE (11.30-13.20) & Praktikum Algoritma & Pemrograman(15.30-17.30)
Kamis: Jaringan Komputer (07.30-09.20) & Praktikum Jaringan Komputer (09.30-11.20) & Pendidikan Kewarganegaraan (11.30-13.20) & Statistika (13.30-15.20)
Jumat: Kuliah Umum
Sabtu: Tidak ada kelas
Minggu: Tidak ada Kelas
untuk keluar dari program akan menampilan "TerimakKasih"

input: memasukan kata sandi

proses:
#masukan kata sandi
#masukkan programnya/isi program:
perulangan while:
1. mengakses jadwal Semester 1
2. mengakses jadwal semester 2
3. exit 
penginputan untuk perulangan


output: menampilkan hasil yang diminta
'''

print ("===========================")
print ("======Selamat Datang======")
print ("====Jadwal Mata Kuliah====")
print ("===========================")

kata_sandi =int(input("Masukkan kata sandi: "))
if kata_sandi == 71200641:
    while True:
        print("1. Menampilkan Jadwal Semester 1")
        print("2. Menampilkan Jadwal Semester 2")
        print("3. Exit")
        a = int(input("Masukkan pilihan Anda: "))
        if a == 1:
            b = str(input("Masukkan Hari: "))
            if b == "Senin":
                print ("Jadwal Kelas : Matematika Teknik (07.30-09.20) & Bahasa Indonesia (11.30-13.20 ) & Praktikum Teknologi Komputer (15.30-17.20)")
            elif b == "Selasa":
                print("Jadwall Kelas: Teknologi Komputer (11.30-13.20) ")
            elif b == "Rabu":
                print("Jadwal Kelas: Logika Matematika (07.30-09.20) & Praktikum Teknologi Komputer (09.30-11.20) & Pendidikan Agama Kristen (11.30-13.20)")
            elif b == "Kamis":
                print("Jadwal Kelas: Interaksi Manusia dan Komputer (11.30-13.20)")
            elif b == "jumat":
                print("Kuliah Umum")
            elif b == "Sabtu" or b == "Minggu":
                print("Anda Tidak Ada Kelas")
            else:
                pass
        elif a == 2:
            c = str(input("Masukkan Hari: "))
            if c == "Senin":
                print("Jadwal Kelas: Algoritma & Pemrograman (11.30-13.20) & Praktikum Algoritma & Pemrograman(13.30-15.30)")
            elif c == "Selasa":
                print("Jadwal Kelas: Arsitektur & Organisasi Komputer (11.30-13.20)")
            elif c == "Rabu":
                print("Jadwal Kelas: Matematika Diskrit (07.30-09.20) & ICE (11.30-13.20) & Praktikum Algoritma & Pemrograman(15.30-17.30)")
            elif c == "Kamis":
                print("Jadwal Kelas: Jaringan Komputer (07.30-09.20) & Praktikum Jaringan Komputer (09.30-11.20) & Pendidikan Kewarganegaraan (11.30-13.20) & Statistika (13.30-15.20)")
            elif c == "Jumat":
                print("Kuliah Umum")
            elif c == "Sabtu" or c == "Minggu":
                print("Anda Tidak Ada Kelas") 
        elif a == 3:
            print("TerimaKasih")
            break
else:
    print("Access Denied")



