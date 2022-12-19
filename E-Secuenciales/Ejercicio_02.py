import os
os.system("cls")

m = int( input("Metros : "))
c = m * 100
pg = c / 2.54
pies = pg/ 12
y = pies / 3

print( f"Centímetros : {c:.2f}")
print( f"Pulgadas : {pg:.2f}")
print( f"Pies : {pies:.2f}") 