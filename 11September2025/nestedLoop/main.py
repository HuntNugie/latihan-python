# nested loop istilah dimana sebuah looping bisa saja bersarang

# program perkalian
awal = int(input("Masukan angka di mulai dari 1 mau angka apa yang d kali : "))
akhir = int(input("Mau di kali sampai berapa : "))

for i in range(1,awal+1):
    for j in range(1,akhir+1):
        print(f"{i} x {j} = {i*j}")
    
    print("="*10)