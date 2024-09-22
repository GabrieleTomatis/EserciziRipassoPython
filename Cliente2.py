import socket as s

udp_client_socket = s.socket(s.AF_INET, s.SOCK_DGRAM)

server_address = ("192.168.1.51", 6980) #ip server + porta
BUFFER_SIZE = 4092 #grandezza buffer

for i in range(10):
    messaggio = "ciao!!" + str(i+1)
    udp_client_socket.sendto(messaggio.encode("utf-8"), server_address)

data, server_address = udp_client_socket.recvfrom(BUFFER_SIZE)

print(f"Messaggior ricevuto da server: {data.decode()} da {server_address}")

