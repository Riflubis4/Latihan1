import kalkulator

awal = int(input("Masukkan nilai awal = "))
akhir =  int(input("Masukkan nilai akhir = "))

print(awal)
print(akhir)

def tambah(a,b):
    return a + b
def kurang(a,b):
    return a - b
def kali(a,b):
    return a * b
def bagi(a,b):
    if b != 0:
     return a / b

print("PROGRAM KALKULATOR SEDERHANA")
print("Penjumlahan")
print("Pengurangan")
print("Perkalian")
print("Pembagian")
pilihan = int(input("Masukkan pilihan ="))

if pilihan == 1:
    print(tambah(awal,akhir))
if pilihan == 2:
    print(kurang(awal,akhir))
if pilihan == 3:
    print(kali(awal, akhir))
if pilihan == 4:
    print(bagi(awal, akhir))
 
