#NMA: Andrew Christian Nagere
#NIM: 71200641

#sumber: https://koding.alza.web.id/latihan-soal-percabangan/

''' Berikut adalah beberapa istilah generasi berdasarkan tahun kelahirannya:

Baby boomer, kelahiran 1944 s.d 1964
Generasi X, kelahiran 1965 s.d 1979
Generasi Y (Millenials), kelahiran 1980 s.d 1994
Generasi Z, kelahiran 1995 s.d 2015
Buat program dimana user diminta untuk menuliskan nama dan tahun kelahirannya, 
kemudian cetak nama dan generasinya.

input: memasukkan nama dan tahun lahir

proses:
*input nama dan tahun
* masuk dalam percabangan/pilihan/kaegori:
1. jika tahun >= 1944 and <= 1964, print baby boomer
2. jika tahun >= 1964 and <= 1979, print generasi x
3. jika tahun >= 1980 and <= 1994, print generasi y (millenials)
4. jika tahun >= 1995 and <= 2015, print generasi z
5. selain itu tdk ada kategori

output:
user bisa mendapatkan hasil apakah dia lahir di tahun dengan julukan apa!!!

'''
nama = str(input("Masukkan nama Anda: "))
tahun = int(input("Masukkan Tahun Kelahiran: "))
if tahun >= 1944 and tahun <= 1964:
    print("User",nama,"Anda lahir ditahun Baby Boomer")
elif tahun >= 1965 and tahun <= 1979:
    print("User",nama,"Anda lahir di tahun Generasi X")
elif tahun >= 1980 and tahun <= 1994:
    print("User",nama,"Anda lahir di tahun Generasi Y (Millenials)")
elif tahun >= 1995 and tahun <= 2015:
    print("User",nama,"Anda lahir di tahun Generasi Z")
else:
    pass
