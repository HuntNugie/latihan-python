# latihan operator assigment
# operator assigment berfungsi untuk memanipulasi nilai yang ada di sebelah kiri dengan nilai sebelah kanan sesuai dengan jenis operator assigment nya

# =
# berfungsi untuk memasukan nilai sebelah kanan ke variabel sebelah kiri
a = 10
print(f"nilai awal A adalah {a}")

# +=
# berfungsi untuk menjumlahkan antara nilai sebelah kiri dengan nilai sebelah kanan
a += 2
print(f"nilai A += 2 adalah {a}")

# -=
# berfungsi untuk mengkurangkan antara nilai sebelah kiri dengan nilai sebelah kanna
a-=2
print(f"nilai A -= 2 adalah {a}")

# *=
# berfungsi untuk mengkalikan antara nilai sebelah kiri dengan nilai sebelah kanan
a*=2
print(f"nilai A *= 2 adalah {a}")

# /= 
# berfungsi untuk membagi nilai sebelah kiri dengan nilai sebelah kanan
# dan pembagian pasti akan menghasilkan nilai float
a /= 2
print(f"nilai A /= 2 adalah {a}")

# **=
# exponen berfungsi untuk mempangkatkan nilai sebelah kiri dengan nilai sebelah kanan
# tipe data yang di hasilkan tergantung operand nya jika operand nya itu float maka hasilnya float jika operand nya int akan menghasilkan int
a**=2
print(f"nilai A **= 2 adalah {a}")

# //=
# floor division berfungsi untuk membagikan nilai sebelah kiri dengan nilai sebelah kanan tetapi hasilnya itu bulat ke bawah 
# tipe data yang di hasilkan floor division ini tergantung operand nya jika operand nya itu float maka hasilnya float jika operand nya itu int akan menghasilkan int
a//=2
print(f"nilai A //= 2 adalah {a}")

# %=
# modulus berfungsi untuk menghasilkan sisa bagi antara pembagian nilai sebelah kiri dengan nilai sebelah kanan
a%=2
print(f"nilai A %= 2 adalah {a}")