# tuple merupakan data struktur mirip dengan list hanya saja dia immutable jadi tidak bisa di ubah

ttl = ("Bandung",30,11,2004)

# cetak satu tuple
print(ttl[0])

# cetak semua tuple
for i in ttl:
    print(i)

i = 0;
while i < len(ttl):
    print(ttl[i])
    i+=1