# Kalkulator sederhana 

# membuat fungsi operator + - / x

def tambah (a,b):
    return a + b

def kurang(a,b):
    return a - b 

def bagi(a,b):
    return a / b

def kali(a,b):
    return a * b

print(f"Selamat datang diKalkulator sederhana.Silahkan masukan angka!\n")

# Input angka untuk kalkulator sederhana dengan fungsi pembulatan

angka1 = round(float(input("Masukan angka pertama :")))
print(f'\nPiliih operator \n 1. + (tambah) \n 2. - (kurang)\n 3. / (bagi) \n 4. x (kali)')
operator= input("\nMasukan operator yang anda inginkan :(+,-,/,x) ")
angka2 = round(float(input("\nMasukan angka kedua :")))


if operator == "1" :
    hasil = tambah(angka1,angka2)
    print(f"{angka1} + {angka2} = {hasil}")

elif operator == "2" :
    hasil = kurang(angka1,angka2)
    print(f"{angka1} - {angka2} = {hasil}")

elif operator == "3" :  
    hasil = bagi(angka1,angka2)
    print(f"{angka1} / {angka2} = {hasil}")

elif operator == "4" :
    hasil = kali(angka1,angka2)
    print(f"{angka1} x {angka2} = {hasil}")

else :
    print("Masukan Angka yang benar dong !")

print("\nTerima Kasih telah menggunakan layanan kami ")
