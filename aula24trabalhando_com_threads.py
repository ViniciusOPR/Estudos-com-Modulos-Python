# (Parte 1) Threads - Executando processamentos em paralelo
from collections.abc import Callable, Iterable, Mapping
from threading import Lock, Thread
from time import sleep

"""
class MeuThread(Thread):
    def __init__(self, texto: str, tempo: int):
        self.texto = texto
        self.tempo = tempo

        super().__init__()
    
    def run(self):
        sleep(self.tempo)
        print(self.texto)

t1 = MeuThread('Thread 1', 2)
t1.start()

t2 = MeuThread('Thread 2', 3)
t2.start()

t3 = MeuThread('Thread 3', 5)
t3.start()

for i in range(15):
    print(i)
    sleep(1)
"""

# (Parte 2) Threads - Executando processamentos em paralelo
"""
def vai_demorar(texto: str, tempo: int):
    sleep(tempo)
    print(texto)

t4 = Thread(target=vai_demorar, args=('Olá Mundo 1', 5))
t4.start()

t5 = Thread(target=vai_demorar, args=('Olá Mundo 2', 1))
t5.start()

t6 = Thread(target=vai_demorar, args=('Olá Mundo 3', 2))
t6.start()

for a in range(15):
    print(a)
    sleep(.5)
"""
class Ingressos:
    """
    Classe que vende ingressos
    """

    def __init__(self, estoque: int):
        """ Inicializando...

        :param estoque: quantidade de ingressos em estoque
        """
        self.estoque = estoque
        # Nosso cadeado
        self.lock = Lock()

    def comprar(self, quantidade: int):
        """
        Compra determinada quantidade de ingressos

        :param quantidade: A quantidade de ingressos que deseja comprar
        :type quantidade: int
        :return: Nada
        :rtype: None
        """
        # Tranca o método
        self.lock.acquire()

        if self.estoque < quantidade:
            print('Não temos ingressos suficientes.')
            # Libera o método
            self.lock.release()
            return

        sleep(1)

        self.estoque -= quantidade
        print(f'Você comprou {quantidade} ingresso(s). '
              f'Ainda temos {self.estoque} em estoque.')

        # Libera o método
        self.lock.release()


if __name__ == '__main__':
    ingressos = Ingressos(10)

    for i in range(1, 20):
        t = Thread(target=ingressos.comprar, args=(i,))
        t.start()

    print(ingressos.estoque)