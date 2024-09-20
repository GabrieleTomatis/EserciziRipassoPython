
#creo un dizionario
dizionario = {
    "a": 1,
    "b": 2,
    "c": 3,
} 

#printo il dizionario, per vedere se effettivamente me lo stampa, è solo un test mio
print(dizionario)

#inizializzo il dizionario, che dovra avere le chiavi scambiate con i valori
dizionario_scambio_chiaveValore = {}

#scrivo un for, che itera sul dizionario leggendo chiave e valore, il metodo .items, serve per iterare sui dizionari, senza esso, ciclerei solo sulle chiavi e non avrei i valori
for chiave, valore in dizionario.items():

    #assegno al posto del valore la chiave
    dizionario_scambio_chiaveValore[valore] = chiave

print(dizionario_scambio_chiaveValore) 
