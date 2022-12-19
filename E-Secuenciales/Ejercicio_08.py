import os
os.system("cls")

radio = float(input("Radio del cilindro: "))
altura = float(input("Altura del cilindro: "))

areabase = 3.141592 * (radio ** 2)
arealateral = 2 * 3.141592 * radio * altura
areatotal = 2 * areabase * arealateral

print(f"Área Base: {areabase: .2f} m²")
print(f"Área lateral : {arealateral: .2f} m²")
print(f"ÁREA TOTAL: {areatotal: .2f} m²")