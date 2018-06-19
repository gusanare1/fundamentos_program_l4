Toyota = "Frias 4G, Fortuner, Hilax, Innova, Yaris, RAV4"
Hyunday = "Aceint, Creta, Grand i10, Santa Fe, Tucson"
Nissan = "Versa, Pathfinder, Qasahqal, Kicks, X-trail"
Mazda = "CX-5, CX-9, BT-50, Sedan, Hatchback"

import numpy as np
import random
marcas_autos = []
marcas_autos = Toyota.split(", ") + Hyunday.split(", ") + Nissan.split(", ") + Mazda.split(", ")
autos_dias = np.zeros( (8,len(marcas_autos)), dtype=int) #Creas matriz
#print(Toyota+Hyunday+Nissan+Mazda)
for i in range(0,len(marcas_autos)): #Recorro la matriz
	for j in range(0, 7):
		autos_dias[j][i] = random.randrange(1,20)
	autos_dias[7][i] = random.randrange(1,10)
print(autos_dias)
print("---------------------------------")
preg_toyota = autos_dias[:,0:6]
prom_toyota = np.sum(preg_toyota)/np.sum(autos_dias)*100
print("4. %4.2f" %(prom_toyota))
preg_nissan = autos_dias[:,11:16]
print("5. %d" %(np.sum(preg_nissan)))
preg_hyunday = autos_dias[:, 6:11]
preg_mazda = autos_dias[:, 16:21]
print("6. %d Toyota %d Hyunday %d Nissan %d Mazda" % (np.sum(preg_toyota), np.sum(preg_hyunday) ,np.sum(preg_nissan), np.sum(preg_mazda)) )
intereses = []
intereses.append(str(np.sum(preg_toyota))+"-Toyota+")
intereses.append(str(np.sum(preg_hyunday))+"-Hyunday+")
intereses.append(str(np.sum(preg_nissan))+"-Nissan+")
intereses.append(str(np.sum(preg_mazda))+"-Mazda+")
print("7. %s" %min(intereses))
prom_interesados = np.sum(autos_dias)/4
superaron_promedio_interesados = ""
for i in range(0,len(intereses)):
	if int(intereses[i].split("-")[0])>prom_interesados:
		superaron_promedio_interesados += intereses[i][intereses[i].find("-")+1:]+" "
print("8. Prom Interesados: %d:: %s"%(prom_interesados,superaron_promedio_interesados))
toyota_real =np.sum(preg_toyota[7:8,:])/np.sum(preg_toyota[0:7,:])
hyunday_real =np.sum(preg_hyunday[7:8,:])/np.sum(preg_hyunday[0:7,:])
nissan_real =np.sum(preg_nissan[7:8,:])/np.sum(preg_nissan[0:7,:])
mazda_real =np.sum(preg_mazda[7:8,:])/np.sum(preg_mazda[0:7,:])
print("9. Porc. Real %4.2f Toyota %4.2f Hyunday %4.2f Nissan %4.2f Mazda" %(toyota_real*100, hyunday_real*100, nissan_real*100, mazda_real*100))
modelos_ventas = {}
for i in range(0, len(marcas_autos)):
	modelos_ventas[marcas_autos[i]]=np.sum(autos_dias[:,i])
print("10.a "+str(sorted(modelos_ventas, key=modelos_ventas.get, reverse=True)[:5]).replace(" ",""))
#10-2da forma
modelos_ventas=[]
for i in range(0,len(marcas_autos)):
	modelos_ventas.append(str(np.sum(autos_dias[:,i]))+"+"+marcas_autos[i])
modelos_ventas=sorted(modelos_ventas, reverse=True)
print("10.b "+str(modelos_ventas[:5]))
print("11. %d" %(np.sum(autos_dias[:,13]) ))
