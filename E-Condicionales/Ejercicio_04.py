
import os
os.system("cls")



nota1 = int(input("primera nota: "))
nota2 = int(input("segunda nota: "))
nota3 = int(input("tercera nota: "))

if nota3 > 10 and nota3 <=18 and nota1 < 21 and nota2 < 21: 
   nota3_p = nota3 + 2
   print(f"Nota 3 con puntos: {nota3_p: .2f}")
   p = (nota1 + nota2 + nota3_p) / 3
   print(f"PROMEDIO: {p: .2f}")
elif nota1 > 20 or nota2 > 20 or nota3 > 20: 
   print(f"NOTA INCORRECTA ")
else: 
   p = (nota1 + nota2 + nota3) / 3
   print(f"PROMEDIO: {p: .2f}")
