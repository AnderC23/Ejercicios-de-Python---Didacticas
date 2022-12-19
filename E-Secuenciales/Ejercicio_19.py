import os
os.system ("Cls")

sueldo_Bsico = 500
MTotalVendido = float(input("Ingrese el monto total vendido: "))

c9 = (9*MTotalVendido)/100
sueldo_Bruto = sueldo_Bsico + c9
d = (11*sueldo_Bruto)/100
sueldoN = sueldo_Bruto - d

print(f"comisión: {c9: .2f} ")
print(f"Sueldo Bruto: {sueldo_Bruto: .2f} ")
print(f"Descuento : {d: .2f}")
print(f"Sueldo Neto : {sueldoN: .2f}")