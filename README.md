# Security_Lab_1 security lab 1 

## Dependencies
Currently Python2.7 and 3 are needed, will fix later.
Install DES library.
```
sudo apt install python3-pip
sudo pip3 install des
```

## Usage
This package provides a server hosted chatroom, where messages are encrypted at endpoints using DES.

Run the server in python2 for now.
To run as a demo, use the loopback address and a random port number:
```
python server.py 127.0.0.1 9909
```

Then clients connect using the same ip and port number:
```
python3 client.py 127.0.0.1 9909
```

Each connection and message will be displayed on the server, but unreadable without the secret key.
 
![Screenshot](https://raw.githubusercontent.com/curtisghc/Security_Lab_1/master/Screenshot.png)


Key must be placed in the running directory as "key.txt".
