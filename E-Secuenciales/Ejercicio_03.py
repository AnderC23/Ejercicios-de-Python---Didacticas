import os
os.system("cls")

t1 = float(input("Tramo 1: "))
t2 = float(input("Tramo 2: "))
t3 = float(input("Tramo 3: "))

t1m = t1 * 1000
t2m = t2 / 3.281
t3m = t3 * 1609

tm = t1m + t2m + t3m
ty = tm * 1.094

print( f"Longitud total en metros:  {tm:.2f} m")
print( f"Longitud total en yardas:  {ty:.2f}  yd")