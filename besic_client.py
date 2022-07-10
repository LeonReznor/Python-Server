import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ADDR = ("global/local ip here", "your port here")
client.connect(ADDR)

message = "Hello World!".encode("utf-8")
msg_bits = len(message)
send_bits = str(msg_bits).encode("utf-8")
send_bits += b" " * (256 - send_bits)
client.send(send_bits)
print("len sent")
client.send("Hello World!".encode("utf-8"))
print("message sent")

message = "disc".encode("utf-8")
msg_bits = len(message)
send_bits = str(msg_bits).encode("utf-8")
send_bits += b" " * (256 - send_bits)
client.send(send_bits)
print("len sent")
client.send("disc".encode("utf-8"))
print("disconnect sent")