import time
from threading import  Thread

def carro(velocidade, piloto):
    trajeto = 0
    while trajeto <= 100:
        print('Piloto: {}, km: {}'.format(piloto, trajeto))
        trajeto += velocidade
        time.sleep(0.5)


t_carro1 = Thread(target=carro, args=[10, 'Mepes'])
t_carro2 = Thread(target=carro, args=[20, 'Iggy'])

t_carro1.start()
t_carro2.start()