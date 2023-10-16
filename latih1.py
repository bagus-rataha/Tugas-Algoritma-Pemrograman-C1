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

# inputan = 

print("Masukkan range angka awal - akhir (28, 57)" + input())
# print(cari_bilangan_prima(1, 30))