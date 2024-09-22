import socket as s

udp_client_socket = s.socket(s.AF_INET, s.SOCK_DGRAM)

server_address = ("192.168.1.51", 6980) #ip server + porta
BUFFER_SIZE = 4092 #grandezza buffer

while True:
    messaggio = input("Manda un messaggio: ")
    udp_client_socket.sendto(messaggio.encode('utf-8'), server_address)

    if(messaggio.lower() == "arrivederci"):
        print("Il cliente ha terminato la connessione")
        break

    data, address = udp_client_socket.recvfrom(BUFFER_SIZE)
    print(f"{data.decode('utf-8')}, da {address}")

    if(data.decode('utf-8').lower() == "arrivederci"):
        print("Il server ha terminato la connessione")
        break

udp_client_socket.close()