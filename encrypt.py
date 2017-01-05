from simplecrypt import encrypt,decrypt
password = "123"
cipher = encrypt(password, "Hellloooo")
print(cipher) 
plain = decrypt(password, cipher) 
print(plain)
