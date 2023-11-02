def celsius_to_fahrenheit(celsius):
    return(celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return(fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

print (f"Pilih operasi conversi suhu :\n1. Celcius to Fahrenheit\n2. Fahrenheit to Celcius\n3. Celsius to Kelvin\n4. Kelvin to Celsius\n5. Fahrenheit to Kelvin\n6. Kelvin to Fahrenheit")


pilih = input("Masukan nomer operasi (1/2/3/4/5/6) :")
if pilih in ['1', '2', '3', '4', '5', '6'] :
    suhu = float(input("Masukan angka : "))

    if pilih == '1' :
        hasil =celsius_to_fahrenheit(suhu)
        from_unit = "Celsius"
        to_unit= "Fahrenheit"

    elif pilih == '2' :
        hasil = fahrenheit_to_celsius(suhu)
        from_unit = "Fahrenheit"
        to_unit = "Celsius"

    elif pilih == '3' :
        hasil = celsius_to_kelvin(suhu)
        from_unit = "Celsius"
        to_unit = "Kelvin"

    elif pilih == '4' :
        hasil = kelvin_to_celsius(suhu)
        from_unit = "Kelvin"
        to_unit = "Celsius"

    elif pilih == '5' :
        hasil = fahrenheit_to_kelvin(suhu)
        from_unit = "Fahrenheit"
        to_unit = "Kelvin"

    elif pilih == '6' :
        hasil = kelvin_to_fahrenheit(suhu)
        from_unit = "Kelvin"
        to_unit = "Fahrenheit"
    
    print(f"{suhu} {from_unit} sama dengan {hasil:.2f} {to_unit}")

else :
    print("Pilihan operasi tidak valid")
