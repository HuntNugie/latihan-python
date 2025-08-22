# tipe data string merupakan tipe data campuran character character yang menjadi text

# membuat string bisa menggunakan single quote atau double quote
nama = "Nugie kurniawan"
print(nama)

# jika ingin membuat quote sebagai string kita bisa menggunakannya
print("sekarang adalah hari jum'at")

# memanipulasi dengan backslash
# backslash disini dapat di gunakan untuk memanipulasi string yang kita bentuk

# tab
# berfungsi untuk menambahkan tab pada string
print("Nugie \tNadin")

# newline
# berfungsi untuk menambahkan ke baris baru seperti menggunakan enter
print("Nugie \nNadin")

# backspace
# berfungsi untuk menghapus baris sebelumnya seperti menggunakan backspace
print("Nugie \bNadin")

# backslash dua kali
# berfungsi untuk bisa menggunakan backslash nya sebagai string
print("C\\nugie\\nadin")

# raw
# berfungsi untuk menghapus konversi backslash di string
print(r"C:\user\nugie")

# multiline string
# berfungsi untuk agar saat membentuk string kita bisa membentuk dengan baris baru karna enter/tab/spasi disini akan di hitung sebagai character string
print("""
      Nama : Nugie kurniawan
      Prodi : Teknik informatika
      """)

# kombinasi antara multiline string dengan raw string
print(r"""
      file : C:\user\nugie
      website : www.ngk.com\home
      """)