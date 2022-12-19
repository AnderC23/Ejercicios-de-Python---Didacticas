import os 
os.system ("cls")

nt = float(input("Ingrese la cantidad de horas trabajadas: "))
sueldo_Basico = nt * 10
sueldo_Bruto = ((20*sueldo_Basico)/100) + sueldo_Basico
sueldo_Neto = sueldo_Bruto - ((10*sueldo_Bruto)/100) 

print(f"Sueldo Básico: {sueldo_Basico: .2f}")
print(f"Sueldo Bruto: {sueldo_Bruto: .2f}")
print(f"Sueldo Neto: {sueldo_Neto: .2f}")
