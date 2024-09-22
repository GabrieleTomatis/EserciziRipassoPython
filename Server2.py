import socket as s

server_address = ("192.168.65.103", 6980) #ip server + porta
BUFFER_SIZE = 4092 #grandezza buffer

udp_server_socket = s.socket(s.AF_INET, s.SOCK_DGRAM)#uso ipv4 e udp
udp_server_socket.bind(server_address)#sto associando l'oggetto che abbiamo creato all'ip e alla porta inizializzata sopra

for i in range(10):
    data, address = udp_server_socket.recvfrom(BUFFER_SIZE) #ricevo i dati dal client
    print(f"Messaggio ricevuto: {data.decode('utf8')} da {address}")

udp_server_socket.sendto("Messaggi ricevuti con successo".encode("utf-8"), address)
udp_server_socket.close()