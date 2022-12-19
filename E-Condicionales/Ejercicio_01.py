import os
os.system("cls")

cp = float(input("Cantidad de productos: "))

if cp <= 25:
    i = cp * 27
    d = i * 0.05
    ip = i - d
    print(f"Importe: {i: .2f}")
    print (f"Importe total a pagar: {ip: 2f} ")

elif cp > 25 and cp < 50:
    i = cp * 25
    d = i * 0.05
    ip = i - d
    print(f"Importe: {i: .2f}")
    print (f"Importe total a pagar: {ip: 2f} ")
    
else :
    i = cp * 23
    d = i * 0.15
    ip = i - d
    print(f"Importe: {i: .2f}")
    print (f"Importe total a pagar: {ip: 2f} ")