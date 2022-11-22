#punto 1
dizionario={}
dizionario["Giuseppe Gullo"]=[("corsa campestre",(40,21,0),"allievi"),("corsa 100mt",(0,12,0),"juniores mas"),("corsa 200mt",(0,29,19),"juniores mas")]
dizionario["Antonia Barbera"]=[("corsa campestre",(0,39,11),"juniores fem"),("corsa 100mt",(0,18,0),"juniores fem"),("corsa 200mt",(0,0,0),"juniores fem")]
dizionario["Nicola Esposito"]=[("corsa campestre",(0,43,22),"allievi"),("corsa 100mt",(0,14,0),"juniores mas"),("corsa 200mt",(0,39,19),"juniores mas")]

#punto 2
dizionario["Mattia Gostivari"]=[("corsa campestre",(10,22,0),"allievi"),("corsa 100mt",(0,14,0),"juniores mas"),("corsa 200mt",(0,27,10),"juniores mas")]

#punto 3
atleta=dizionario["Giuseppe Gullo"]
atleta.append(("corsa ad ostacoli 400mt",(0,40,34),"allievo"))
dizionario["Giuseppe Gullo"]=atleta

atleta=dizionario["Antonia Barbera"]
atleta.append(("corsa ad ostacoli 400mt",(0,39,10),"allieva"))
dizionario["Antonia Barbera"]=atleta

atleta=dizionario["Nicola Esposito"]
atleta.append(("corsa ad ostacoli 400mt",(0,40,10),"allievo"))
dizionario["Nicola Esposito"]=atleta

atleta=dizionario["Mattia Gostivari"]
atleta.append(("corsa ad ostacoli 400mt",(0,40,26),"allievo"))
dizionario["Mattia Gostivari"]=atleta
# controllo Spinarelli 9:36

#punto 4
print(dizionario["Giuseppe Gullo"][0])

#controllo Spinarelli 9:38

#punto 5
print("minuti: ",dizionario["Nicola Esposito"][2][1][0])
print("secondi: ",dizionario["Nicola Esposito"][2][1][1])
print("millisecondi: ",dizionario["Nicola Esposito"][2][1][2])

#controllo Spinarelli 9:42

#punto 6
print(dizionario["Antonia Barbera"][1][1])

#controllo Spinarelli 9:44

#punto 7
min=(0,14,0)
for chiave in dizionario.keys():
  if(dizionario[chiave][1][2]=="juniores mas"):
    if(dizionario[chiave][1][1][0]<min[0]):
      min=dizionario[chiave][1][1]
    elif(dizionario[chiave][1][1][0]>min[0]):
      min=min
    elif(dizionario[chiave][1][1][0]==min[0]):
      if(dizionario[chiave][1][1][1]<min[1]):
        min=dizionario[chiave][1][1]
      elif(dizionario[chiave][1][1][1]>min[1]):
        min=min
      elif(dizionario[chiave][1][1][1]==min[1]):
        if(dizionario[chiave][1][1][2]<min[2]):
          min=dizionario[chiave][1][1]
        elif(dizionario[chiave][1][1][2]>min[2]):
          min=min
        else:
          print("i tempi sono uguali")
print(f"il tempo minimo per la categoria juniores mas nella corsa 100 mt è: {min}")

#controllo Gornati 9:59

#punto 8

max=(0,29,19)
for chiave in dizionario.keys():
  if(dizionario[chiave][2][2]=="juniores mas"):
    if(dizionario[chiave][2][1][0]>max[0]):
      max=dizionario[chiave][2][1]
    elif(dizionario[chiave][2][1][0]<max[0]):
      max=max
    elif(dizionario[chiave][2][1][0]==max[0]):
      if(dizionario[chiave][2][1][1]>max[1]):
        max=dizionario[chiave][2][1]
      elif(dizionario[chiave][2][1][1]<max[1]):
        max=max
      elif(dizionario[chiave][2][1][1]==max[1]):
        if(dizionario[chiave][2][1][2]>max[2]):
          max=dizionario[chiave][2][1]
        elif(dizionario[chiave][2][1][2]<max[2]):
          max=max
        else:
          print("i tempi sono uguali")
print(f"il tempo massimo per la categoria juniores mas nella corsa 200 mt è: {max}")

#controllo Spinarelli 10:05

#punto 9
sommamin=0
sommasec=0
sommamilli=0
cont=0
for chiave in dizionario.keys():
  if(dizionario[chiave][0][2]=="allievi"):
    sommamin+=dizionario[chiave][0][1][0]
    sommasec+=dizionario[chiave][0][1][1]
    sommamilli+=dizionario[chiave][0][1][2]
    cont+=1
mediamin=sommamin/cont
mediasec=sommasec/cont
mediamilli=sommamilli/cont
media=(mediamin,mediasec,mediamilli)
print("la media nella corsa campestre categoria allievi sarà: ",media)

#controllo Spinarelli 10:27

#punto 10

def popola():
  n=int(input("inserisci numero atleti che vuoi inserire"))
  for i in range(n):
    aggiungi()

def aggiungi():
  chiave=leggichiave()
  lista=leggilista()
  dizionario[chiave]=lista

def leggichiave():
  chiave=""
  while(chiave in dizionario.keys()):
    chiave=input("inserisci una chiave")
  
def leggilista():
  lista=[]
  discipline=int(input("inserisci il numero di discipline"))
  for i in range(discipline):
    nomedis=legginomedis()
    tempo=leggitempo()
    categoria=leggicategoria()
  lista=[nomedis,tempo,categoria]
  return lista

def legginomedis():
  nome=input("inserisci il nome della disciplina")
  return nome

def leggitempo():
  tempi=()
  tempo1=int(input("inserisci il tempo dei minuti"))
  tempo2=int(input("inserisci il tempo dei secondi"))
  tempo3=int(input("inserisci il tempo dei millisecondi"))
  tempi=(tempo1,tempo2,tempo3)
  return tempi

def leggicategoria():
  categoria=input("inserisci la categoria")
  return categoria

scelta=1

if(scelta==1):
  popola()


#controllo Spinarelli 10:38
