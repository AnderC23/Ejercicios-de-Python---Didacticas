import os
os.system ("cls")
print(f"                            RECTÁNGULO ")
Base = float(input("Base: "))
Altura = float(input("Altura: "))

area = Base * Altura
perimetro = 2 * (Base + Altura)

print(f"Área: {area: .2f} m²" )
print(f"Perímetro: {perimetro: .2f} m")