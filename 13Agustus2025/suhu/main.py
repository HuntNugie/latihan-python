# program untuk konversi suhu ke bentuk lain
print("Selamat datang di program konversi suhu") 
pilihan = int(input("1.Celcius \n2.Reamur \n3.fahrenheit \n4.kelvin \nSilahkan pilih mau konversi mulai dari mana : "))


if pilihan == 1:
    pil = int(input("1.Reamur \n2.fahrenheit \n3.kelvin \nSilahkan pilih mau konversi kemana : "))
    if pil == 1 :
        celcius = float(input("Masukkan suhu celcius : "))
        reamur = (4/5)*celcius
        print(f"Suhu dari {celcius} Celcius ke reamur adalah {reamur}")
    elif pil == 2 :
        celcius = float(input("Masukkan suhu celcius : "))
        fahrenheit = ((9/5)*celcius )+32
        print(f"Suhu dari {celcius} Celcius ke fahrenheit adalah {fahrenheit}")
    elif pil == 3 :
        celcius = float(input("Masukkan suhu celcius : "))
        kelvin = celcius+273
        print(f"Suhu dari {celcius} Celcius ke kelvin adalah {kelvin}")
elif pilihan == 2:
    pil = int(input("1.celcius \n2.fahrenheit \n3.kelvin \nSilahkan pilih mau konversi kemana : "))
    if pil == 1:
        reamur = float(input("Masukkan suhu reamur anda : "))
        celcius = (5/4) * reamur
        print(f"Suhu dari {reamur} Reamur ke celcius adalah {celcius}")
    elif pil == 2:
        reamur = float(input("Masukkan suhu reamur anda : "))
        fahrenheit = ((9/4)*reamur) + 32
        print(f"Suhu dari {reamur} Reamur ke fahrenheit adalah {fahrenheit}")
    elif pil == 3:
        reamur = float(input("Masukkan suhu reamur anda : "))
        kelvin = ((5/4)*reamur)+273
        print(f"Suhu dari {reamur} Reamur ke kelvin adalah {kelvin}")
elif pilihan == 3:
    pil = int(input("1.celcius \n2.reamur \n3.kelvin \nSilahkan pilih mau konversi kemana : "))
    if pil == 1:
        fahrenheit = float(input("Masukkan suhu fahrenheit anda : "))
        celcius = 5/9*(fahrenheit-32)
        print(f"Suhu dari {fahrenheit} Fahrenheit ke celcius adalah {celcius}")
    elif pil == 2:
        fahrenheit = float(input("Masukkan suhu fahrenheit anda : "))
        reamur = 4/9(fahrenheit-32)
        print(f"Suhu dari {fahrenheit} Fahrenheit ke reamur adalah {reamur}")
    elif pil == 3:
        fahrenheit = float(input("Masukkan suhu fahrenheit anda : "))
        celcius = 5/9*(fahrenheit-32)
        kelvin = celcius+273
        print(f"Suhu dari {fahrenheit} Fahrenheit ke kelvin adalah {kelvin}")
elif pilihan == 4:
    pil = int(input("1.celcius \n2.reamur \n3.fahrenheit \nSilahkan pilih mau konversi kemana : "))
    if pil == 1:
        kelvin = float(input("Masukkan suhu kelvin anda : "))
        celcius = kelvin-273
        print(f"Suhu dari {kelvin} Kelvin ke celcius adalah {celcius}")
    elif pil == 2:
        kelvin = float(input("Masukkan suhu kelvin anda : "))
        reamur =  4/5*(kelvin-273)       
        print(f"Suhu dari {kelvin} Kelvin ke reamur adalah {reamur}")
    elif pil == 3:
        kelvin = float(input("Masukkan suhu kelvin anda : "))
        celcius = kelvin-273
        fahrenheit = ((9/5)*celcius )+32
        print(f"suhu dari {kelvin} Kelvin ke fahrenheit adalah {fahrenheit}")