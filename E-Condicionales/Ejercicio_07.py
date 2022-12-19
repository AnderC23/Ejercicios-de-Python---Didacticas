import os
os.system ("cls") 

n1 = float(input("Ingrese primer número: "))
n2 = float(input("Ingrese segundo número: "))
n3 = float(input("Ingrese tercer número: ")) 

if n1>n2 and n1<n3 or n1<n2 and n1>n3:
   print(f"Número intermedio  {n1: .2f}") 
elif n2>n1 and n2<n3 or n2<n1 and n2>n3:
    print(f"Número intermedio  {n2: .2f}")
elif n3>n1 and n3<n2 or n3<n1 and n3<n2:
    print(f"Número intermedio {n3: .2f}")
else:
    print("No hay numero intermedio")