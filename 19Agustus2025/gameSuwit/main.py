# latihan game suwit
import random
# selamat datang
print("Selamat datang di permainan game suwit")
ulang = True
while(ulang):
    # mengambil inputan user
    user = int(input(f"anda dapat memilih di antara bawah ini \n1.Gajah \n2.Semut \n3.Manusia \nMasukan pilihan anda (1-3) : "))
    
    # memverifikasi pilihan user
    if(user == 1):
        user = "gajah"
    elif(user == 2):
        user = "semut"
    elif(user == 3):
        user = "manusia"
    else:
        print("Anda tidak memasukkan angka dengan benar")
        break
    
    # mengambil pilihan computer
    comp = random.randint(1,3)
    # verifikasi pilihan computer
    if(comp == 1):
        comp = "gajah"
    elif(comp == 2):
        comp = "semut"
    elif(comp == 3):
        comp = "manusia"
    else:
        comp = "tidak memilih apa apa"
    
    # rules game
    if(user == comp):
        hasil = "user dan computer imbang"
    else:
        # jika tidak imbang 
        if(user == "gajah"):
            hasil = "user menang" if (comp == "manusia") else "user kalah"
        elif(user == "semut"):
            hasil = "user menang" if (comp == "gajah") else "user kalah"
        elif(user == "manusia"):
            hasil = "user menang" if (comp == "semut") else "user kalah"
    
    print(f"pilihan user : {user} \npilihan computer : {comp} \nHasil pertandingan tersebut adalah {hasil}")
    ulang = True if(input("Apakah anda mau mengulangi lagi ? (y/n) ") == "y") else False