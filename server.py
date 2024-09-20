import socket as s

server_address = ("192.168.65.103", 6980)
BUFFER_SIZE = 4092 #uanti bit posso inviare o ricevere

udp_server_socket = s.socket(s.AF_INET, s.SOCK_DGRAM) #dgram è per udp stream è per tcp
udp_server_socket.bind(server_address)

data, address = udp_server_socket.recvfrom(BUFFER_SIZE) #quando un client invia dei dati, vengono messi in data
print(f"Messaggio ricevuto: {data.decode('utf8')} da {address}")
