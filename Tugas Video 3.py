#Nama: Andrew Christian Nagere
#NIM: 71200641
#Materi: Modular Programming (fungsi)
#Sumber: https://core.ac.uk/download/pdf/45375438.pdf

'''SOAL:Buatlah fungsi perkalian dua bilangan bulat!
input: memasukkan bilangan yang akan di operasikan(2 bilangan bulat)

proses:
1. deklarasi fungsi (penggunaan fungsi def)
2. deklarasi fungsi utama (input bilangan)
3. pemanggilan fungsi (hasil ouput)

output:
hasil dari program yang dibuat
'''

#deklarasi fungsi:
def perkalian(bil1,bil2):
   hitung = bil1 * bil2
   return hitung
#deklarasi fungsi utama:
bil1 = int(input("Masukkan Bilangan 1: "))
bil2 = int(input("Masukkan Bilangan 2: "))
#pemanggilan fungsi:
print("Hasil Perkalian bilangan",bil1,"dengan",bil2,"adalah",perkalian(bil1,bil2))



