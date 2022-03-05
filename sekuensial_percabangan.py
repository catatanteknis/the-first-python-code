"""
Ini adalah project pertama menggunakan phyton
"""
print("Hello World!")
print("My name is Roni Wijaya")

total_susu = 10
total_telur = 50

print(f"Total susu = {total_susu} botol")
print(f"Total Telur = {total_telur} butir")
if total_susu > 3:
    if total_telur > 0:
        print("Beli 3 botol susu dan 5 telur")
    else:
        print("Cukup beli 3 botol susu saja")
else:
    print("Tidak usah membeli susu")
