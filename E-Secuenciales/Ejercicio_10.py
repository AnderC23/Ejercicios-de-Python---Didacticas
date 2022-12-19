import os
os.system("cls")

n4 = int(input ("Numero natural de 4 cifras: "))

c4 = n4 % 10
c3 = int((n4 % 100) / 10)
c2 = int((n4 % 1000) / 100)
c1 = int((n4 - (n4 % 1000)) / 1000)

print(f"{c4}{c3}{c2}{c1}") 