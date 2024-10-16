import hashlib

while True:
    string = input("digite para gerar o hash ou 'sair' para encerrar:")
    if string.lower() == 'sair':
        break
    
    hash_object = hashlib.sha1(string.encode())
    
    print("Hash SHA-1:", hash_object.hexdigest())
