# Python program to implement client side of chat room.
import socket
import select
import sys
from des import DesKey
import random
import string
import re


def keygen(length=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def write_key(key):
    with open("key.txt", 'w') as fp:
        fp.write(key)
    print("Key written to \"key.txt\"")


def read_key():
    with open("key.txt", 'r') as fp:
        return fp.read()


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if len(sys.argv) != 3:
    print("Correct usage: script, IP address, port number")
    exit()

should_generate = input("Generate new key? (y/n)")

if (should_generate == "y"):
    key = keygen(8)
    write_key(key)
else:
    key = read_key()

key0 = DesKey(key.encode('utf-8'))

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if len(sys.argv) != 3:
    print("Correct usage: script, IP address, port number")
    exit()
IP_address = str(sys.argv[1])
Port = int(sys.argv[2])
server.connect((IP_address, Port))

while True:

    # maintains a list of possible input streams
    sockets_list = [sys.stdin, server]

    """ There are two possible input situations. Either the
    user wants to give  manual input to send to other people,
    or the server is sending a message  to be printed on the
    screen. Select returns from sockets_list, the stream that
    is reader for input. So for example, if the server wants
    to send a message, then the if condition will hold true
    below.If the user wants to send a message, the else
    condition will evaluate as true"""
    read_sockets, write_socket, error_socket = select.select(sockets_list, [], [])

    for socks in read_sockets:
        if socks == server:
            message = socks.recv(2048)
            message = message.split(b' ')
            try:
                message[1] = key0.decrypt(message[1], padding=True)
            except:
                print("[Unable't decrypt message from " + message[0] + "]")
            else:
                message = message[0] + b' ' + message[1]
                message = message.decode('utf-8')
                print(message)
        else:
            message = sys.stdin.readline()
            sys.stdout.write("<You>")
            sys.stdout.write(message)
            message = key0.encrypt(message.encode('utf-8'), padding=True)
            server.send(message)
            sys.stdout.flush()
server.close()
