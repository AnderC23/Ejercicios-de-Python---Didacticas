import os
os.system("cls")

ft = float(input("Estatura en pies: "))
pulgadas = float(input("Estatura en pulgadas: "))

print( f"Estatura inglesa:  {ft:} ft - {pulgadas:} in")

ftametros = ft * (1.0 / 3.28084)
pmetros = pulgadas * (1.0 / 39.3701)
em = ftametros + pmetros  

print( f"La estatura en metros sería: {em: .2f} m")