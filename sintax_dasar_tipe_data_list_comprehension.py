"""
Type data pada list bisa berbeda beda
- List Comprehension
"""

daftar_buku = [1001, 'single', 'the lord of the ring', -3.14, '4DX', 'second change', 99]
print('Tampilkan data variable daftar_buku:')
print(daftar_buku)

# Menghapus element menggunakan del
del daftar_buku[2]
print('\nIsi data dari variable daftar_buku:')
print(daftar_buku)

# Menghapus element index 0 dg batas index 2 menggunakan comprehension
del daftar_buku[0:2] #START:END
print('\nIsi data dari variable daftar_buku:')
print(daftar_buku)

# Menghapus element namun dg increment 2
del daftar_buku[0::2] #START:END:STEP

print('\nProses semua dengan for in range dengan bantuan len():')
for i in range(0, len(daftar_buku)):
    print(f'{i+1}. {daftar_buku[i]}')

# Menghapus semua element pada list menggunakan comprehension
del daftar_buku[:] #START:END
print('\nIsi data dari variable daftar_buku:')
print(daftar_buku)