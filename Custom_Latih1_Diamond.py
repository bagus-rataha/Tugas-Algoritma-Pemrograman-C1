def pyramid():
    tinggi = input("Masukkan Tinggi Yang diinginkan (Max 40): ")
    if not tinggi.isdigit():
        print('Please Only Input Numbers!!!')
        return pyramid()
    tinggi = int(tinggi)
    
    if tinggi >= 50:
        print('Max Height is 50 for better view.')
        return pyramid()
    
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
        
        
    for i in range(tinggi-1, 0, -1):
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

pyramid()
