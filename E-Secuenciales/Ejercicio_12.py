import os
os.system("cls")

segundos= int(input("segundos: "))

dias = segundos // (24 * 60 * 60)
segundos = segundos % (24 * 60 * 60)
horas = segundos // (60 * 60)
segundos = segundos % (60 * 60)
minutos = segundos // 60
segundos = segundos % 60

print ("Días: {}".format(dias))
print ("Horas: {}".format(horas))
print ("Minutos: {}".format(minutos))
print ("Segundos: {}".format(segundos))