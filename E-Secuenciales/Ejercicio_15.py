import os
os.system("cls")

juan = float(input("Ingrese la cantidad que aportará Juan en dólares: "))
rosa = float(input("Ingrese la cantidad que aportará Rosa en dólares: "))
daniel = float(input("Ingrese la cantidad que aportará Daniel en Soles: "))

danielDol = daniel / 3.00
t = juan + rosa + danielDol
Porcentaje_Juan = (juan * 100) / t
Porcentaje_Rosa = (rosa* 100) / t
Porcentaje_Daniel = (danielDol * 100) / t

print(f"conversión de soles a dolares de Daniel {danielDol:.2f}")
print ( f"Total de Aportes: {t:.2f} %")
print( f"Juan :  {Porcentaje_Juan:.2f} %")
print( f"Rosa :  {Porcentaje_Rosa:.2f} %")
print( f"Daniel :  {Porcentaje_Daniel:.2f} %")