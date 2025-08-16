# latihan komparasi 
# operator perbandingan merupakan operator yang membandingkan 2 buah nilai yang akan menghasilkan tipe data boolean true or false

# < akan membandingkan nilai di sebelah kecil lebih kecil dari yang sebelah kanan
a = 5
b = 5
hasil = a<b
print(f"{a} < {b} = {hasil}")

# > akan membandingkan nilai di sebelah kiri lebih besar dari nilai yang sebelah kanan
hasil = a>b
print(f"{a} > {b} = {hasil}")

# <= akan membandingkna nilai di sebelah kiri lebih kecil atau sama dengan yang sebelah kanan
hasil = a<=b
print(f"{a} <= {b} = {hasil}")

# >= akan membandingkan nilai di sebelah kiri lebih besar atau sama dengan nilai di sebelah kanna
hasil = a>=b
print(f"{a} >= {b} = {hasil}")

# == akan membandingkan apakah kedua nilai tersebut memiliki nilai yang sama 
hasil = a==b
print(f"{a} == {b} = {hasil}")

# != akan membandingkan apakah kedua nilai tersebut memiliki nilai yang berbeda atau tidak
hasil = a!=b
print(f"{a} != {b} = {hasil}")

# is merupakan pembanding object identity yang akan membandingkan apakah object variabel tersebut memiliki alamat memori yang sama atau tidak
hasil = a is b
print(f"{hex(id(a))} is {hex(id(b))} = {hasil}")


# is not merupakan pembanding object identity yang akan membandingkan apakah object variabel tersebut memiliki alamat memori yang berbeda 
hasil = a is not b
print(f"{hex(id(a))} is not {hex(id(b))} = {hasil}")
