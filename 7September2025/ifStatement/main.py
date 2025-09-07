# if statement merupakan kontrol alur program dimana program baru akan di jalankan dengan kondisi tertentu

user = int(input("masukan angka anda : "))

# 1 statement
# if user>17 :
#     print(f"usia anda {user} lebih dari 17")
    
    
# 2 statement
# if user > 17:
#     print(f"Usia anda {user} lebih dari 17")
# else :
#     print(f"usia anda {user} kurang dari 17")

# lebih dari 2 statement
if user % 2 == 0 :
    print("bilangan genap")
elif user % 2 == 1:
    print("Bilangan ganjil")
else :
    print("Yang anda masukan bukan lah angka")