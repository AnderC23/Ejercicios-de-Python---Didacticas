import os
os.system ("Cls")

d = float(input(" Donación en soles: "))
m_centroSalud = ((25*d)/100)
m_ComedorInfantil = ((35*d))/100
m_escuelaInfantil = ((25*d))/100 
m_asiloAncianos = ((15*d))/100

print(f"25% para Centro de Salud: {m_centroSalud: .2f} ")
print(f"35% para el Comedor Infantil: {m_centroSalud: .2f} ")
print(f"25% para la Escuela Infantil: {m_escuelaInfantil: .2f} ")
print(f" % Sobrante para Asilo de Ancianos: {m_asiloAncianos: .2f} ")