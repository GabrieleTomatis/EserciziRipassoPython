import socket as s

server_address = ("192.168.1.51", 6980) #ip server + porta
BUFFER_SIZE = 4092 #grandezza buffer

udp_server_socket = s.socket(s.AF_INET, s.SOCK_DGRAM)#uso ipv4 e udp
udp_server_socket.bind(server_address)#sto associando l'oggetto che abbiamo creato all'ip e alla porta inizializzata sopra

while True:
    data, address = udp_server_socket.recvfrom(BUFFER_SIZE)
    print(f"{data.decode('utf-8')}, da {address}")

    if(data.decode('utf-8').lower() == "arrivederci"):
        print("il cliente ha terminato la connessione")
        break

    risposta = input("rispondi al messaggio: ")
    udp_server_socket.sendto(risposta.encode('utf-8'), address)

    if(risposta.lower() == "arrivederci"):
        print("il server ha terminato la connessione")
        break

udp_server_socket.close()