from operator import truediv
import socket
import os
with open("port.txt", "r") as f:
    port = f.read()  
ServerIP = "0.0.0.0"
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Head = 256
form = "utf-8"
server.bind((ServerIP, int(port)))

def serv_scr(conn, addr):
    print("connected")
    connected = True
    printlist = []
    while connected:
        msg_leng = conn.recv(Head).decode(form)
        if msg_leng:
            print("message recieved")
            msg_leng = int(msg_leng)
            msg = conn.recv(msg_leng).decode(form)
        if msg == "disc":
            print("disconnected")
            connected = False
        if msg != "disc":
            printlist.append(msg)

    if os.path.exists("txt.txt"):
        with open("txt.txt", "r") as file:
            cont = file.read().splitlines()
        with open("txt.txt", "w") as file:
            for i in cont:
                if i in printlist:
                    continue
                else:
                    printlist.append(i)

            for i in printlist:
                file.write(i + "\n")

    else:
        with open("txt.txt", "w") as file:
            for i in printlist:
                file.write(i + "\n")
    conn.close

def serv():
    server.listen()
    while True:
        conn, addr = server.accept()
        serv_scr(conn, addr)
        

print("Server started")
serv()


input()