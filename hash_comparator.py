import hashlib

message1 = 'message1.txt'
message2 = 'message2.txt'

hash1 = hashlib.new('ripemd160')
hash1.update(open(message1, 'rb').read())

hash2 = hashlib.new('ripemd160')
hash2.update(open(message2, 'rb').read())

if hash1.digest() != hash2.digest():
    print(f'O arquivo {message1} é diferente do {message2}')
else:
    print(f'O arquivo {message1} é igual ao {message2}')