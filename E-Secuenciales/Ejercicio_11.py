import os
os.system("cls")

nu1 = int(input ("Número de 3 cifras: "))
nu2 = int(input ("Número de 3 cifras: "))

n1_3 = nu1 % 10
n1_2 = int((nu1 % 100) / 10)
n1_1 = int((nu1 % 1000) / 100)

nu2_3 = nu2 % 10
nu2_2 = int((nu2 % 100) / 10)
nu2_1 = int((nu2 % 1000) / 100)

print(f"{n1_3}{nu2_2}{n1_1}")
print(f"{nu2_3}{n1_2}{nu2_1}")