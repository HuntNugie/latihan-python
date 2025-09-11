# break berfungsi untuk menghentikan looping secara paksa

# program password
secret = "nugie"
password = ""
while password != secret:
    password = input("Masukan password : ")
    if password == secret:
        print(f"{password} sudah benar") 
        break
    print("password salah")
    
# continue berfungsi untuk melanjutkan ke iterasi selanjutnya dan jika ada program di bawah nya akna di lewati
# program apakah bilangan tersebut ganjil atau bukan
for i in range(1,101):
    if i % 2 == 0:
        continue
    print(f"{i} bilangan ganjil")