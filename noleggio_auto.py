#1
diz={"AA123BB":[("giugno",9,1293),("luglio",7,3231),("agosto",7,4020),("settembre",6,3928)],
     "AB345CD":[("giugno",8,1391),("luglio",6,1234),("agosto",9,4932),("settembre",8,2872)], 
     "CD456FF":[("giugno",7,2872),("luglio",6,3273),("agosto",4,3211),("settembre",8,2827)]}
print(diz)
#2
diz["ZZ999BM"]=[("giugno",10,1000),("luglio",10,1000),("agosto",10,1000),("settembre",10,1000)]
print(diz)
#3
print(diz["AA123BB"][1])
print(f"mese: {diz['AA123BB'][1][0]}")
print(f"numero noleggi: {diz['AA123BB'][1][1]}")
print(f"kilometri: {diz['AA123BB'][1][2]}")
#4
print(f"numero noleggi: {diz['AA123BB'][1][1]}")
#5
kmTot=0
for i in range(4):
  kmTot+=diz['AB345CD'][i][2]
print(f" la somma di tutti i km in tutti i mesi per la targa AB345CD è: {kmTot}")
#6
somma=0
for targa, dati in diz.items():
  #print(targa,dati)
  #print(dati)
  for dato in dati:
    somma+=(dato[2])
print(f"la somma di tutti i km è: {somma}")
#7
print(diz["CD456FF"])
print(diz["CD456FF"][0][2])
y=(diz["CD456FF"][0][2])
for i in range (4):
  if(diz["CD456FF"][i][2])>y:
    oo=i
print(oo)
print(diz["CD456FF"][oo][2])
