# list merupakan data struktur yang dapat menampung banyak nilai sekaligus dan tipe data dari nilai nya boleh campur list mempunyai index yang di mulai dari 0 serta dapat di ubah mutable

# cara membuat
# number
angka = [1,2,3,4,5]
# string
nama = ["Nugie","Nadin","Fairel"]
# boolean
boolean = [True,False]
# campuran
campuran = [1,2,3,"Nugie","nadin",True,False]

# cara mencetak satu nilai
print(angka[0])

# cara mengganti nilai
nama[0] = "Jaenudin"
print(nama)

# cara menambahkan nilai
nama.append("Nugie") # ini akan menambahkan nilai di paling belakang
print(nama)
nama.insert(1,"Kurniawan") # ini akan menambahkan nilai di index yang di tentukan
print(nama)

# cara menghapus nilai
nama.remove("Fairel") # ini akan menghapus berdasarkan isi dari nilainya
print(nama)
nama.pop() # ini secara default jika tidak di set akan menghapus nilai paling akhir
print(nama)
nama.pop(1) # ini jika di isi parameter nya degan nomor index maka akan di hapus sesuai index
print(nama)

# mengecek apakah suatu nilai ada di dalam list
print("Nadin" in nama) # ini akan menghasilkan nilai boolean True jika ada False jika tidak ada

# mencetak semua isi list dengan loop
# for
for i in campuran:
    print(i)
    
# while
i = 0
while i < len(campuran):
    print(campuran[i])
    i+=1