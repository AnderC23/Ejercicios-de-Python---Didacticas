import os
os.system("cls")


c = float(input("cantidad de productos: "))
if c <= 50:
    print("Se regalan 5 caramelos")
elif c >= 51 and c <= 100: 
    print("Se regalan 10 caramelos")
else : 
    print("Se regalan 15 caramelos")


importe = c * 20
if importe > 700: 
    descuento = importe * 0.16
    print (f"Importe sin descuento: {importe: .2f}")
    print (f"Importe con descuento: {descuento: .2f}")
elif importe >= 501 and importe < 700: 
    descuento = importe * 0.14
    print (f"Importe sin descuento: {importe: .2f}")
    print (f"Importe con descuento: {descuento: .2f}")
elif importe <= 500: 
    descuento = importe * 0.12
    print (f"Importe sin descuento: {importe: .2f}")
    print (f"Importe con descuento: {descuento: .2f}")