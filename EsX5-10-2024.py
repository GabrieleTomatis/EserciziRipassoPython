# Crea un software che stampi il nome del tasto cliccato su tastiera (solo lettere)
# Usa la libreria:
# pynput

numeri = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

#importo la libreria richiesta
from pynput import keyboard


#stampa lettere
def on_press(key):
    # bisogna verificare che gli input non siano altri tasti, gestisco eccezione!!
    try:
        #stampo carattere quando è una lettera
        if key.char not in numeri and key.char != None:
            print('alphanumeric key {0} pressed'.format(key.char))
        
    except AttributeError:
        #non stampo quando il carattere non è riconosciuto
        if key == keyboard.Key.esc:
            return False
        else:
            pass

# Creo un event listener che entra in azione quando schiaccio sulla tastiera
# è un thread!! viene eliminato alla pressione di esc
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

# creo il thread e gli assegno la funzione
listener = keyboard.Listener( on_press=on_press)
listener.start()