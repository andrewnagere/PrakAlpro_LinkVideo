#Nama: Andrew Christian Nagere
#NIM: 71200641
#Sumber: Buku Logika Pemrograman PYTHON by ABDUL KADIR
''' tunjukkan program untuk menampilkan n bilngan ganjil dengan n dimasukkan:
A.) menggunakan perulangan for
B.) menggunakan perulangan while 
 
input: memasukkan jumlah bilangan yg dingingkan 

proses:
untuk perulangan for: membuat fungsi for i in range (apa??) 1, 2 * n, 2; print i
untuk perulangan while: membuat variabel (hitungan = 1); perulangan while (while hitungan <= n); memasukkan rumus/variabel diddalamnya; print

output:
kita akan mendapatkan hasil tampilan bilangan ganjil yang diminta

'''
n = int(input("n = "))
#perulangan for:
for i in range (1, 2 * n, 2):
    #ketika n didapatkan, maka akan lanjut ke bil selanjutnya dengan melangkah sebanyak 2x
    print(i,end= " ")
    # end= " ", fungsinya agar hasil output akan menyamping

print()#membuat baris baru

#perulangan while:
hitungan = 1
while hitungan <= n:
    print (2 * hitungan - 1, end= " ")
    hitungan = hitungan + 1




