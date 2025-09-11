# while dan for memiliki kondisi else dimana akan di jalankan jika kondisi nya selesai secara normal bukan di break

# program password
secret_password = "nugietea123"

password = ""
kesempatan = 3
while kesempatan > 0:
    password = input("Masukan password anda : ")
    if password == secret_password:
        print("Password anda benar")
        break
    print("password salah")
    kesempatan -= 1
else:
    print("kesempatan anda sudah habis")
    
for i in range(1,6):
    print(i)
else:
    print("Sudah berhenti normal")