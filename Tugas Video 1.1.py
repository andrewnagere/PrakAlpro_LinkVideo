# Nama : Andrew Christian Nagere
# NIM : 71200641
# Sumber : https://www.fisika.co.id/2020/08/rumus-percepatan.html

''' Pak Andi mengendarai sepeda sepanjang lintasan lurus 
dengan persamaan kecepatan v = (2t + 4) m/s, dengan t dalam sekon. 
Tentukanlah percepatan rata-rata sepeda dalam selang waktu t1 = 1 sekon dan t2 = 3 sekon

rumus kecepatan: v = (2t + 4)
rumus percepatan: a = (v2 - v1) / (t2 - t1)

v = kecepatan (m/s)
t = waktu (s)
a = percepatan rata-rata (m/s^2)

------
input: t1 = 1 sekon, t2 = 3 sekon

proses:
1. mencari nilai v1 dan v2 (memasuknan nilai t kedalam rumus kecepatan)
2. mencari nilai a (percepatan)

output:
nilai dari percepatan sepeda
'''
t1 = int(input("Masukkan t1: "))
t2 = int(input("Masukkan t2: "))

v1 = 2 * t1 + 4
v2 = 2 * t2 + 4

print ("nilai v1", v1, "m/s")
print ("nilai v2", v2, "m/s")

print("================")

a = (v2 - v1) / (t2 - t1)

print(" percepatan sepeda adalah:", a, "m/s^2")