# looping merupakan mengulang program yang sama secara berulang 

# for
for i in range(10): #default dimulai dari 0
    print("Hello world")
    
# untuk mau di atur awal mulai nya bisa tambahkan lagi parameter
for i in range(1,11): #ini artinya dimulai dari 1 - 10 karna index terakhir nya tidak di eksekusi
    print("Hello nugie")
    
# untuk bisa loncat
for i in range(1,10,2): # ini artinya di mulai dari 1 sampai 9 dan di lewat 2 
    print(i)

# decscending
for i in range(10,-1,-1): #ini artinya di mulai dari 10 sampai ke -1 dengan di lewati kurang -1 jadi akan descending
    print(i)
    
# descending di lewati lebih dari 1
for i in range(10,-1,-2): # ini akan di lewati 2 
    print(i)