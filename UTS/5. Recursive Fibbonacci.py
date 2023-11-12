def fibonacci (n):
  if n < 1:
    return [n]

  listSebelumN = fibonacci(n - 1)
  
  #Adjustment untuk cek 2 angka terakhir, jika panjang angkanya 1 maka penambahannya menjadi 0 + 1
  angka1 = listSebelumN[-2] if len(listSebelumN) > 1 else 0 # Adjust to 1
  angka2 = listSebelumN[-1] if len(listSebelumN) > 1 else 1 # Adjust to 1

  return listSebelumN + [angka1 + angka2]


def input_dynamic():
  inputan = input("Enter numbers length : ")

  if not inputan.isdigit():
      print('Please Only Input Numbers!!!')
      return input_dynamic()
  
  print("Calculating...")
  list_fibo = fibonacci(int(inputan) - 1) #adding -1 to clean call function
  string = ''
  for index, number in enumerate(list_fibo):
    string += f"| " + str(number) +" |\n" if (index+1) % 5 == 0 else f" | " + str(number) 
  
  string = string if string != '' else "There's no Fibonacci Numbers in This Range"
  print(string)
  
  
input_dynamic() #adjust moving -1