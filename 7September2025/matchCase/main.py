# match case merupakan salah satu alternative lain selain if sama untuk kontrol alur program tetapi match case lebih di khususkan untuk expression di banding perbendaingan dan lebih di khususkan untuk yang menghasilkan nilai pasti

hari = input("Masukan hari : ")

match hari:
    case "senin" | "selasa" | "rabu" | "kamis" | "jumat" :
        print("itu adalah hari wajib belajar")
    case "sabtu" | "minggu" :
        print("itu hari opsional untuk belajar ")
    case _:
        print("anda tidak memasukkan nama nama hari ")