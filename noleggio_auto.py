import pprint
pp=pprint.PrettyPrinter(indent=4)
noleggio={}

#1
noleggio["AA123BB"]=[("Giugno",9,1293),("Luglio",7,3231),("Agosto",7,4020),("Settembre",6,3928)]
noleggio["AB345CD"]=[("Giugno",8,1391),("Luglio",6,1234),("Agosto",9,4932),("Settembre",8,2872)]
noleggio["CD456FF"]=[("Giugno",7,2872),("Luglio",6,3273),("Agosto",4,3211),("Settembre",8,2827)]

#2
noleggio["ZZ999MG"]=[("Giugno",10,1000*10),("Luglio",10,1000*10),("Agosto",10,1000*10),("Settembre",10,1000*10)]

#3
print("tutte le informazioni sul mese di Luglio della targa AA123BB")
print(noleggio["AA123BB"][1])

#4
print("numero di noleggi nel mese di Luglio della targa AA123BB")
print(noleggio["AA123BB"][1][1])

#5
somma=0
for i in range (len(noleggio["AB345CD"])):
  somma+=noleggio["AB345CD"][i][2]
print(f"la somma di tutti i KM dell'auto AB345CD è: {somma}")

#6
tot=0
for chiave in noleggio:
  print(chiave)
  for i in range (len(noleggio[chiave])):
    tot+=noleggio[chiave][i][2]
print(f"la somma di tutti i kilometri è: {tot}")

#7
max=0
cont=0
for i in range (len(noleggio["CD456FF"])):
  if(noleggio["CD456FF"][i][2]>max):
    max=noleggio["CD456FF"][i][2]
    cont=i
print(f"il mese con più kilometri per la targa CD456FF è: {noleggio['CD456FF'][cont]}")


