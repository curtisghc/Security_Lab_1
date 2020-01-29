from des import DesKey
import random
import string

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

should_generate = input("Generate new key? (y/n)")

if(should_generate == "y"):
    key = keygen(8)
    write_key(key)
else:
    key = read_key()

key0 = DesKey(key.encode('utf-8'))

#ip_str = input("Enter the ip to chat")

print("Write messages, \'quit\' to quit")

while (True):
    data = input(">")
    if(data == 'quit'):
        break
    encrypted_data = key0.encrypt(data.encode('utf-8'), padding=True)
    print(encrypted_data)


    decrypted_data = key0.decrypt(encrypted_data, padding=True)

    print('decrypted')
    print(decrypted_data.decode('utf-8'))
