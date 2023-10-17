def is_prima (x): #11
  for i in range(2, x): # 2, 3,4,5,6,7,8,9, 10
    if x % i == 0: # 10 % 2 == 0 ? Not Prima
      return False 

  return True

def cari_bilangan_prima (awal, akhir):
  list_bilangan_prima = []

  for x in range(awal, akhir + 1):
    if is_prima(x):
      list_bilangan_prima.append(x)

  return list_bilangan_prima

def input_dynamic():
  print()
  inputan = input("Enter numbers range awal - akhir \"28, 57\" or \"21,18\": ")
  if inputan.find(',') < 0:
    print('Please Follow Input Format To Use App awal - akhir \"28, 57\"')
    input_dynamic()
 
  start, end = inputan.split(',')
  start = start.strip()
  end = end.strip()

  if not start.isdigit() or not end.isdigit():
      print('Please Only Input Numbers!!!')
      input_dynamic()
  
  print("Calculating...")
  list_prim = cari_bilangan_prima(int(start), int(end))
  string = ''
  for index, number in enumerate(list_prim):
    string += f" | [" + str(index+1) + ".] " + str(number) +" \n" if (index+1) % 5 == 0 and index+1 >= 5 else f" | [" + str(index+1) + ".] " + str(number) +" " 
  
  string = string if string != '' else "There's no Prime Numbers in This Range"
  return string


print(input_dynamic())