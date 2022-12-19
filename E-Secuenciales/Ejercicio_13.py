import os
os.system("cls")
import datetime

h = datetime.datetime.now()
print("HORA ACTUAL: ", h)
h_A = h + datetime.timedelta(minutes=45)
print ("Dentro de 45 minutos la hora será: " )
print (h_A)
