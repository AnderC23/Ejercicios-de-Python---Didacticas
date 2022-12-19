import os
os.system ("cls")


a = int(input(" Grados del ángulo: "))


if a == 0: 
    print("Ángulo NULO")
if a > 0 and  a < 90: 
    print("Ángulo AGUDO")
if a == 90: 
    print("Ángulo RECTO")
if a > 90 and a < 180: 
    print("Ángulo OBTUSO")
if a >= 180 and a < 360: 
    print("Ángulo CÓNCAVO")
if a == 360: 
    print("Ángulo COMPLETO" )
elif a > 360: 
    print(" Ingrese un ángulo que se encuentre en el intrevalo de 0° A 360° ")