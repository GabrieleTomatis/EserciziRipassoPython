valore = int(input("Inserisci un valore a tuo piacimento: "))

#inizializzo una variabile temporanea, che chiamo temp, assegnando il suo valore ad 1
temp = 1

#faccio un for, che come range, ha l'espressione necessaria per calcolare il fattoriale del numero inserito in input
for i in range(2, valore + 1):

    #utilizzo la variabile temp, che ha valore 1 (elemento neutro della moltiplicazione), e lo moltiplico per il valore di i
    temp = temp * i
 
print(temp)
