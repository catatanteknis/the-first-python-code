# perulangan while
j_buku = 10
baca_ulang = 0
s_baca = 0

while s_baca <= j_buku:
    if s_baca == 9 and baca_ulang < 5:
        baca_ulang += 1
        print(f"Sekarang sedang membaca buku ke-{s_baca} dan belum paham")
    else:
        print(f"Saya sudah Sudah membaca buku ke-{s_baca} dan sudah paham")
        s_baca += 1
