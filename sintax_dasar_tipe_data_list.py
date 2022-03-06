"""
Type data pada list bisa berbeda beda
"""

daftar_buku = ['marmut merah jambu', 'single', 'the lord of the ring', '4DX']
print('Tampilkan data variable daftar_buku:')
print(daftar_buku)

print('\nProses semua dengan for in:')
for buku in daftar_buku:
    print(buku)

print('\nTampilkan isi daftar_buku berdasarkan index tertentu:')
print(daftar_buku[0])
print(daftar_buku[2])

# Menambahkan data pada list menggunakan append dan berbeda type data
daftar_buku.append(-3.14)

print('\nProses semua dengan for in range dengan bantuan len():')
for i in range(0, len(daftar_buku)):
    print(f'{i+1}. {daftar_buku[i]}')

# menghapus semua data pada list
daftar_buku.clear()
print('\nIsi data dari variable daftar_buku:')
print(daftar_buku)