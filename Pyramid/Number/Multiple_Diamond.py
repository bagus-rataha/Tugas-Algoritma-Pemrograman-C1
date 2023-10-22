def diamond(tinggi, banyaknya_diamond):
    for i in range(banyaknya_diamond):
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

def sanitize_input():
    max_height = 9
    tinggi = input("Masukkan Tinggi Yang diinginkan ("+ str(max_height) + ") : ")
    if not tinggi.isdigit():
        print('Please Only Input Numbers!!!')
        return sanitize_input()
    
    
    max_diamond = 50
    banyaknya_diamond = input("Masukkan Jumlah Diamond Yang diinginkan ("+ str(max_diamond) + ") : ")
    if not banyaknya_diamond.isdigit():
        print('Please Only Input Numbers!!!')
        return sanitize_input()
    
    
    banyaknya_diamond = int(banyaknya_diamond)
    tinggi = int((int(tinggi) + 1) / 2)
    if tinggi > max_height:
        print(f'Max Height is ' + str(max_height) + ' for better view.')
        return sanitize_input()
    
    return diamond(tinggi, banyaknya_diamond)

sanitize_input()
