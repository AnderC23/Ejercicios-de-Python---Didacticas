import os
os.system ("Cls")

n = float(input("Numero de artículos: "))
p= float(input("Numero de unidad del artículo: "))
i = n * p
d1 = (15* i)/100
d2 = ((15*i)/100) + d1 
ip =  i - d2 

print(f"Importe de la compra: {i: .2f}")
print(f"Descuento: {d2: .2f}")
print(f"Importe a pagar: {ip: .2f}")