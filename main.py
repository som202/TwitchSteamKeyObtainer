import socket
from pynput.keyboard import Controller, Key

def enterKey(key):

    keyboard = Controller()

    keyboard.type(key)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

def findKey(s):

    a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    for i in range(len(s)):
        try:
            if (s[i] in a) and (s[i + 5] == '-') and (s[i + 11] == '-'):
                t = i
                s = s[t:]
                s = s[0:17]
                enterKey(s)
                print(f"Found and activated key: {s}")
                break
        except:
            continue

server = 'irc.chat.twitch.tv'
port = 6667
username = input("Enter your twich username: ")
token = input("Enter your oauth token: ")
channel = '#' + input("Enter the twitch username whose chat you want to scan: ")

sock = socket.socket()

sock.connect((server, port))
sock.send(f"PASS {token}\n".encode('utf-8'))
sock.send(f"NICK {username}\n".encode('utf-8'))
sock.send(f"JOIN {channel}\n".encode('utf-8'))
print("- Scanning chat... Place your cursor on the textbox where u enter the key... (ctrl+c to stop)")

while True:
    res = sock.recv(2048).decode('utf-8')

    if res.startswith('PING'):
        sock.send("PONG\n".encode('utf-8'))

    res = res.split(":")[-1]

    findKey(res)
