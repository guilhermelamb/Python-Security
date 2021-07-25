import ctypes

atributo_ocultar = 0x02

retorno = ctypes.windll.kernel32.SetFileAttributesW('file_to_be_hidden.txt', atributo_ocultar)

if retorno:
    print('Arquivo ocultado')
else:
    print('Arquivo não foi ocultado')