from des import DesKey

key0 = DesKey(b"test key")

data = "one two three four"

print("original")
print(data)

encrypted_data = key0.encrypt(data.encode('utf-8'), padding=True)

print("encrypted:")
print(encrypted_data)

decrypted_data = key0.decrypt(encrypted_data, padding=True)

print("decrypted:")
print(decrypted_data.decode('utf-8'))
