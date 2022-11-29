import pprint
pp=pprint.PrettyPrinter(indent=4)
prenotazioni={}

def leggiChiave():
  fila=""
  numero=""
  fila=input("inserisci la fila: ")
  while len(fila)==0:
    fila=input("inserisci la fila: ")
  numero=input("inserisci il numero dell'ombrellone: ")
  while len(numero)==0:
    numero=input("inserisci il numero dell'ombrellone: ")
  return [fila,numero]
#-----------------------------------------------------------------
def leggiDati():
  prezzoB=input("inserisci il prezzo bassa stagione: ")
  while len(prezzoB)==0:
    prezzoB=input("inserisci il prezzo bassa stagione: ")
  prezzoA=input("inserisci il prezzo alta stagione: ")
  while len(prezzoA)==0:
    prezzoA=input("inserisci il prezzo alta stagione: ")
  giorno=input("inseriesci il giorno: ")
  mese=int(input("inseirisci il mese: (6 giugno, 7 luglio, 8 agosto, 9 settembre"))
  while (mese>9 or mese<6):
    mese=input("inseirisci il mese: ")
  anno=input("inserisci l'anno: ")
  if(mese==7 or mese==8):
    prezzo=prezzoA
  elif(mese==6 or mese==9):
    prezzo=prezzoB
  nGiorni=int(input("inserisci numero di giorni: "))
  prezzo=prezzo*nGiorni
  while nGiorni==0:
    nGiorni=input("inserisci numero di giorni: ")
  opSdraio=int(input("(opzionale) vuoi una sdario in più?"))
  if(opSdraio>1):
    while(i==opSdraio):
      prezzo=prezzo+prezzo/3
      i+=1;
  opLettino=int(input("(opzionale) vuoi un lettino in più?"))
  if(opLettino>1):
    while(i==opLettino):
      prezzo=prezzo+prezzo/2
      i+=1;
  return[(prezzoB,prezzoA),(giorno,mese,anno),nGiorni,prezzo]
  #-----------------------------------------------------------
#1
def popola():
  nPrenotazioni=int(input("Quante prenotazioni vuoi aggiungere? ="))
  for i in range (nPrenotazioni):
    chiave=leggiChiave()
    if chiave in prenotazioni:
      print("CONTATTO GIA' ESISTENTE!")
      chiave=leggiChiave()
      print("CONTATTO GIA' ESISTENTE!")
      while(chiave in prenotazioni):
         chiave=leggiChiave()
      dati=leggiDati()
      prenotazioni[chiave]=dati
    else:
      dati=leggiDati()
      prenotazioni[chiave]=dati
  pp.pprint(prenotazioni) 
#2
def mostraPrenotazioneSingola():
  chiave=leggiChiave()
  if chiave in prenotazioni:
    print(prenotazioni[chiave])
  else:
    print("prenotazione non esistente")
#3
def mostraTuttePrenotazioni():
  pp.pprint(prenotazioni)





#menu'
scelta=1
while (scelta!=0):
  print('0) Esci')
  print('1) Popola')
  print('2) Mostra le prenotazioni di un ombrellone')
  print('3) Mostra tutte le prenotazioni')
  print('4) Riduzione prezzo percentuale')
  print('5) Calcolo incasso totale di un mese')
  print('6) Visualizza le prenotazioni di n mesi')
  scelta=int(input('Scegli :'))
  if scelta==1:
    popola()
  elif scelta==2:
    mostraPrenotazioneSingola()
  elif scelta==3:
    mostraTuttePrenotazioni()
  elif scelta==4:
    riduzionePrezzo()
  elif scelta==5:
    incassoMensile()
  elif scelta==6:
    mostraPrenotazioniMesi()
