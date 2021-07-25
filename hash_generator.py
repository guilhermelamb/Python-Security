import hashlib

string = input('Digite o texto a ser gerado a hash: ')

resultado_md5 = hashlib.md5(string.encode('utf-8'))
resultado_sha1 = hashlib.sha1(string.encode('utf-8'))
resultado_sha224 = hashlib.sha224(string.encode('utf-8'))
resultado_sha256 = hashlib.sha256(string.encode('utf-8'))
resultado_sha384 = hashlib.sha384(string.encode('utf-8'))

print('O hash md5 é: ', resultado_md5.hexdigest())
print('O hash sha1 é: ', resultado_sha1.hexdigest())
print('O hash sha224 é: ', resultado_sha224.hexdigest())
print('O hash sha256 é: ', resultado_sha256.hexdigest())
print('O hash sha384 é: ', resultado_sha384.hexdigest())