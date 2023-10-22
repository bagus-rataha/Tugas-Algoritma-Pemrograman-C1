def pyramid(tinggi, banyaknya_pyramid):
    
    for i in range(banyaknya_pyramid):
        for i in range(1, tinggi + 1):
            baris = ''

            # Section Space
            for j in range(tinggi - i):
                baris += ' '

            angka = 1
            # Section Line Numbers
            for k in range(1, i + 1): #123
                baris += str(angka) #123
                angka += 1 #234
                
            angka -= 2 #karna di awal sudah nambah 1 dan di akhir ditambah 1 lagi, supaya turun 2 angka sesuai urutan perlu dikurangin 2
            
            # Section Total Reverse Numbers Line
            for l in range(i - 1, 0, -1):
                # print(i-1)
                baris += str(l)
                angka -= 1

            # Menampilkan baris
            print(baris)


def sanitize_input():
    max_height = 9
    tinggi = input("Masukkan Tinggi Yang diinginkan ("+ str(max_height) + ") : ")
    if not tinggi.isdigit():
        print('Please Only Input Numbers!!!')
        return sanitize_input()
    
    max_pyramid = 50
    banyaknya_pyramid = input("Masukkan Jumlah Pyramid Yang diinginkan ("+ str(max_pyramid) + ") : ")
    if not banyaknya_pyramid.isdigit():
        print('Please Only Input Numbers!!!')
        return sanitize_input()
    
    banyaknya_pyramid = int(banyaknya_pyramid)
    tinggi = int(tinggi)
    return pyramid(tinggi, banyaknya_pyramid)

sanitize_input()
