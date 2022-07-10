In this repository you will find a "server.py" python script. This script will listen on the port that is specified in "port.txt". 
To communicate with this server, you will have to send the length of a message in numbers, but encrypted, and filled to 256 bytes with binary spaces.

Exaple:

def send(msg):
    message = msg.encode("utf-8")
    message_length = len(message)
    send_length = str(message_length).encode("utf-8")
    send_length += b" " * (256 - len(send_length))
    client.send(send_bits)
    client.send(message)

if you want to disconnect from the server, you will have to do send("disc").
So the server will write all the messages, so not the lengths, to a txt file called "txt.txt" in this case.
I have include a client script that takes all wifi passwords from all the wifi networks you have been connected to, formats them nicely, and sends them to the server.
You have the option to change the port, but you have to do it on both the client side and server side, or you could make it so it grabs the port from another server, so you change it there and it will always work.
You also have the option to change the maximum size of the message, by changing the value of 256 to something  bigger or smaller. I have not tested the performance difference, but it is not to noticeble with smaller values.

Note: You can only connect to the server if all the info is correct, and if the server script is running with the right local ip.

And if you want to connect from anywhere in the world, you can use global ip in the client side. But then you have to set-up port fowarding on your router, so that it fowards to the right port on your machine where server.py is running.
(Note: sometimes you can't use your global ip if the server is on the same network as the client, since most router can't send traffic to their own ip adress.)
This is one of the most basic server setups, but i hope you have fun with it if you want to use it, and for handeling more traffic at once, setup Multithreading.

