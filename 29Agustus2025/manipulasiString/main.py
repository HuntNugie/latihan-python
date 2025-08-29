# memanipulasi string dengan method

# membuat string menjadi kecil semua
nama = "Nugie Alexander Kurniawan"
print(f"normal = {nama}")
nama = nama.lower()
print(f"lower = {nama}")

# membuat string menjadi besar semua
judul = "demonslayer kimetsu no yaiba"
print(f"normal = {judul}")
judul = judul.upper()
print(f"upper = {judul}")

# mengecek dengan is Method biasanya method yang menggunakan is itu adalah method pengecekan yang hanya menghasilkan nilai boolean

# untuk mengecek apakah terdapat huruf dan angka dalam 1 string
cekAlnum = "nugie123"
print(f"apakah {cekAlnum} terdapat huruf dan angka dalam 1 string nya : {cekAlnum.isalnum()}")

# untuk mengecek semuanya adalah alphabet
cekAlpha = "nugitea"
print(f"apakah {cekAlpha} semua nya itu terdiri dari huruf alphabet saja : {cekAlpha.isalpha()}")

# untuk mengecek semuanya adalah string angka
cekDecimal = "12345"
print(f"apakah {cekDecimal} semunya itu terdiri dari string angka : {cekDecimal.isdecimal()}")

# untuk mengecek string kosong
cekSpace = "\t\t"
print(f"apakah {cekSpace} merupakan string kosong yang tidak ada teks : {cekSpace.isspace()}")

# untuk mengecek apakah semua kalimat nya di awali dengan huruf besar
cekTitle = "Kurniwati Alexandria"
print(f"apakah {cekTitle} di depan kalimat nya di awali huruf besar : {cekTitle.istitle()}")

# untuk mengecek lowercase
cekLower = "nugiekurniawan"
print(f"apakah {cekLower} karakter nya kecil semua : {cekLower.islower()}")

# untuk mengecek upppercase
cekUpper = "NADINNGRAHA"
print(f"apakah {cekUpper} karakter nya besar semua : {cekUpper.isupper()}")

# untuk mengecek awal kalimat menggunakan suatu teks
judul = "You are the apple of my eye"
print(f"apakah {judul} itu di awali dengan string 'you' : {judul.startswith("you")}")

# untuk mengecek akhir kalimat menggunkana suatu teks
print(f"apakah {judul} itu di akhiri dengan string 'eye' : {judul.endswith("eye")}")

# untuk pergabungan array atau list menjadi satu string
data = ["aku","calon","mantu","terbaik","mamah mu"]
print(" ".join(data))

# untuk pemisahan dari string menjadi array atau list
data = "akukyahcalonkyahmantukyahterbaikkyahmamahkyahmu"
print(data.split("kyah"))

# alokasi karakter untuk string menjadi di sebelah kanan
print("kanan".rjust(10,"="))

# alokasi karakter untuk string menjadi di sebelah kiri
print("kiri".ljust(10,"*"))

# alokasi karakter untuk string menjadi di tengah
print("tengah".center(10,"|"))

# menghapus karakter khusus kecuali string nya
tengah = "tengah".center(20,"=")
print(tengah.strip("="))