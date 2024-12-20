#ini adalah program SPIN
# dibuat pada 13/12/2024
# dibuat oleh M Fagian Darmawan
import os
os.system("cls")
print(30 * "\033[38;5;13m=")
print("PROGRAM SPIN".center(30))
print(30 * "\033[38;5;13m=")

import math

def tambah(x, y):
    return x + y

def kurang(x, y):
    return x - y

def kali(x, y):
    return x * y

def bagi(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Tidak bisa membagi dengan nol"

def pangkat(x, y):
    return x ** y

def akar(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return "Error: Tidak bisa menghitung akar kuadrat dari bilangan negatif"

def faktorial(x):
    if x >= 0 and x == int(x):
        return math.factorial(int(x))
    else:
        return "Error: Faktorial hanya dapat dihitung untuk bilangan bulat non-negatif"

def sin_radian(x):
    return math.sin(x)

def cos_radian(x):
    return math.cos(x)

def tan_radian(x):
    try:
        return math.tan(x)
    except:
        return "Error: Nilai tidak valid untuk tan"

def kalkulator():
    print("\n=== Kalkulator Super Canggih ===")
    print("1. Tambah")
    print("2. Kurang")
    print("3. Kali")
    print("4. Bagi")
    print("5. Pangkat")
    print("6. Akar Kuadrat")
    print("7. Faktorial")
    print("8. Sin (dalam radian)")
    print("9. Cos (dalam radian)")
    print("10. Tan (dalam radian)")

    pilihan = input("Masukkan pilihan (1-10): ")

    if pilihan in ('1', '2', '3', '4', '5'):
        try:
            angka1 = float(input("Masukkan angka pertama: "))
            angka2 = float(input("Masukkan angka kedua: "))
        except ValueError:
            print("Error: Masukkan angka yang valid")
            return

        if pilihan == '1':
            print(f"Hasil: {angka1} + {angka2} = {tambah(angka1, angka2)}")
        elif pilihan == '2':
            print(f"Hasil: {angka1} - {angka2} = {kurang(angka1, angka2)}")
        elif pilihan == '3':
            print(f"Hasil: {angka1} * {angka2} = {kali(angka1, angka2)}")
        elif pilihan == '4':
            print(f"Hasil: {angka1} / {angka2} = {bagi(angka1, angka2)}")
        elif pilihan == '5':
            print(f"Hasil: {angka1} ^ {angka2} = {pangkat(angka1, angka2)}")
    elif pilihan == '6':
        try:
            angka = float(input("Masukkan angka: "))
        except ValueError:
            print("Error: Masukkan angka yang valid")
            return
        print(f"Hasil: √{angka} = {akar(angka)}")
    elif pilihan == '7':
        try:
            angka = float(input("Masukkan angka: "))
        except ValueError:
            print("Error: Masukkan angka yang valid")
            return
        print(f"Hasil: {angka}! = {faktorial(angka)}")
    elif pilihan == '8':
        try:
            angka = float(input("Masukkan sudut dalam radian: "))
        except ValueError:
            print("Error: Masukkan angka yang valid")
            return
        print(f"Hasil: sin({angka}) = {sin_radian(angka)}")
    elif pilihan == '9':
        try:
            angka = float(input("Masukkan sudut dalam radian: "))
        except ValueError:
            print("Error: Masukkan angka yang valid")
            return
        print(f"Hasil: cos({angka}) = {cos_radian(angka)}")
    elif pilihan == '10':
        try:
            angka = float(input("Masukkan sudut dalam radian: "))
        except ValueError:
            print("Error: Masukkan angka yang valid")
            return
        print(f"Hasil: tan({angka}) = {tan_radian(angka)}")
    else:
        print("Error: Pilihan tidak valid")

if __name__ == "__main__":
    kalkulator()
