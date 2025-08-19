# latihan komparasi dan logika

# buat program dimana akan menghasilkan true jika angka inputan tuh kurang dari atau lebih dari 10
print("Kurang dari 3 atau lebih dari 10")
user = int(input("Masukkan angka anda : "))
hasil = (user < 3 or user > 10)
print(f"angka user : {user} \nHasil dari kurang dari 3 atau lebih dari 10 adalah {hasil}")

# buat program dimana akan menghasilkan true jika angka lebih dari 3 dan kurang dari 10

hasil = (user>3 and user<10)
print(f"angka user : {user} \nHasil dari lebih dari 3 dan kurang dari 10 adalah {hasil}")