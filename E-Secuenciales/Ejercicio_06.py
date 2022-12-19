import os
os.system("cls")

print("Cilindro")

radio = float(input("Radio: "))
altura = float(input("Altura: "))

area = 2 * 3.1415 * radio * (radio + altura) 
volumen = 3.1415* ( radio ** 2 ) * altura

print(f"Área Total: {area: .2f} m²")
print(f"Volumen: {volumen: .2f} m³")